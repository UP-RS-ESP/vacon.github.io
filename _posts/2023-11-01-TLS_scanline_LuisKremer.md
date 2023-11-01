---
title: 'A line-based segmentation and subsampling approach for classifying point clouds using the random forest algorithm'
author: "Luis Kremer"
author_profile: true
date: 2023-10-23
# permalink:
toc: true
toc_sticky: true
toc_label: "A line-based segmentation and subsampling approach for classifying point clouds using the random forest algorithm"
header:
  overlay_image: https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/00_cover_img.png
  overlay_filter: 0.3
  caption: "Segmented and subsampled point clouds representing an oak tree on the campus of the University of Potsdam"
read_time: false
tags:
  - TLS
  - LiDAR
  - line-based approach
  - segmentation
  - classification
  - random forest
---

Dense point clouds generated from Terrestrial Lidar Scanner pose a challenge to classification algorithm because of their large data amounts. Here a scanline segmentation approach for phase-based lidar scanner is presented that will allow to apply common classification algorithms.

# Introduction

3D data acquired from devices like laser scanners are commonly shown as point clouds (PCDs). Classifying point clouds with supervised machine learning algorithms can have two fundamental challenges: 1) the amount of data is large and lead to computationally expensive calculation that may exceed the capabilities of current GPUs; and 2) unlike gridded 2D data (e.g., images or digital elevation models), raw point clouds are irregularly shaped and unstructured, making it challenging to apply conventional 2D machine learning methods (Hu et al., 2020; Su et al., 2018; Thomas et al., 2019).

To address these challenges in classification, recent studies have employed pre-processing techniques to convert irregular point clouds into a uniform 3D volumetric grid using voxelization. While voxelization aids in subsampling and structuring the data, it results in the loss of geometric details and natural variances prevailing in the raw point cloud (Liu et al., 2019; Su et al., 2018). This loss of information is particularly significant in forest ecology, where detailed analyses of structural metrics (e.g., leaf shape, branch dimensions, or crown properties) from Terrestrial Laser Scanning (TLS) data is essential (Calders et al., 2020).

This work addresses the issue of information loss due to pre-processing steps of point clouds such as voxelization. Based on a scanline segmentation and subsampling approach, we seek to significantly reduce the amount of data while keeping most relevant information of the points within a segment. We use a Random Forest (RF) classifier to classify the subsampled data and map the results back to the raw point cloud. The outcome is a classification on the raw, full resolution data, enabling to extract features like trees or leaves without having information loss.

*This internship was supervised by Prof. Dr. Bodo Bookhagen.*

# Methods

## Study site and data acquisition

Ten TLS scans of an oak tree were acquired on the campus of the University of Potsdam in April 2023 (Figure 1). The TLS scanner used was the Z+F Imager 5016, which translates the phase shift between the outgoing and incoming laser pulses into distance estimates (Calders et al., 2020). The scanner provides x-y-z coordinates, intensity (backscatter strength) and RGB information for each point. About 6-7 million points were recorded per scan.

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/01_study_area.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/01_study_area.png" width="90%" height="90%" ></a><figcaption> Figure 1: Excerpt of the ten scans processed in the Z+F LaserControl software. The dots are the individual scan positions around the oak tree. The lines are the connections between the scans and the markers detected for alignment. The bold lines are walls. </figcaption>
</figure>
</center>

## Scanline extraction

Point clouds can be described by either using the commonly encountered Cartesian coordinates ($x$, $y$, $z$) or spherical coordinates. In spherical coordinates, a point vector is described by the radial coordinate $r$ (distance from the scanner to the point), the vertical angle $theta$ (angle with respect to the z-axis) and the horizontal angle $phi$ (angle with respect to the x-y axis).

A TLS scans the environment in discrete scanlines that are closely spaced (Figure 2b). Points along a scanline have either similar vertical angles (vertical scanline) or similar horizontal angles (horizontal scanline). In this work, we focus on points with similar horizontal angles to extract the scanlines.

Sorting all points of one scan by their horizontal angles results in a stepped line (Figure 2a). Each step represents a slight rotation of the scanner around the vertical axis, indicating the start of a new scanline.

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/02_scanline_extraction.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/02_scanline_extraction.png" width="90%" height="90%" ></a><figcaption> Figure 2:  Shows the first 20,000 points from scan 1, sorted by horizontal angle (Φ). Figure A shows the plot of the point index against the horizontal angle. Figure B shows the same scene as a 3D plot, displaying points with their corresponding x-y-z coordinates. The red dot indicates the position of the scanner. The scene depicts the point cloud within a range of about 1 centimeter in the x-direction, 30 meters in the y-direction, and 15 meters in the z-direction. There is a wall on the left and the oak tree on the right side of the scanner. </figcaption>
</figure>
</center>

Steps are identified by calculating the difference between consecutive points in the sorted point cloud. A significant difference indicates a knickpoint, which is the beginning of a new scanline (Figure 3). A threshold of 0.002 degrees was chosen. Whenever the difference between two points exceeded this threshold, the point cloud was split at this index creating a new scanline. With this method, about 5000 scanlines were extracted from a single TLS scan.

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/03_scanline_extraction.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/03_scanline_extraction.png" width="90%" height="90%" ></a><figcaption> Figure 3: Figure A shows the point cloud separated by the scanline boundaries. Each color represents an individual scanline. Figure B shows the same scene as a 3D plot. The colors in A mark the corresponding scanline in B. </figcaption>
</figure>
</center>

## Scanline segmentation

For each scanline (Figure 4), a two-step segmentation process was implemented. First, the radial distance differences (RDD; x-axis of Figure 4a) of consecutive point pairs were calculated on the sorted and extracted scanline. For example, the differences in $r$ across the scanline are large (Figure 4a) when there is a gap between two groups of points. Whenever the difference exceeded a predetermined threshold, the scanline was divided at that point, creating a new segment (Figure 5). A RDD threshold value of 0.4 m was selected for this work. For the specific scanline shown in Figure 5, the segmentation based on radial distance differences resulted in 21 segments.

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/04_scanline_segmentation.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/04_scanline_segmentation.png" width="90%" height="90%" ></a><figcaption> Figure 4: Shows the first scanline from scan 1 as A) the scanner distance (<i>r</i>) against the height [m], and B) as a 3D plot.  </figcaption>
</figure>
</center>

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/05_scanline_segmentation.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/05_scanline_segmentation.png" width="90%" height="90%" ></a><figcaption> Figure 5: Shows the first scanline from scan 1, segmented using radial differences between points. Each color represents a segment.  </figcaption>
</figure>
</center>

In the second segmentation step, the segments generated in the previous stage underwent further processing based on differences in slope. For each consecutive pair of points within a segment, the slope was calculated. For a number of $n$ points within a segment the slope calculation can be expressed as:

$$
\[ d_i = \\sqrt{\\left| (x\_{2i} - x\_{1i})^2 \\right| + \\left| (y\_{2i} - y\_{1i})^2 \\right| + \\left| (z\_{2i} - z\_{1i})^2 \\right| }\]

\[ m\_{\\text{deg}, i} = \\arctan \\left( \\frac{z\_{1i} - z\_{2i}}{d_i} \\right) \]
$$
where:

- $i$ ranges from 1 to $n$-1
- $d\_{i}$ is the 3D distance between each of the $n$-1 consecutive point pairs ((x\_{1i}, y\_{1i}, z\_{1i})) and ((x\_{2i}, y\_{2i}, z\_{2i}))
- (m\_{\\text{deg}, i}) is the slope between each of the n-1 consecutive point pairs in degrees

Similarly to the previous segmentation stage, for each computed slope value, the difference in slope between successive pairs was calculated. If the difference exceeded a certain slope threshold, the segment was further divided (Figure 6). For this work, a slope threshold of 25 degrees was chosen.

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/06_scanline_segmentation.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/06_scanline_segmentation.png" width="90%" height="90%" ></a><figcaption> Figure 6: Shows the first scanline from scan 1, further segmented using slope differences between points. Each color represents a segment.  </figcaption>
</figure>
</center>

## Scanline subsampling

Finally, each segment was reduced to its centroid, representing the median position of all points within the segment. It can be considered as the center of mass of the segment. However, to preserve the natural structure of the input point cloud, the point closest to the centroid was chosen as the centroid (Figure 7).

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/07_01_centroid_subsampling.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/07_01_centroid_subsampling.png" width="90%" height="90%" ></a><figcaption> Figure 7: Centroid subsampling of the first scanline from scan 1. Each segment is condensed to the closest point to the segment median (red dots). </figcaption>
</figure>
</center>

During this process, 12 attributes characterizing the segment were calculated and assigned to the centroid. The attributes are the **mean** and **variance** of:

- Red
- Green
- Blue
- Intensity
- Rho ($r$)
- Height ($z$)

Thus, along with the x-y-z coordinates, every centroid was represented by an array in the form of a row with 15 columns (1, 15). With a total of $n$ segments resulting from the segmentation process, the final subsampled point cloud array had the shape ($n$, 15) (Figure 8).

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/07_02_example_subsampling_scan01.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/07_02_example_subsampling_scan01.png" width="90%" height="90%" ></a><figcaption> Figure 8: Centroid subsampling result of the first scan. The point colors represent the mean intensity per segment. The brighter the color, the higher the intensity. The original full resolution data of 6,711,986 points was subsampled to 227,136 points. </figcaption>
</figure>
</center>

In order to incorporate the RF classification results from the centroid subsampled data into the raw, full resolution point clouds, each segment and its corresponding centroid was associated with a separate array containing the segment ID. Thus, each segment was identified by its unique ID, and the corresponding centroid shared the same ID.


# Application: random forest classification

The ten centroid subsampled point clouds were used as the starting point for a random forest classification. A random forest consists of multiple decision trees, each generated independently by sampling subsets of the training data. The final classification is determined by the majority class among the trees. This means that each tree contributes a vote for the class assignment. The class with the most votes is finally selected (Belgiu und Drăguţ, 2016). The number of trees generated for the RF classifier is user-defined - for this work a value of 100 was chosen.

We selected an RF classifier rather than a neural network approach because of its suitability for classification tasks with limited training data. Its architecture, based on decision trees, mitigates overfitting caused by an unbalanced selection of training data (Belgiu und Drăguţ, 2016). In addition, the RF classifier efficiently manages numerous input features and automatically selects the most appropriate ones for the final classification. That enables a transparent evaluation of the importance of different features after training, helping to determine the relevance of each feature (Niemeyer et al., 2014; Weinmann et al., 2015).

## Classification workflow

Before training and applying the RF classifier to the ten point clouds derived from the data acquisition, they were processed using the scanline segmentation approach and centroid subsampling described in the previous chapter. The first scan of the subsampled datasets was used for both training and testing the RF classifier. The trained model was then applied to the remaining nine scans to classify the point clouds. After classification of the centroid subsampled point clouds, the results were re-incorporated into the original full resolution data. The overall accuracy metric was used to evaluate the classification. It is important to note that we acknowledge the limitations of relying on accuracy alone as a metric to evaluate the performance of the RF classifier. However, the focus was on assessing the general applicability of the method rather than incorporating fully comprehensive performance measures of the model. Therefore, only this metric was used in the evaluation.

## Training labels

Manual labeling was applied to all points within the ten point clouds. Our focus was on ground and vegetation related features. As a result, a significant amount of points were designated as unclassified, relating to objects such as walls, bicycles, cars or street lights. The classes considered for training/testing and prediction included:

- Class 0: unclassified
- Class 2: ground
- Class 3: low vegetation
- Class 4: leaves
- Class 5: tree

For the training data set, the classes were unbalanced. Therefore, class weights were applied based on their respective frequencies:

| Class | Frequency | Weight |
|-------|-----------|--------|
| 0 | 24\.469 | 1\.94 |
| 2 | 41\.793 | 1\.14 |
| 3 | 2\.369 | 20\.03 |
| 4 | 97\.202 | 0\.49 |
| 5 | 71\.379 | 0\.66 |

# Results

## Overall accuracy

The overall accuracy assessment of the RF classification results was performed on the centroid subsampled point clouds and the raw, full resolution point clouds (Figure 9). For all datasets, the accuracy is above 90%, indicating a strong overall classification performance. Scans closer to the first scan (training dataset), such as scans 2, 3, 9, and 10, generally have higher accuracy scores than scans further away, such as scans 5, 6, and 7. The centroid subsampled datasets show slightly better results compared to the back-labeled full resolution datasets. However, these differences are small for most scans, becoming noticeable only for scans 5 and 7.

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/08_rf_results.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/08_rf_results.png" width="90%" height="90%" ></a><figcaption> Figure 9: Result of the random forest classification on nine scans. The figure shows the accuracy scores for the full resolution datasets and their corresponding centroid subsampled point clouds.  </figcaption>
</figure>
</center>

## Visual impression

The overall accuracy results show that the full resolution scans 5 and 7 perform below average. A comparison between the RF-labeled full resolution dataset of scan 5 (Figure 10a) and the ground truth dataset (Figure 10b) shows accurate classification in many areas. However, misclassifications occur mainly at the beginning of the oak trunk and to the left of the pavement, where bushes and low vegetation are present.

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/09_rf_results_visual_scene1.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/09_rf_results_pcd.png" width="90%" height="90%" ></a>
</figure>
</center>

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/10_ground_truth_visual_scene1.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/10_ground_truth_pcd.png" width="90%" height="90%" ></a><figcaption> Figure 10: Visual comparison of the RF classification result (A) and the true labels (B).  </figcaption>
</figure>
</center>

## Feature importance

As mentioned above, a notable advantage of RF classification over other machine learning approaches is the ability to infer the importance of input features. In our RF model, it is evident that the mean height and mean intensity of the segments are key features that significantly influence the model's classification decisions (Figure 11). Within the RGB values, the blue band information appears to have the most significant impact. In general, segment mean values play a more critical role in the RF classifier's decision-making than segment variance values. Among the statistical measures, height and intensity are the most important, while the green and red bands are the least influential.

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/11_rf_feature_importance.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_scanline_LuisKremer/11_rf_feature_importance.png" width="90%" height="90%" ></a><figcaption> Figure 11: Feature importance of the RF model used to classify the points clouds. </figcaption>
</figure>
</center>

# Discussion and conclusion

Overall, our proposed method for classifying TLS point clouds with a random forest classifier is able to achieve promising results. The aim was to condense the amount of data while preserving as much information as possible within the point clouds. This was achieved by a two-step scanline segmentation followed by centroid reduction of these segments. The centroids were assigned 12 attributes for classification. The advantage of this approach is the ability to seamlessly integrate the classification results of the subsampled point clouds back into the raw full resolution point clouds, facilitated by the shared unique IDs between segments and centroids.

Evaluation of the classification accuracy on the full resolution raw point clouds consistently shows values above 90% across all scans. Identified classification errors occur primarily at the beginning of the oak trunk and adjacent to the pavement where low vegetation is present. These errors appear as long, incorrect colored stripes. It is evident that the segment boundaries do not perfectly separate ground from low vegetation and the oak trunk. This behavior is attributed to sub-optimal parameters of the thresholds in the two-step segmentation process. However, defining a universal threshold that accurately segments objects along scanlines in TLS point clouds is challenging. Point density varies significantly depending on the distance of an object from the scanner. Therefore, closer objects require different thresholds than those further away. To address this issue, future improvements could include the implementation of adaptive thresholds. For example, considering the previous 10, 50, or 100 neighbors and comparing the point-to-point differences to the mean difference of these previous neighbors could increase the flexibility of the segmentation. This adaptive approach could mitigate the challenge of erroneous object delineation due to incorrect parameterization.

Further improvements to the proposed method could focus on the features used for random forest classification and their significance. It is evident that mean feature values are of greater value to the classifier than variance values. Consequently, including more mean feature values in the model could improve the classification result. To address this, the computation of features could be extended by including three meaningful attributes that were not explored in this work: slope, curvature, and segment orientation. Segment orientation can be determined by calculating the point normals within a segment. These additional attributes could improve the results by adding structural components specific to elements such as ground, leaves, branches, or trunks. With these considerations, the proposed method could possibly yield even more meaningful outcomes. This could allow in-depth analysis of classified point clouds at full resolution, providing the basis for a comprehensive understanding of vegetation morphology.

# References

Belgiu, M., & Drăguţ, L. (2016). Random forest in remote sensing: A review of applications and future directions. *ISPRS journal of photogrammetry and remote sensing, 114*, 24-31.

Calders, K., Adams, J., Armston, J., Bartholomeus, H., Bauwens, S., Bentley, L. P., ... & Verbeeck, H. (2020). Terrestrial laser scanning in forest ecology: Expanding the horizon. *Remote Sensing of Environment, 251*, 112102.

Hu, Q., Yang, B., Xie, L., Rosa, S., Guo, Y., Wang, Z., ... & Markham, A. (2020). Randla-net: Efficient semantic segmentation of large-scale point clouds. In *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition* (pp. 11108-11117).

Liu, Y., Fan, B., Xiang, S., & Pan, C. (2019). Relation-shape convolutional neural network for point cloud analysis. In *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition* (pp. 8895-8904).

Niemeyer, J., Rottensteiner, F., & Soergel, U. (2014). Contextual classification of lidar data and building object detection in urban areas. *ISPRS journal of photogrammetry and remote sensing, 87*, 152-165.

Su, H., Jampani, V., Sun, D., Maji, S., Kalogerakis, E., Yang, M. H., & Kautz, J. (2018). Splatnet: Sparse lattice networks for point cloud processing. In *Proceedings of the IEEE conference on computer vision and pattern recognition* (pp. 2530-2539).

Thomas, H., Qi, C. R., Deschaud, J. E., Marcotegui, B., Goulette, F., & Guibas, L. J. (2019). Kpconv: Flexible and deformable convolution for point clouds. In *Proceedings of the IEEE/CVF international conference on computer vision* (pp. 6411-6420).

Weinmann, M., Jutzi, B., Hinz, S., & Mallet, C. (2015). Semantic point cloud interpretation based on optimal neighborhoods, relevant features and efficient classifiers. *ISPRS Journal of Photogrammetry and Remote Sensing, 105*, 286-304.
