---
title: 'Generation of high-resolution digital topography of a rugged anticline using SPOT-6 satellite images and the NASA Ames Stereo Pipeline'
author: "Ananya Pandey"
author_profile: true
date: 2024-03-05
permalink: 
toc: true
toc_sticky: true
toc_label: "Generation of high-resolution digital topography of a rugged anticline using SPOT-6 satellite images and the NASA Ames Stereo Pipeline"
header:
  overlay_image: https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_3.png 
  overlay_filter: 0.3
  caption: "Rugged Anticline in the arid intermontane Calchaquí Valley, Eastern Cordillera, NW Argentina"
read_time: false
tags:
  - digital topography
  - SPOT-6
  - stereophotogrammetry
  - NASA Ames Stereo Pipeline
  - Calchaquí Valley
---

Regional-scale Earth surface process analyses require cost-effective, large-area coverage, high-resolution digital elevation models (DEMs). Stereogrammetry, employing optical data from two or more overlapping images, emerges as a viable method for generating 3D topography in areas with sparse vegetation cover. 


# Introduction

Digital elevation models (DEMs) are crucial for analyzing the geomorphic processes shaping landscapes. Investigating such processes in regions characterized by both active tectonics and climate sensitivity provides valuable insights into associated hazards. This work focuses on the arid intermontane Calchaquí valley of the Eastern Cordillera of the NW Argentinian Andes, a region undergoing active deformation and highly sensitive to climatic forces. The area witnesses significant discharge events during the South American Monsoon season, resulting in heavy rainfall and flooding. Its predominantly dry, sparsely vegetated land is vulnerable to extreme discharge events. Hence, topographic analyses of this area are of relevance. 

While freely available DEMs often lack the resolution to reveal intricate topographic details, high-resolution lidar-derived DEMs are costly and practical only for small-scale evaluations. For regional-scale assessments, stereogrammetry provides a cost-effective, high-resolution option for generating digital topography (Shean et al., 2019). Stereogrammetry generates three-dimensional (3D) models of objects or landscapes with the help of two or more overlapping pairs of photographs taken from different viewpoints. 

This study uses the SPOT 6 (Satellite pour l'Observation de la Terre) images to generate a high-resolution (3m) DEM. The DEM is created with the help of the NASA Ames Stereo Pipeline, a collection of freely available and open-source automated tools for geodesy and stereogrammetry (Beyer et al., 2018). This DEM serves for studying actively deforming structures in an intra-continental setting in NW Argentinian Andes. Additionally, multiple DEMs generated using different algorithms and parameters have been compared to analyze their accuracy. 

*This internship was supervised by Prof. Dr. Bodo Bookhagen.*

# Study Region

The fault-bounded intermontane Calchaquí valley lies in the southeastern part of the Eastern Cordillera of the NW Argentinian Andes. The area is part of the Andean foreland and falls in the Salta Province, near the city of Cachi. The ongoing Andean orogenic deformation has led to the formation of inverted structures in the Andean foreland of NW Argentina (Strecker et al., 2012). This has resulted in thick-skinned deformation and recent seismicity. The reactivation of lower Paleozoic and Cretaceous basement structures has formed basement-cored mountain ranges with partially connected depocenters (Carrera et al., 2006).  

The DEM created in this work is of an anticlinal feature in the Calchaquí valley, presumably formed over a blind thrust fault, due to the reactivation of the basement structure. The DEM serves as a basis for studying how these structures form and evolve by looking into the behavior of river networks and the deformation of fluvial terraces. This can also be used for hazard studies such as debris flows and landslides.

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_1.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_1.png" width="90%" height="90%" ></a><figcaption> Figure 1: Map of the study area. (A) Map showing the location of the anticline and the surrounding regions in the continent of South America. (B) Map showing the proximity of the study area to the city of Salta in Argentina. (C) The zoomed-in view of the area of investigation - the yellow box highlights the anticline under study. </figcaption>
</figure>
</center>

# Data

- Panchromatic tri-stereo SPOT 6 satellite imagery at a resolution of 1.5m of a growing anticline in the Calchaquí valley  
- Copernicus 30m DEM 

# Methods

The work is divided into two sections. The first section discusses the basic steps involved in DEM generation using the Ames Stereo Pipeline (ASP). In the second, comparative analyses on DEMs created using different algorithms and parameters have been performed.

## Part 1: DEM Generation

A high-resolution DEM can be generated using ASP by analyzing stereo images taken from different viewpoints. These images captured from slightly different angles help to create depth perception and reconstruct the spatial structure of the observed terrain. ASP provides a range of stereo-matching algorithms and predefined parameters designed for creating a DEM. Some of the tools that ASP offers for DEM generation are described below.

### Bundle Adjustment

  Error in satellite position and orientation can affect the accuracy of a DEM created using ASP. These errors can be corrected using a pre-processing step called bundle adjustment. Bundle adjustment helps 
  minimize the error between the estimated pixel locations of 3D objects and their actual positions in the captured images -  ensuring consistency among observations of a single ground feature across multiple 
  images.
  
### Stereo Correlation

  Correlation is the most important process within ASP. Stereo correlation matches the neighborhood of each pixel in the left image to a similar neighborhood in the right image. It works on a pair of overlapping 
  stereo images from corresponding cameras and creates a point cloud that can be converted to a DEM.

### Point Cloud Alignment

  An existing ground truth, such as a DEM, can be used to rectify imperfectly calibrated camera intrinsic parameters. This significantly reduces distortions in the resulting DEMs which closely align with the 
  ground truth. This work uses Copernicus 30m DEM for point cloud alignment. The resultant transformation matrix can also be used as a part of the bundle adjustment step for robust spatial coherence. 

### Map-projection

  The stereo correlation process can fail if the two images are very different – if the cameras have very different perspectives, the terrain has very steep portions. This results in large disparity values and 
  3D terrains with noise or missing values. ASP deals with this issue with the implantation of map-projection – the left and the right images can be projected onto a low-resolution smooth terrain without holes. 
  The resultant map-projected images are then used for stereo correlation. 

- Workflow Summary

  Step 1: The original SPOT 6 stereo images are used during the bundle adjustment *(bundle_adjust)* step for correcting camera intrinsics. 

  Step 2: Stereo correlation *(parallel_stereo)* is performed on the images using the bundle adjustment results obtained in *Step 1*.

  Step 3: The resultant point cloud is converted to a DEM *(point2dem)*.

  Step 4: This DEM is aligned *(pc_align)* to the Copernicus 30m DEM to obtain a transformation matrix. 

  Step 5: This transformation matrix is further utilized for a second round of bundle adjustment *(bundle_adjust)* for precise spatial coherence. 

  Step 6: The original images are then map-projected onto the lower-resolution Copernicus DEM. This step also uses the camera adjustment obtained by previously running *bundle_adjust* in *Step 5*. 

  Step 7: Stereo correlation is performed again using the map-projected images and the camera adjustment results obtained by running *bundle_adjust* in *Step 5*.

  Step 8: The point cloud is converted to a final DEM *(point2dem)*.

  <center>
  <figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_2.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_2.png" width="90%" height="90%" ></a><figcaption> Figure 2: Ames Stereo Pipeline - Workflow Summary </figcaption>
  </figure>
  </center>

## Part 2: DEM Comparison

Various stereo-matching algorithms and other parameters offered by ASP have been used in generating DEMs. Multiple DEMs generated have been compared by two means:

a) Visual Inspection  - Smoothness of hillshade, presence of holes, or other artifacts.

b) Intersection Error  - as a relative measurement of accuracy

*How can intersection error be used as a relative measurement of accuracy?*

The rays emanating from matching pixels in the cameras rarely intersect perfectly on the ground because any slight error in the position of the cameras will affect the accuracy of the rays. The actual shortest distance between the rays at this point is an important error metric that measures how self-consistent the two camera models are for this point. The distance between the two emanating rays from matching points in the cameras at their closest point of intersection is the triangulation error or the intersection error (Beyer et al., 2018). Hence, the intersection error can be used as a relative measure of the accuracy of a DEM.

The following parameters have been explored to compare DEM quality:

- Different Stereo-matching Algorithms

  ASP offers several stereo-matching algorithms of which the following three have been used:

  (i) *Block Matching* Algorithm (BM): The block matching algorithm divides the target image into fixed-size blocks and finds for each block the corresponding block in the other image that provides the best 
       match (Fuhrt, 2008).
     
  (ii) *Semi-Global Matching* Algorithm (SGM): The SGM stereovision algorithm enables pixel-wise  matching between a pair of stereo images. The results obtained using this algorithm are highly accurate and the 
       speed to generate results is high (Hirschmüller, 2008). The only downside is its characteristic streaks in the final disparity image.
 
  (iii) *More-Global Matching* Algorithm (MGM): The MGM algorithm is similar to the SGM algorithm with a few extra operations per pixel. It gives higher-quality results by removing the streaking artifacts of 
         SGM. MGM produces qualitatively and quantitatively denser results than SGM with little computation overhead (Facciolo et al., 2015). 
   
### Using Map-projected images vs Using Original Images

- Different Image Pairs
  
  SPOT imagery has three image acquisitions over the area of interest within the same orbital pass. The three images are shot with different viewing angles within the same orbit. This enables the generation of 
  3D models over the area of interest. The three images are named A, B, and C. The second image, B, is acquired by a near-vertical angle. The near-nadir image acquisition enables viewing hidden items and is 
  useful for urban or mountainous areas. The anticline in the present study has some rough patches of very steep terrain for which the second image, B, might be useful. However, the anticline also 
  has areas for which oblique viewing angles work better, and, in that case, image pair AC might be more useful.

- Different Sizes of Correlation Kernels and Sub-Pixel Kernels

  The correlation kernel size determines the window size in the left and the right image for pixel comparison. Smaller kernel sizes might enhance results for intricate features, but it could also 
  potentially increase the occurrence of false matches or noise. Three different combinations of correlation kernel and sub-pixel kernel sizes were explored.

  (i) Correlation kernel: 5x5; Sub-pixel kernel: 11x11
  
  (ii) Correlation kernel: 7x7; Sub-pixel kernel: 15x15
  
  (iii) Correlation kernel: 9x9; Sub-pixel kernel: 21x21

# Results

## Choice of Stereo-matching Algorithms

###  Hillshade of the DEMs Overlain by Elevation Values

   In Figure 3, the MGM DEM (C) has the least holes, and the BM DEM (A) has the most holes. On a closer inspection (zooming in on the DEMs), it can also be seen that the MGM and the SGM DEMs are smoother when 
   compared to the BM DEM. Overall, the MGM DEM produces the least number of artifacts.

   <center>
   <figure>
   <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_3.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_3.png" width="90%" height="90%" ></a><figcaption>  Figure 3: A - BM DEM, B - SGM DEM, C - MGM DEM </figcaption>
   </figure>
   </center>
  

###  Intersection Errors of the DEMs

   The intersection error plot, which is used in this study as a relative measurement of the accuracy of a DEM, also reveals lower overall intersection errors for the SGM and the MGM DEM (which are comparable), 
   and higher intersection error for the BM DEM.

   <center>
   <figure>
   <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_4.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_4.png" width="90%" height="90%" ></a><figcaption>  Figure 4: Plot showing comparable intersection errors for the SGM and the MGM algorithms 
   whereas higher intersection errors for the BM algorithm 
   </figcaption>
   </figure>
   </center>
  
###  A Zoomed-in Perspective

   The most jagged portion of the anticline is selected to look at the performance of the different stereo-matching algorithms in more difficult terrain scenarios.

   (i) More artifacts for the BM DEM: The hillshade reveals that the BM DEM has more artifacts than the other two DEMs.

   <center>
   <figure>
   <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_5.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_5.png" width="90%" height="90%" ></a><figcaption>  Figure 5: Hillshade reveals more artifacts in rugged areas for the BM DEM </figcaption>
   </figure>
   </center>
   

   (ii) Higher intersection error for the BM DEM: The intersection error map of the same region reveals denser areas of higher intersection error values for the BM DEM.

   <center>
   <figure>
   <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_6.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_6.png" width="90%" height="90%" ></a><figcaption>  Figure 6: Denser regions of high intersection error for the BM DEM </figcaption>
   </figure>
   </center>

   (iii) Less good pixel region (more bad pixel region) for the BM DEM: ASP facilitates generating a "good pixel map" which indicates (in gray) pixels that were successfully matched with the correlator, and (in 
   red) those that were not matched. Larger areas of unsuccessfully matched pixels can be seen for the BM algorithm.

   <center>
   <figure>
   <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_7.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_7.png" width="90%" height="90%" ></a><figcaption>  Figure 7: Grey regions show well-matched pixels and red regions show badly matched pixels. 
   Larger areas of badly matched pixels can be seen for the BM DEM. </figcaption>
   </figure>
   </center>


## Map-projecting the Original Images 

### Intersection Error of the DEMs

  The DEM created using map-projected images has a lower overall intersection error than the one created using original images.

  <center>
  <figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_8.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_8.png" width="90%" height="90%" ></a><figcaption> Figure 8: Intersection error plot for DEMs created using map-projected and original images 
  </figcaption>
  </figure>
  </center>

### Hillshade and Intersection Error Map of a Zoomed-in Area of the Anticline

  The hillshade of the DEM created using map-projected images has fewer artifacts and is relatively smoother.

  <center>
  <figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_9.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_9.png" width="90%" height="90%" ></a><figcaption> Figure 9: Hillshade and intersection error map of a zoomed-in area of the anticline. The map- 
  projected hillshade has fewer artifacts and is relatively smoother.</figcaption>
  </figure>
  </center>
  

## Choice of Image Pairs 

### Intersection Error of the DEMs

  The intersection error of the DEM created using the oblique image pair, AC, is the highest. However, it appears that for this image pair, there are larger intersection errors in the very jagged portions which 
  might have contributed to the overall higher intersection errors (see below for intersection error maps). The other not-so-jagged portions (which constitute a larger area than a few jagged belts) have lower 
  intersection errors for the DEM created using the oblique image pair (AC).

  <center>
  <figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_10.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_10.png" width="90%" height="90%" ></a><figcaption> Figure 10: Intersection error plot for DEMs created using three different image pairs 
  </figcaption>
  </figure>
  </center>

- Hillshade and Intersection Error Map of Rugged Areas with Steep Slopes

  The near-nadir image acquisition for image B enables viewing hidden items and is useful for rugged terrain. The anticline in the present study has some areas with near-vertical slopes for which the DEM 
  created using an oblique image (A or C) and a near-nadir image (B) has a smoother hillshade and lower intersection errors.

  <center>
  <figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_11.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_11.png" width="90%" height="90%" ></a><figcaption> Figure 11: The jagged portion of the anticline where the image pair AC with oblique views 
  produces the highest intersection error values. A combination of an oblique view image (A or C) with the near-nadir image (B) produces results with much lower intersection error. </figcaption>
  </figure>
  </center>
  

### Hillshade and Intersection Error Map of Areas with Gentler Slopes

  The areas that do not have very steep slopes are resolved better using oblique images A and C. The hillshade is smoother.

  <center>
  <figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_12.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_12.png" width="90%" height="90%" ></a><figcaption> Figure 12: In the not-so-jagged portion, the image pair AC has the lowest intersection error 
  values and the least number of artifacts. </figcaption>
  </figure>
  </center>

## Choice of Correlation Kernel and Sub-pixel Kernel Size 

### Intersection Error of the DEMs

  The subpixel kernel sets the correlation kernel size in units of pixels. The intersection error of the DEM created using a correlation kernel size of 9, and a sub-pixel kernel size of 21 is the lowest.

  <center>
  <figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_13.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_13.png" width="90%" height="90%" ></a><figcaption> Figure 13: Intersection error plot for DEMs created using three different kernel sizes 
  </figcaption>
  </figure>
  </center>
  

### Hillshade and Intersection Error Map of a Zoomed-in Area of the Anticline

  Based on a visual inspection, the DEM created using a kernel size 21x21 is the smoothest.

  <center>
  <figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_14.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_14.png" width="90%" height="90%" ></a><figcaption> Figure 14: Correlation kernel size of 9 produces the smoothest DEM </figcaption>
  </figure>
  </center>

# Discussion

## Comparison of Intersection Errors

   Based on the results, the MGM DEM produces the best quality DEM as opposed to the SGM and the BM DEM. It is worth comparing the intersection errors of these DEMs to the standard MGM DEM. A Q-Q plot, which is a
   scatterplot created by plotting two sets of quantiles against one another can be used to compare the intersection errors. It can be noted that while the SGM DEM's intersection error values slightly deviate 
   from the MGM DEM towards higher intersection errors, the BM DEM's values are significantly deviated.

   <center>
   <figure>
   <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_15.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_15.png" width="90%" height="90%" ></a><figcaption> Figure 15: Q-Q plot of intersection errors (with MGM intersection error values as "standard" 
   values). </figcaption>
   </figure>
   </center>

## Elevation Difference between DEMs

   Elevation difference values between the MGM DEM and the SGM and the BM DEM respectively can express how closely the DEMs align with the standard MGM DEM. A distribution of these elevation difference values 
   shows a higher standard deviation for the BM DEM as compared to the SGM DEM.
  
  - Mean dh (MGM - SGM): -0.05 +/- 1.12
  - Mean dh (MGM - BM): -0.10 +/- 2.15

   <center>
   <figure>
   <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_16.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_16.png" width="90%" height="90%" ></a><figcaption> Figure 16: Elevation difference distribution </figcaption>
   </figure>
   </center>

## Disparity Map

  The most important process of ASP is stereo correlation. ASP has a collection of algorithms that compute correspondences between pixels in the left image and pixels in the right image. A map showing these 
  correspondences is the disparity map. With the above observations, MGM DEM has been selected as the one producing the most accurate results. It is worth looking into the disparity maps of this algorithm. ASP 
  facilitates dividing the total disparity into vertical and horizontal components. It can be noted that the more rugged features have higher offset magnitudes as compared to the other features of the terrain. 
  This also suggests that the corresponding pixels are most probably incorrectly matched in very steep regions. 

  <center>
  <figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_17.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_17.png" width="90%" height="90%" ></a><figcaption> Figure 17: x offset - horizontal disparity, y offset - vertical disparity. Map showing 
  disparity components for the MGM DEM </figcaption>
  </figure>
  </center>

## Map-projection

   Map-projection transforms the original images into a pair of closely aligned images - this leaves only minor perspective differences between the images, which precisely correspond to the features targeted by 
   the stereo correlation process (Beyer et al., 2018). GIF images can elaborate qualitatively on the effect of map-projection on the original images and an improvement in incorrect disparity values between 
   corresponding pixels of the stereo images. 

   <center>
   <figure>
   <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_18.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_18.png" width="90%" height="90%" ></a><figcaption> Figure 18: Disparity between original images </figcaption>
   </figure>
   </center>

   <center>
   <figure>
   <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_19.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/AnanyaPandey_figs/Figure_19.png" width="90%" height="90%" ></a><figcaption> Figure 19: Disparity after map-projection </figcaption>
   </figure>
   </center>

# Conclusion

Stereogrammetry holds its importance in generating high-resolution surface models in areas of high relief and sparse vegetation. ASP offers a multitude of parameters for creating and refining a high-resolution DEM. Several parameters have been discussed in this study and it can be concluded that map-projecting the stereo images onto a pre-existing DEM is key to generating accurate DEMs. The disparity between corresponding pixels in original images is not a real perspective difference and can lead to large DEM errors if they are not map-projected before the stereo correlation step. It can also be seen that in difficult terrains, the MGM algorithm can create significantly better results than the other algorithms. 

This study highlights the importance of exploring intersection errors across various DEMs to measure their relative accuracy. The DEMs that visually appear smoother and better in quality than others also consistently possess lower intersection error values. 

# References

Beyer, R. A., Alexandrov, O., and McMichael, S. (2018). The ames stereo pipeline: NASA’s open source software for deriving and processing terrain data. Earth and Space Science, 5(9):537–548.

Carrera, N., Muñoz, J. A., Sàbat, F., Mon, R., & Roca, E. (2006). The role of inversion tectonics in the structure of the Cordillera Oriental (NW Argentinean Andes). Journal of Structural Geology, 28(11), 1921–1932. https://doi.org/10.1016/j.jsg.2006.07.006.

Facciolo, G., de Franchis, C., and Meinhardt, E. (2015). MGM: A Significantly More Global Matching for Stereovision. British Machine Vision Conference.

Furht, B. (2008). Encyclopedia of Multimedia. Springer, Boston, MA. https://doi.org/10.1007/978-0-387-78414-4_132.

Hirschmüller, H. (2008). Stereo processing by semiglobal matching and mutual information. IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 30, no. 2, pp. 328-341.

Shean, D. E., Joughin, I. R., Dutrieux, P., Smith, B. E., and Berthier, E. (2019). Ice shelf basal melt rates from a high-resolution digital elevation model (dem) record for Pine Island Glacier, Antarctica. The Cryosphere, 13(10):2633–2656.

Strecker, M. R., Hilley, G. E., Bookhagen, B., & Sobel, E. R. (2012). Structural, geomorphic, and depositional characteristics of contiguous and broken foreland basins: Examples from the eastern flanks of the Central Andes in Bolivia and NW Argentina. Tectonics of Sedimentary Basins, edited, pp. 508–521.

