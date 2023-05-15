---
title: 'Point cloud registration: TLS 3-D model of the Golm campus at the University of Potsdam'
author: "Luis Kremer"
author_profile: true
date: 2023-05-15
permalink: /posts/2023/05/TLS-point-cloud-Golm
toc: true
toc_sticky: true
toc_label: "Point cloud representation of the Golm campus at the University of Potsdam"
header:
  overlay_image: https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_Golm_images/00_Golm_TLS.png
  overlay_filter: 0.3
  caption: "Point cloud representation of the Golm campus at the University of Potsdam"
read_time: false
tags:
  - TLS
  - LiDAR
  - 3-D campus model
  - point cloud registration
  - ICP
---

In the last two decades, Terrestrial Laser Scanning (TLS) has gained increasing importance as a ground-based remote sensing technique for measuring three-dimensional (3-D) spaces using Light Detection and Ranging (lidar). But registering and aligning multiple scans has remained a challenge and this article explores different options for a large (n=222 scan positions) dataset.

# Introduction
In the last two decades, Terrestrial Laser Scanning (TLS) has gained increasing importance as a ground-based remote sensing technique for measuring three-dimensional (3-D) spaces using Light Detection and Ranging (LiDAR). TLS has a wide range of applications, from architecture and engineering to forest inventory for determining biomass, stem volume, or biodiversity (Liang et al., 2016). The fundamental mechanism of many TLS systems is based on measuring the differences in time between the emitted and reflected laser pulses, which usually have wavelengths between 0.5 and 1.5 µm (Pfeifer & Briese, 2007). By using the runtime of a laser pulse, a 3-D representation (x, y, z) of the environment can be generated. Modern scanners are capable of scanning the surroundings with laser pulse repetition rates that exceed 1 MHz, resulting in point clouds that consist of millions of points with millimeter-scale precision.

Unlike airborne laser scanning point clouds, terrestrial laser scanning point clouds consist of individual data acquisitions, which must be merged to obtain full coverage of the study area. However, merging multiple point clouds can be a challenging process that requires precise alignment to avoid errors and ensure features are accurately represented. To prevent misalignment of scans during data acquisition, terrestrial laser scanners are usually equipped with a GNSS antenna for the x, y, and z location of the scanner and an Inertial Measurement Unit (IMU) for measuring the orientation and acceleration of the scanner with respect to the ground (Lillesand et al., 2015). However, this concept is limited when the GNSS signal is weak (e.g., near dense vegetation), the IMU is biased across scans (e.g., due to abrupt movements or long walking distances with the scanner), or the overlap between scans is too small. When these limitations occur together, they can significantly shift the resulting point clouds beyond the limit of the scanner's onboard alignment capabilities. In cases of misalignment after the data acquisition, post-processing steps must be performed to re-align all individual scan positions. To address the alignment issues of point clouds, the Iterative Closest Point (ICP) algorithm has been established in the last three decades (Besl & McKay, 1992; Chen & Medioni, 1992).

In the summer of 2022, we collected TLS data from the entire Golm campus at the University of Potsdam using the RIEGL VZ-400i terrestrial laser scanner. The objective was to create a precise 3-D model of the campus that can be used as a reference for future point cloud comparison work. Due to time constraints and safety reasons, we were unable to use a Differential GNSS base station for signal corrections as it always requires a line-of-sight connection with the scanner. We obtained over 200 individual scans, but a significant number were unaligned and required post-processing. Therefore, our objective for this project was to systematically align these scans to construct a comprehensive 3-D model of the Golm campus. We aim to highlight potential processing challenges and provide insights on how to avoid them. The three research questions that we address in this project are: 1) which methods can be used to systematically align multiple point clouds from terrestrial laser scans; 2) which is the most suitable variant of the ICP algorithm for aligning the scans?; and 3) how does the sampling pattern impact alignment performance?



# Study area
TLS data was collected from the Golm campus at the University of Potsdam from August 22 to August 25, 2022 (Figure 1). A total of 222 scan positions were acquired across the campus, with a balance between short distances to ensure adequate overlap and limiting the number of scans given the large area covered (~0.16 km<sup>2</sup>). The average distance between consecutive scan positions was 33.67 m (Figure 2), although there were variations with a standard deviation of 26.78 m. The large distances (> 75 m) seen in Figure 2 were due to the scanner being relocated to a new position.


<center>
<figure>
<a href="01_ScansPositions.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_Golm_images/01_ScansPositions.png" width="80%" height="80%" ></a><figcaption>Figure 1: Map showing the individual scan positions, with the lines indicating consecutive scans. The lines for the courtyard in the center of the image have been omitted for clarity. </a> </figcaption>
</figure>
</center>


<center>
<figure>
<a href="02_ScanDistances.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_Golm_images/02_ScanDistances.png"></a><figcaption>Figure 2: Barplot showing the scan-to-scan distances. Each bar in the plot represents the distance between two consecutive scans. For example, a bar at position 1 indicates the distance between scan 01 and scan 02. </a> </figcaption>
</figure>
</center>


# Validity of the raw data
To analyze the validity of the more than 200 individual scans acquired in our project, the degree of noise within scans and the consistency of the initial scan alignment across the entire study area were first examined. This information was critical in determining the next steps in data processing, such as noise removal and registration of scans, which will be discussed in more detail in the following chapters.


## Noise
One of the advantages of TLS is that a high density of points can be captured per scan. In our case, around 10 million points per scan were obtained for most of the scans. However, the high point density can also result in the presence of noisy points in the point cloud, which can pose a challenge in data processing and analysis. One of the main causes of noise in our scans was reflection issues caused by windows. Due to the double bounce effect of the laser reflecting off a window and an object back to the scanner, the object (e.g., trees or building facades) is projected behind the window and may be misplaced in the point cloud after merging multiple scans (Figure 3). To avoid problems with the alignment of overlapping point clouds, these noise artifacts had to be removed.


<center>
<figure>
<a href="03_Noise.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_Golm_images/03_Noise.png"></a><figcaption>Figure 3: Merged full resolution scans including noise. The long stripes of points demonstrate the susceptibility of TLS data to window reflections of the laser. In the lower and upper middle parts, reflections are projected onto the street. </a> </figcaption>
</figure>
</center>


## Alignment consistency
Figure 4 shows the bird's eye view of all merged individual point clouds immediately after the data collection and thus the starting point of our 3-D model of the Golm campus. Individual point clouds were preprocessed after the acquisition, including subsampling, tree removal, and noise reduction (see methods for more details). Upon initial inspection of the 3-D visualization, it is evident that building facades are stacked, particularly in the central area of the campus. Even without zooming in, it is apparent that some scans were not accurately positioned or aligned with the scanner's onboard processing platform. This impression is further confirmed by looking at building 27/29 of the campus from a different perspective (Figure 5). Several scans appear to be distorted and protruding into the courtyard.  

<center>
<figure>
<a href="04_RawData_Misalignment.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_Golm_images/04_RawData_Misalignment.png"></a><figcaption>Figure 4: Bird's eye view of all merged individual point clouds after data acquisition. Particularly large errors in the initial alignment are visible in the center of the image (building 27/29). </a> </figcaption>
</figure>
</center>


<center>
<figure>
<a href="05_RawData_Misalignment_Building2729.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_Golm_images/05_RawData_Misalignment_Building2729.png"></a><figcaption>Figure 5: Full resolution data of building 27/29, showing significant misalignment of scans </a> </figcaption>
</figure>
</center>


As seen above, there were several unaligned scans after the data collection, and manually checking for them was tedious. To automate this process, we calculated the cloud-to-cloud distances between each scan and all the other scans. We achieved this by merging all scans and iteratively removing one scan position for analysis. The cloud-to-cloud distance was then calculated and the scan was merged back with the entire point cloud. This process was repeated for each scan position. Figure 6 displays the results of the cloud-to-cloud distance analysis. The upper plot illustrates the minimum distance for each point in each of the 222 scans to the closest neighboring point in another scan. The lower plot presents the median cloud-to-cloud distance for each scan, taking all points into account.

The upper plot in Figure 6 should ideally show bright pixels along the x-axis, meaning that each point has a close neighbor point in another scan. This is the first indication of good alignment between scans, although it does not guarantee perfect alignment of the entire 3-D model as scans can be systematically shifted. The ground plot should have median cloud-to-cloud distances close to zero. However, large gaps with dark values in the upper plot and bars sticking out in the lower plot (e.g., scan ID 110-118) can be observed, and are indicative of misaligned scans. Setting an arbitrary threshold of 10 cm for cloud-to-cloud misalignment would identify 38 out of 222 scans as misaligned (red dots in Figure 6), while a threshold of 5 cm would already identify 99 unaligned scans.


<center>
<figure>
<a href="06_RawData_cloudtocloud_distance.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_Golm_images/06_RawData_cloudtocloud_distance.png"></a><figcaption>Figure 6: The upper plot displays the minimum distance between every point in the 222 scans and its closest neighbor in any other scan. The distance values of the points are binned and represented by dark color (few points) and bright color (many points at that distance). The lower plot shows the median cloud-to-cloud distance for each scan, which is calculated by taking the minimum distances of all points in a scan and calculating the median value. </a> </figcaption>
</figure>
</center>


Visual inspection and cloud-to-cloud distance analysis indicate that the source data are unsuitable for direct use. To create a 3-D model of the Golm campus, individual alignment of the scans was required. The next chapter addresses this topic in detail, followed by the methods used for alignment.


# Point cloud registration
As each scan in a TLS campaign has its local coordinate system, accurate registration methods are necessary to create a homogeneous data set in the same coordinate system with seamless overlapping areas of point clouds (Grant et al., 2013). During the registration, algorithms seek a suitable transformation that minimizes the distance between two overlapping point clouds. The output of the registration algorithm is a transformation matrix that represents operations such as translation, rotation, and scaling of the point cloud coordinates.

Significant advances have been made in the development of registration algorithms, and a general workflow consisting of coarse global registration of scans, followed by local refinement, has been established (Zhou et al., 2016). As coarse and fine registration form the fundamental building blocks of this project, an explanation of both concepts will be provided in the following section.


## Global registration
Prior to fine registration, global registration is performed, which does not require pre-alignment of point clouds. Several algorithms are available for global registration, of which RANSAC (Random Sample Consensus) is a widely used method (Zhou et al., 2016). The RANSAC algorithm is an iterative process that randomly selects a user-defined number of points in one point cloud and searches for their correspondence in the other point cloud. The transformation is estimated and evaluated based on criteria such as the distance correspondence between the two point clouds (Dung et al., 2013). This process is repeated until convergence. The search for correspondence in the point cloud that needs to be aligned (source point cloud) can require a significant number of iterations. To accelerate this process, Fast Point Feature Histograms (FPFH) are calculated (Rusu et al., 2009). FPFH describe the local geometry of a point and its neighboring points. This descriptor enables the RANSAC algorithm to search for nearest neighbors based on the FPFH, thus speeding up the correspondence search. This global registration method is implemented in the Python package `Open3D`.

Besides the automatic global registration mentioned above, global registration can also be performed manually using software such as `CloudCompare`. User can select a set of matching points (at least three) in both the target (reference) and source point clouds. Based on this correspondence, the transformation of the source point cloud is calculated.


## ICP registration

Unlike global alignment, fine registration methods require two point clouds that already have a rough correspondence. The Iterative Closest Point (ICP) algorithm is commonly used for local refinement and has two main variants:


**Point-to-point ICP**

The Iterative Closest Point (ICP) registration method using the point-to-point variant was introduced by Besl and McKay (1992). This iterative algorithm consists of two stages in each iteration:

- First, for each point in the source point cloud, it searches for the closest point in the target point cloud.
- Second, it attempts to find a transformation that minimizes the distance between the corresponding points.

These two processing stages are repeated until convergence (Salvi et al., 2007).


**Point-to-plane ICP**

The point-to-plane variant of the ICP algorithm takes into account that scanned objects are not individual points, but surfaces. Unlike point-to-point, which tries to minimize the distance between individual points, the point-to-plane method assumes that points in the source point cloud are generally on a surface of the target point cloud. This accounts for the fact that the source and target point clouds are not necessarily identical.

The general processing procedure of the point-to-plane method is similar to that of the point-to-point approach. However, instead of searching for the closest points between the source and target point clouds, the method calculates the intersection of the point normal in the source point cloud with the tangent plane at its corresponding point in the target point cloud. Then, the algorithm attempts to find a transformation that minimizes the distance between points and the tangent planes at its correspondence points (Low, 2004). This process is repeated until convergence.

Pulli (1999) emphasize the advantages of the point-to-plane method compared to the point-to-point method. Some of the arguments and findings are:

- The point-to-plane method converges an order of magnitude faster than the point-to-point method.
- The point-to-point method typically requires at least ten times more point matching and alignment iterations than the point-to-plane method.
- The point-to-plane method is not significantly slowed down by false point pairs since each point can slide along the tangent plane of its corresponding point.


# Methods
Due to alignment issues during acquisition, as indicated in the section "alignment consistency" it was not possible to directly merge the raw point clouds from each scan to obtain a 3-D model of the Golm campus. To address the research questions, different alignment approaches and algorithms were applied. Analysis steps, necessary data pre-processing, and evaluation metrics of the results are described below.


## Analysis
Since fine registration requires pre-aligned point clouds, the scans with a median cloud-to-cloud distance of more than 10 cm were removed (a total of 38 scans; see Figure 6). The RANSAC global registration approach and manual point pair selection were then applied to roughly align the 38 excluded ones to the remaining scans. Two separate alignment approaches were subsequently performed using both variants of the ICP algorithm.

1. For the first approach, a `loop closure method` was implemented by starting with the first scan and aligning the second scan to the first scan. The aligned scans were merged, and the iterative process was continued by moving on to the next scan until all 222 scans were aligned and merged. To ensure a systematic approach, scans were aligned in a serpentine pattern, starting in the eastern part of the campus and continuing until the first loop was closed in the western part. Subsequently, all other scans between this serpentine pattern were aligned to the framework of the first aligned scans, resulting in the closure of the loop several times. This approach was repeated for both point-to-point and point-to-plane variants of ICP to compare their performance.

2. In the second approach, an airborne laser scanning (ALS) dataset of the campus was used as the target point cloud, and each TLS scan was aligned as the source point cloud to it. This approach was repeated for both variants of the ICP algorithm (point-to-point and point-to-plane) to compare whether a different target point cloud affected the result.

The analyses were performed using Python 3.9, utilizing two primary packages: `laspy` for reading and writing .laz files, and `open3d` for implementing the ICP algorithms. The software `CloudCompare` was used for manual global registration.



## Data preparation

Each TLS scan consists of about 10 million data points. Processing such a large amount of data has a significant impact on the computation time. Therefore, each scan was subject to the following pre-processing steps prior to analysis:


**1. Subsampling to 10 centimeters**

The subsampling of the point clouds was performed using a voxel-grid filter. This approach assigns a 3-D grid of 10 cm spacing voxels to the point cloud, and samples only the closest point to the center of each voxel. This reduces the amount of data and evens out varying point density.


**2. Outlier filter**

A statistical filter was applied to identify outliers in the point cloud. For each point, the mean distance to its `n` nearest neighbors was computed, and the overall standard deviation was determined. Points were classified as outliers if the mean distance to their `n` nearest neighbors exceeded the distance threshold of `m` multiplied by the overall standard deviation. For this analysis `n` was set to 12, and `m` to 3.

Additionally, significant noise artifacts (Figure 3) that remained after the statistical outlier filter were manually removed.


**3. Remove non-planar features**

The Golm campus contains both planar objects such as building facades and streets, and non-planar objects like trees. Trees can have slightly varying shapes across scans due to the motion of the leaves, which potentially affects the accuracy of the ICP alignment. To mitigate this issue, non-planar objects were filtered out for the analysis by exploiting the calculation of geometric features. Geometric features, such as `planarity`, describe the shape of a point based on its local neighborhood. For example, a point in a tree crown would have a low `planarity` value, while a point on a street would have a high value.

The computation of the geometric feature `planarity` can be summarized as described by Dittrich et al. (2017):

1. The 3D covariance matrix based on the point's neighborhood is calculated using a fixed radius (e.g., 1 m)
2. The eigenvectors ($$e_{1}$$, $$e_{2}$$, $$e_{3}$$) and eigenvalues ($$\lambda_{1}$$, $$\lambda_{2}$$, $$\lambda_{3}$$) of the 3D covariance matrix are calculated
3. `Planarity` is determined considering the three eigenvalues ($$\lambda_{1}$$, $$\lambda_{2}$$, $$\lambda_{3}$$): on a planar surface eigenvalues $$\lambda_{1}$$ and $$\lambda_{2}$$ are larger than $$\lambda_{3}$$. Therefore, `planarity` ($$P_{\lambda}$$) is calculated based on the following ratio:
$$  P_{\lambda} = \frac{\lambda_{2} - \lambda_{3}}{\lambda_{1}}$$

For the analysis, a `planarity` threshold of 0.7 was selected. The value was arbitrarily chosen but led to reasonable filtering results as shown in Figure 7. As an example, Figure 7a displays the original point cloud data, while Figure 7b shows the results of the data after the data preparation stages.


<center>
<figure>
<a href="07_TLS_processing_before_after.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_Golm_images/07_TLS_processing_before_after.png"></a><figcaption>Figure 7: Example of data preparation. Figure A displays the original point cloud data with all features included, while Figure B shows the subsampled and non-planarity filtered point cloud data. </a> </figcaption>
</figure>
</center>



## Evaluation metrics
Three metrics were used in this project to evaluate the quality of the alignment for both ICP variants and alignment methods.


**Surface roughness**

Surface roughness was utilized for visual inspection rather than quantitative measurement. Surface roughness is calculated as the distance between a point and the best-fitting plane determined by its nearest neighbors. If the scans overlap perfectly on a smooth surface, such as a road, the surface roughness is minimal. Conversely, the surface roughness values increase as the alignment deteriorates.


**Median cloud-to-cloud distance**

The median cloud-to-cloud distance was determined by merging all scans and then removing one scan position at a time for analysis. For each point in the removed scan, the distance to its nearest neighbor in the remaining scans was calculated. The median distance was calculated using all the distances. The removed scan was then merged back, and the same procedure was repeated for the next scan position. The median cloud-to-cloud distance is less affected by outliers in the point clouds.


**dRMS**

A slightly modified version of the dRMS used by Li et al. (2020) was utilized to give more weight to the misaligned and outlier points. The dRMS provides a measure of the average distance between corresponding points in two aligned point clouds. The smaller the dRMS, the higher the accuracy of the alignment. For a source point cloud A and a target (reference) point cloud B, the dRMS can be expressed as:


$$ dRMS(A,B)=\sqrt{\frac{1}{n}\sum_{i=1}^{n}\left ( \left \| a_{i}-b_{j} \right \| \right )^2} $$

where:

- $$a_{i}$$ is the point in the source point cloud corresponding to $$b_{j}$$ in the target point cloud $$n$$ the number of points in $$A$$



# Results
## Global alignment
The automated approach using the RANSAC algorithm supported by FPFH was initially attempted for alignment but was later discarded due to significant runtime issues and the inability to achieve convergence. Especially in the part of Figure 5, the algorithm was not able to come up with a satisfactory solution for the fine registration. Therefore, the manual approach was applied, which involved selecting corresponding point pairs in the target and source point clouds, resulting in successful alignment, as shown in Figure 8. However, some parts of the campus were still misaligned, indicated by sudden changes in surface roughness (Figure 8).


<center>
<figure>
<a href="08_Building2729_surfaceroughness.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_Golm_images/08_Building2729_surfaceroughness.png"></a><figcaption>Figure 8: Building 27/29 after global alignment, showing well-represented building walls. However, surface roughness exceeding 20 cm (yellow areas) reveals misalignment of scans in the z-direction.   </a> </figcaption>
</figure>
</center>


## Fine registration

**Loop closure approach**

Overall, the point-to-point ICP variant using the loop closure approach achieved a good alignment result. Figure 9a indicates that only three scans remained above the 10 centimeter threshold for the median cloud-to-cloud distance threshold. Additionally, after visual inspection using surface roughness, it was observed that two of these scans were not misaligned but rather had poor overlap, resulting in an overall increase in cloud-to-cloud distance. Therefore, almost all scans were correctly aligned using this method, with a majority having below 5 cm cloud-to-cloud distance.

On the other hand, the point-to-plane ICP variant's alignment performance was overall poor, with 87 scans having a cloud-to-cloud distance of more than 10 centimeters (Figure 9b). This method even deteriorated the initial alignment of the raw data (Figure 6).


<center>
<figure>
<a href="09_LoopClosure_Barplot.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_Golm_images/09_LoopClosure_Barplot.png"></a><figcaption>Figure 9: Comparison of results of the loop closure approach: (A) Point-to-point variant leads to an overall good alignment result. The bars sticking out are aligned scans, however, with poor overlap and thus increased value; (B) In contrast, the point-to-plane variant showed significant misalignment for many scans, with over 80 scans having a median cloud-to-cloud distance greater than 10 cm. </a> </figcaption>
</figure>
</center>



**ALS reference approach**

In the case of using the ALS data set as the reference point cloud, the point-to-point ICP variant had a slightly worse alignment performance compared to the loop closure approach, as depicted in Figure 10a. Despite this, the point-to-point approach still resulted in an improvement over the alignment of the raw data, with 18 scans having a median cloud-to-cloud distance greater than 10 centimeters. The scans displayed good alignment agreement along the z-direction but showed deficient alignment in the x- and y-directions, particularly along building walls.

The point-to-plane ICP variant performed better compared to the loop closure approach, with 28 scans exhibiting a median cloud-to-cloud distance greater than 10 centimeters (Figure 10b). However, the point-to-plane variant still underperformed in comparison to the point-to-point variant.


<center>
<figure>
<a href="10_ALSReference_Barplot.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_Golm_images/10_ALSReference_Barplot.png"></a><figcaption>Figure 10: Comparison of results of the ALS reference approach: (A) Point-to-point variant shows misalignment only for individual scans, particularly scan 180-200 where building walls are poorly represented; (B) Point-to-plane variant shows misalignment for more scans, with five scans having a median cloud-to-cloud distance greater than 1 m. </a> </figcaption>
</figure>
</center>



**Overall performance and final 3-D model**

The overall performance of the two ICP variants and the two alignment approaches are shown in the table below. The evaluation metrics, including the dRMS and median cloud-to-cloud distance, suggest that the point-to-point ICP variant using the loop closure approach performed best in this analysis. Additionally, the point-to-point ALS reference approach also demonstrated reasonable results. Conversely, the point-to-plane variant performed worse in both metrics, indicating that it negatively impacted the alignment of the raw data.


| Method                        |dRMS         | Median cloud-to-cloud distance |
|-------------------------------|-------------|--------------------------------|
| Raw data                      | 0.633       | 0.157                          |
| Loop closure: Point-to-Point  | **0.433**   | **0.038**                      |
| Loop closure: Point-to-Plane  | 0.767       | 0.207                          |
| ALS reference: Point-to-Point | 0.434       | 0.059                          |
| ALS reference: Point-to-Plane | 0.859       | 0.460                          |


The final 3-D model of the Golm campus was created using the registered data from the best alignment result achieved through the point-to-point loop closure approach (Figure 11).

<center>
<figure>
<a href="11_final_viz_golm.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_Golm_images/11_final_viz_golm.png"></a><figcaption>Figure 11: Final 3-D model of the Golm campus at the University of Potsdam </a> </figcaption>
</figure>
</center>



# Discussion and conclusion
## Loop closure vs. ALS reference approach

The loop closure approach has been shown to achieve accurate results in the x- and y-directions but reveals issues in the z-direction. This can be attributed to slight alignment errors that propagate through the point cloud. These errors become evident when closing the loops and are even larger when the overlap between the scans is not given.

On the other hand, the ALS reference approach performs well in the z-direction due to the high overlap of ALS and TLS point clouds. However, this method shows lower accuracy in the x- and y-directions, which is likely due to the fact that the ALS dataset does not sufficiently represent the facades of the buildings.

For future work, a combination of the loop closure and ALS reference approaches could be beneficial to improve the overall alignment. The loop closure approach could be used first to align the point clouds in the x- and y-directions, followed by the ALS approach to refine the alignment only in the z-direction.


## Point-to-point vs. point-to-plane ICP
Given the conditions of this project, the point-to-point ICP algorithm outperformed the point-to-plane ICP algorithm and resulted in an overall improvement of the registered data compared to the raw data. Considering the significant number of scans that were misaligned after the data acquisition, the point-to-point algorithm was able to refine the registration with an accuracy of centimeters to millimeters. The removal of non-planar and slightly moving features, such as leaves or branches, proved to be beneficial for the algorithm. This is because the point-to-point variant of the ICP algorithm aims to find identical points in two different point clouds, making it more effective to use only man-made features that are consistent across the scans.

While the point-to-point variant yielded superior results, the point-to-plane variant underperformed and even deteriorated the raw data alignment. This result was unexpected given that the point-to-plane variant is commonly regarded as more realistic due to the challenge of identifying identical points in two distinct point clouds. The inaccurate outcomes of the point-to-plane algorithm can be attributed to two main factors:

1. Restricting the point clouds to planar surfaces was effective for the point-to-point variant but may not have been optimal for the point-to-plane variant. The campus environment, consisting of buildings with large walls lacking distinctive features, posed a challenge for the point-to-plane variant. As a result, the algorithm had difficulty in finding matching features, resulting in the slipping of two large walls.

2. The algorithm randomly oriented the point normals of the point clouds. Figure 12 shows an example of a point cloud with three walls and their corresponding point normals. Ideally, all point normals should face the direction of the scanner. However, since the scanner's location was not specified, the point normals were randomly oriented in both possible directions. Consequently, the algorithm projected the point normals onto the planes of non-corresponding points, causing significant shifts in the x- and y-directions, as observed in our analysis.


<center>
<figure>
<a href="12_Normal_orientation.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_Golm_images/12_Normal_orientation.png"></a><figcaption>Figure 12: Figure A is showing a point cloud with three walls and their computed normals in Figure B </a> </figcaption>
</figure>
</center>


## Impact of the TLS sampling pattern on alignment performance
The RIEGL VZ-400i and other similar scanners are equipped with onboard alignment capabilities, which can eliminate the need for post-processing alignment if a suitable sampling pattern is employed. However, as mentioned in the introduction, the scanner's alignment capabilities are limited when either the GNSS or IMU system is not performing as expected, often due to factors such as weak signal strength, large distances between scans, or the absence of re-initialization at the last scan position after the scanner is turned off. The combined effect of these factors can lead to the alignment issues encountered after the data acquisition in this project.

While this project demonstrated that misalignment issues in a large data set with over 200 scans can be resolved through global alignment and refined alignment using ICP, these processing steps can be avoided or simplified with consistent TLS sampling. Two crucial aspects to consider are short distances (10-20 m) between scans and a consistent sampling pattern in which each scan has a follow-up scan and no location is scanned more than once. Short distance ensures adequate overlap of point clouds from different scans, enabling matching of the same objects during alignment. A consistent scan pattern is essential for proper alignment of subsequent scans, as jumping back and forth between scans can disrupt onboard alignment and potentially lead to misalignment. Keeping these considerations in mind when conducting TLS scanning can help streamline the alignment process and ensure obtaining an accurate 3-D model.



# Important takeaways of the TLS project
- A consistent TLS sampling pattern with each scan having at least two close-by neighboring scans should be followed to ensure reliable on-board registration for the RIEGL VZ-400i scanner
- Short distances (10-20 m) between scans to provide enough overlap can facilitate point cloud registration tasks
- The combination of global and fine registration through the ICP algorithm is able of addressing large misalignments even between scans with little overlap
- The performance of the point-to-point ICP variant benefits from removing non-planar features as handling slightly moving objects across the scans can be challenging
- The implementation of the point-to-plane ICP variant requires careful consideration (e.g., properly oriented point normals) but has the potential to further improve the results of this project
- The combination of the loop-closure approach using TLS scans for x and y alignment and ALS data for z alignment shows promise for the large area covered in this project



# References

Besl, P. J., & McKay, N. D. (1992). Method for registration of 3-d shapes. Sensor fusion IV: control paradigms and data structures, 1611, 586–606.

Dittrich, A., Weinmann, M., & Hinz, S. (2017). Analytical and numerical investigations on the accuracy and robustness of geometric features extracted from 3d point cloud data. ISPRS journal of photogrammetry and remote sensing, 126, 195–208.

Dung, L. -R., Huang, C.-M., Wu, Y. -Y., et al. (2013). Implementation of ransac algorithm for feature-based image registration. J. Comput. Commun, 1(6), 46–50.

Grant, D., Bethel, J., & Crawford, M. (2013). Comparative study of two automatic registration algorithms. ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Information Sciences, 2, 91–95.

Li, P., Wang, R., Wang, Y., & Tao, W. (2020). Evaluation of the icp algorithm in 3d point cloud registration. IEEE Access, 8, 68030–68048.

Liang, X., Kankare, V., Hyyppä, J., Wang, Y., Kukko, A., Haggrén, H., Yu, X., Kaartinen,
H., Jaakkola, A., Guan, F., et al. (2016). Terrestrial laser scanning in forest
inventories. ISPRS Journal of Photogrammetry and Remote Sensing, 115, 63–77.

Lillesand, T., Kiefer, R. W., & Chipman, J. (2015). Remote sensing and image interpretation. John Wiley & Sons.

Low, K.-L. (2004). Linear least-squares optimization for point-to-plane icp surface registration. Chapel Hill, University of North Carolina, 4(10), 1–3.

Pfeifer, N., & Briese, C. (2007). Geometrical aspects of airborne laser scanning and ter-
restrial laser scanning. International Archives of Photogrammetry, Remote Sensing
and Spatial Information Sciences, 36(3/W52), 311–319.

Pulli, K. (1999). Multiview registration for large data sets. Second international conference on 3-d digital imaging and modeling (cat. no. pr00062), 160–168.

Rusu, R. B., Blodow, N., & Beetz, M. (2009). Fast point feature histograms (fpfh) for 3d registration. 2009 IEEE international conference on robotics and automation, 3212–3217.

Salvi, J., Matabosch, C., Fofi, D., & Forest, J. (2007). A review of recent range image registration methods with accuracy evaluation. Image and Vision computing, 25(5), 578–596.

Zhou, Q. -Y., Park, J., & Koltun, V. (2016). Fast global registration. Computer Vision–ECCV 2016: 14th European Conference, Amsterdam, The Netherlands, October 11-14, 2016, Proceedings, Part II 14, 766–782.
