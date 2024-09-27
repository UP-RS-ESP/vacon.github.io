---
title: "Apple segmentation in 3D point clouds"
author: "David Hersh"
author_profile: true
date: 2024-09-27
permalink:
toc: true
toc_sticky: true
toc_label: "Terrestrial laser scanning"
header:
  overlay_image: https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/DavidHersh_Apples/gt_halftree.png
  overlay_filter: 0.3
  caption: "Ground truth labels for half of the apple tree"
read_time: false
tags:
  - Terrestrial laser scanning
  - LiDAR
  - Point Clouds
  - segmentation
---

# Introduction

Detection of fruit in 3D point clouds can help aid in crop yield prediction and can be acheived through clustering and segmentation as shown by Mola et al., 2020. Li et al., 2022 used a deep learning approach to generate bounding boxes around apples and RANSAC to determine the centroid for robotic harvesting. This internship aimed at segmenting apples with simple clustering approach and a deep learning approach.

_This internship was supervised by Prof. Dr. Bodo Bookhagen_

# Scanning and Pre-processing

The study site was the Streuobstwiese Golm located Northeast of the Golm campus, which has a few dozen apple and pear trees.

<figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/DavidHersh_Apples/study_location.png"><img align="right" width="800" src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/DavidHersh_Apples/study_location.png"></a>
 <figcaption> Figure 1. Location of the orchard near campus Golm.</a>  </figcaption>
    </figure>

The scans were taken of a single tree from approximately 12 perspectives. The scanner used was a Zoller+Froelich IMAGER® 5016A, which includes RGB and intensity information. Sphere control points from Zoller and Froelich were placed around the base of the tree along with paper targets to aid in the registration process.

<figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/DavidHersh_Apples/apple_site.jpg"><img align="right" width="800" src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/DavidHersh_Apples/apple_site.jpg"></a>
 <figcaption> Figure 2. Study site with registration targets.</a>  </figcaption>
    </figure>

The scans were then registered using the Z+F LaserControl® software. The software uses the sphere control points and paper targets to align the scans. The software also has a feature to remove noise from the point cloud. The final point cloud was then exported as a LAS file.

<figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/DavidHersh_Apples/registration.png?raw=True"><img width="800" src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/DavidHersh_Apples/registration.png"></a>
 <figcaption>Figure 3. Automated removal during scanning of unreliable points based on pulse return shape. </a>  </figcaption>
    </figure>

The final point cloud was clipped to remove ground points. Due to sunny conditions during scanning, some points, epecially on the top of the tree, had a purple hue (See figure 3).

<figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/DavidHersh_Apples/appletree.png"><img width="800" src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/DavidHersh_Apples/appletree.png"></a>
 <figcaption>Figure 4. Final point cloud after registrations and clipping. </a>  </figcaption>
    </figure>

# Segmentation

Two general approaches to segmentation were tested. The first was using a combination of DBSCAN and RANSAC. The second was using a deep learning approach using KPConv.

## DBSCAN and RANSAC

Using _Density Based Spatial Clustering of Applications with Noise_ (DBSCAN) and _Random Sampling and Consensus_ (RANSAC) was chosen as a first approach due to the simplicity and the ability to easily use RANSAC to fit spheres to each apple. The main goal was to create clusters ideally with only a single apple. Then, using RANSAC, a sphere was fit to each cluster and the root mean squared error (RMSE) was calculated to find the best fitting sphere from the RANSAC iterations.

DBSCAN was implemented using the sklearn library using an $\epsilon$ value of 0.25 and a minimum of 100 points using a ball radius with sklearn. The $\epsilon$ value was tested with multiple values as this determines the maximum distance between two neighbors to be part of the same cluster (Sander et al., 1998).

<figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/DavidHersh_Apples/dbscan.png"><img width="800" src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/DavidHersh_Apples/dbscan.png"></a>
 <figcaption>Figure 5. DBSCAN clusters often include only one apple, but often a much larger area if a larger epsilon value was used.</a>  </figcaption>
    </figure>

Then, for each cluster a sample of 4 random points are chosen and a sphere is fit using Random Sampling and Consensus. The parameters for the RANSAC algorithm require some adjustments to match the density of the dataset, which could not be downsampled without losing significant detail. The chosen parameters were:

- 10,000 iterations per cluster
- Radius threshold of 0.03 meters (eg. if sphere from the 4 chosen points does not have a radius under 0.03 meters, then skip this iteration)
- A threshhold for inliers of 0.01 meters

At each RANSAC iteration on a cluster, the Root Mean Squared Error is calculated as:

$$
\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (d_i - r)^2}
$$

- $n$ is the number of inlier points (points close to the sphere's surface)
- $d_i$ is the Euclidean distance of the $i$-th point from the sphere's center
- $r$ is the radius of the fitted sphere

The final inlier points were chosen by the lowest RMSE where more that 150 points were inliers and the results saved to a PLY file as a new class. Lastly, the output is compared to a ground truth point cloud and evaluated using the following metrics:

$$
\text{Precision} = \frac{TP}{TP + FP}
$$

$$
\text{Recall} = \frac{TP}{TP+FN}
$$

$$
\text{F1} = 2 * \frac{Precision * Recall}{Precision + Recall}
$$

After trying DBSCAN and RANSAC with different combinations of values, the above parameters yielded the following scores:

| Metric    | Score |
| --------- | ----- |
| Precision | 0.22  |
| Recall    | 0.41  |
| F1        | 0.28  |

<figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/DavidHersh_Apples/gt_vs_dbscanransac.png"><img width="800" src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/DavidHersh_Apples/gt_vs_dbscanransac.png"></a>
 <figcaption>Figure 6. Ground truth (left) compared with DBSCAN+RANSAC results (right). </a>  </figcaption>
    </figure>


Overall, the approach of using RANSAC and DBSCAN had a few significant drawbacks:

- There were multiple parameters that required experimentation
- Even for this relatively small point cloud, the process was slow due to having to iterate over many clusters

## Deep learning approach using KPConv

An alternative approach using deep learning was explored. _Kernel Point Convolutions_ (KPConv) was introduced by Thomas et al., 2019 and uses "Kernel Points" in a fashion analogous to Convolutional Neural Networks (CNN) and applies convolutions based on the relative position of points determined by a correlation coefficient as a way to avoid discretization into voxels or grids.

<figure>
  <a 
href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/DavidHersh_Apples/kpconv.png?raw=True"><img width="1000" src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/DavidHersh_Apples/kpconv.png"></a>
 <figcaption>Figure 7. Image convolution (left) and kernel convolution (right). Figure from Thomas et al., 2019. </a>  </figcaption>
    </figure>

For the apple tree, KPConv was tested on half of the tree with ground truth labels of:

0. Branch
1. Apple

This approach utilized a fork of the [PyTorch KPConv repository](https://github.com/HuguesTHOMAS/KPConv-PyTorch) and used a copy of the SenSatUrban dataset as a template and updating the class weights to reflect the apple tree dataset for calculating loss. The dataset was split into 5 parts, using 3 for training and 2 for validation and testing. KPConv can take additional features in additional to x,y,z coordinates, and included here was RGB. Kernel points can either be "rigid" where they are initialized in fixed positions, or "deformable" where they can adapt to the local geometry (Thomas et al., 2019). The deformable kernel points were used in this case.

The model training was done over 200 epochs using 12 kernel points and 5 cm kernel radius and without subsampling the original point cloud as it was sparse and KPConv does not require spatially uniform points. Training required around 3 hours on an NVIDIA Quadro M2200 GPU.

The results of KPConv were evaluated using Intersection over Union (IoU). The mean IoU for the full cloud was:

| Class  | IoU   |
| ------ | ----- |
| Branch | 98.78 |
| Apple  | 59.12 |
| Mean   | 78.95 |

Compared with the more manual approach of DBSCAN and RANSAC, KPConv shows a significant improvement.

<figure>
  <a 
href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/DavidHersh_Apples/gt_vs_pred.png?raw=True"><img width="1000" src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/DavidHersh_Apples/gt_vs_pred.png"></a>
 <figcaption>Figure 8. Comparison of ground truth (left) and prediction (right). Areas of significant misclassification are circled. </a>  </figcaption>
    </figure>

# Conclusion

The more simple approach of DBSCAN and RANSAC was difficult to apply due to the varying point cloud densities and multiple parameters that required tuning. This approach also does not scale well, but could have been sped up by initializing the 4 RANSAC points using a randomly initialized point and 3 nearest neighbors from a KD tree rather than being randomly initialized from a cluster. In comparison, the approach using KPConv yielded good results and could have been improved by adding additional input features, especially intensity. This approach generated a point-wise classification for the entire point cloud, so a final pass over the apple class in the point cloud using RANSAC similar to Li et al., 2022 could be used to generate final instance segmentations.

# References

Gené-Mola, J., Gregorio, E., Cheein, F. A., Guevara, J., Llorens, J., Sanz-Cortiella, R., Escolà, A., & Rosell-Polo, J. R. (2020). Fruit detection, yield prediction and canopy geometric characterization using LiDAR with forced air flow. Computers and Electronics in Agriculture, 168, 105121. https://doi.org/10.1016/j.compag.2019.105121

Sander, J., Ester, M., Kriegel, H., & Xu, X. (1998). A Density-Based algorithm for discovering clusters in large spatial databases with noise. Data Mining and Knowledge Discovery, 2(2), 169–194. https://doi.org/10.1023/a:1009745219419

Thomas, H., Qi, C. R., Deschaud, J., Marcotegui, B., Goulette, F., & Guibas, L. J. (2019, April 18). KPCONV: Flexible and Deformable Convolution for Point Clouds. arXiv.org. https://arxiv.org/abs/1904.08889

Li, T., Feng, Q., Qiu, Q., Xie, F., & Zhao, C. (2022). Occluded Apple Fruit Detection and Localization with a Frustum-Based Point-Cloud-Processing Approach for Robotic Harvesting. Remote Sensing, 14(3), 482. https://doi.org/10.3390/rs14030482
