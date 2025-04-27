---
title: 'Camera Calibration (1): Comparison of boards and parameters with calib.io'
author: "Bodo Bookhagen"
author_profile: true
date: 2025-04-27
toc: true
toc_sticky: true
toc_label: "Camera Calibration (1): Comparison of boards and parameters with calib.io"
header:
  overlay_image: https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/CameraCalibration1_images/checkerboard_clip.jpg 
  overlay_filter: 0.3
  caption: "Checkerboard used for camera calibration"
read_time: false
tags:
  - Camera Calibration
  - calib.io
  - checkerboard
  - Charuco
  - Kalibr
  - OpenCV
---

Precise Camera Calibration is an important part of generating high-quality points clouds and mesh models. We outline some basic procedures to generate reliable camera calibration parameters with the Calibrator software from calib.io and compare several setups, including fixed and moving camera photo taking, checkerboards and Charuco boards, and parameter optimization with Metashape Agisoft.

# Introduction 

There exist multiple ways to perform a camera calibration - [OpenCV](https://opencv.org/) is likely one of the more commonly used approach in the academic sector. There are well documented approaches and codes available (e.g. [OpenCV Camera Calibration Tutorial](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html)). There also exist commercial software packages often used in the industry. These work very well and sometimes come with their own calibration boards (e.g. [Halcon Operator Software](https://www.mvtec.com/products/halcon) and [Halcon Calibration Plates](https://www.mvtec.com/products/calibration-plates)). [calib.io](https://calib.io/) focuses on producing [camera calibration targets](https://calib.io/collections/products) and the [Calibrator software](https://calib.io/products/calib). 

In this short description, we use the Calibrator Software to generate camera calibration parameters.

## Photo-Taking Setup
We use a [Sony ILCE 7RM5](https://www.sony.com/electronics/support/e-mount-body-ilce-7-series/ilce-7rm5/specifications) ([wikipedia](https://en.wikipedia.org/wiki/Sony_%CE%B17R_V)) with a 35 mm (and 50 mm (FE 50 mm F1.4GM) fixed lens. We recorded photos in the highest resolution with 9504x6336 pixels (61MP). Photos were taken with ISO 400, F/11, and exposure times ranging from 1/500 to 1/640 s. For a set of images, we used a tripod (photos labeled *fixed*) or a moving camera with fixed board (labeled *free*). All image stabilization and filtering options were turned off. The JPG file sizes are 50-60 MB each.

All calibration photos were taken by Florian Josephowitz.

## Setting up Camera Calibration with calib.io
There exist several parameters in the calib.io Camera Calibrator software that are linked to the OpenCV implementation. During feature detection, we rely on the homography symmetry for subpixel refinement of checkerboards. The pixel refinement for the Kalibr boards is carried out with a polynomial fit.
 
During the optimization processes, we use the following options:
- *Vanishing points* for the initial calibration
- *Estimate Covariances* to have error estimates for the parameters

We do not use:
- *Optimize Target Geometry* (because our targets are of high quality)
- *Robust Norm* (because we use high quality images and assume they have low uncertainties)
- *Only decreasing steps* (because we want to explore the full landscape of parameters)

We point out that feature detection on the Charuco or Kalibr board tends to have slightly larger uncertainties (about 0.2 to 0.5 pixel higher). For the Kalibr boards, we often active the *Robust Norm* because that remove points with an uncertainty larger than 1 pixel during the inversion.

It is a good strategy to start with a low number of camera distortion parameters. For example, starting out with free parameters for focal length (f) and the principal points (cx, cy) for the extrinsic parameters. For high-quality cameras it is reasonable to assume that the focal length is the same in the x and y direction. Initial setting for the distortion model may only consider k1 and k2 for the radial distortion. These are the second and forth order parameters for a radial fit. The sixth order (k3) parameter can be added in a second step - high-quality cameras often require a limited set of parameters. The tangential distortion caused by a tilted sensor may not be required for a high-quality camera and p1 and p2 can be added in a second iteration. After running an initial optimization with only 5 parameters: f, cx, cy, k1, and k2, you may want to add k2, p1, and p2 in a second iteration. The starting point of the second optimization process is the previous result. The starting point with only 2 distortion parameters is referred to as a 2 parameter model, while the second run with 5 distortion parameters (plus f, cx, cy) is referred to as 5 parameter model. Likely, the 5 parameter model will result in a lower overall error, but you would like to avoid overfitting.

In the *Statistics tab* you should verify that the pooled statistics shows a low (<1 pixel, better < 0.5 or 0.2 pixel) Relative Pose Error (RPE).

## Calibration Boards: Checkerboard vs. Charuco (or Kalibr)
The checkerboard setup is the most straight forward board to use. The detection of the black and white squares on the board is optimized with sub-pixel refinement approaches that allow a very precise detection of the corners. The detection is fast. The drawback is that the entire checkerboard will need to be included in the photo and all corners need to have a successful subpixel refinement- otherwise the detection process will not work and the photo will not be used. This makes it somewhat difficult to take photos with the checkerboard in the very corner - but these are important for a successful calibration. Also, the detection process of the checkerboard corners is very sensitive to reflection and glare: Using the checkerboard in bright sunlight or with strong lights will likely lead to a failed detection process and hence no data points from these images. It may take some practice (and time) to take good photos with the checkerboard located in the corner. The checkerboard we used for the camera calibration have 28x17 columns x rows with a 10 mm spacing.

The Charuco or Kalibr boards have individual markers for each field. This allows to take photos with only part of the board in the photo. This is a benefit for taking photos from the corner areas. However, the marker detection is much slower than for checkerboards and also less precise, because different sub-pixel refinement methods are chosen. The Charuco board is not that sensitive toward reflection, because if the subpixel detection fails for part of the board, the other corners are still used for the calibration process. The [Kalibr board](https://calib.io/products/kalibr-targets) has 10 columns, 7 rows, and a spacing of 2.5 mm. These values will need to be entered manually. The subpixel refinement method is a *Polynomial fit*.

We find the checkerboards to be more straight forward to use for camera calibration, especially with a large number of photos (faster). But both boards produce comparable results.

We emphasize that the boards will need to be very smooth and even. Glueing a laser printed checkerboard on a cardboard will only result in a low-quality calibration board. This may work for a low resolution camera (2MP), but will be imprecise for a high-resolution camera (42 or 61 MP). A board printed on aluminium or LDPE composite sheet is preferable. We printed boards on foam and this gives reasonable results for small calibration boards (A4 size), but the boards are easily bend during transport. A curved or deformed board should not be used for camera calibration.


<center>
<figure >
  <a href="high_point_cloud.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/CameraCalibration1_images/Kalibr_parameters_col10_row7.png"></a>
</figure>
</center>
<figcaption>Figure 1: Depending on the size of the board and spacing of features, the settings have to be manually adjusted. We have used these settings for our Kalibr board.</figcaption>


# Results and Discussion

We have performed several tests to elucidate the most practical setting for camera calibration. We emphasize that the camera calibration does not need to be done during every photo taking session, but it is useful to have reliable camera calibration parameters. The calibration results were processed with tools available in out github repository [Camera Calibration](https://github.com/UP-RS-ESP/CameraCalibration). The python codes *calib-to-opencv.py* was used to convert the json output from the Calibrator software to OpenCV xml, and the code *compareDistortion_from_CC_xml.py* was used to create the figures shown below.

We tested the following scenarios:
- Fixed vs. moving camera calibration
- Varying camera calibration parameters (only radial vs. radial and tangential parameters)
- Comparison of checkerboard vs. Charuco boards
- Optimization of an existing camera calibration file during Metashape Agisoft photo alignment step


## Fixed and Moving-Camera Calibration
There appears to be only very small differences between fixed and free-board calibrations. 

<center>
<figure >
    <a href="Sony_ILCE-7RM5_35mm_checkerboard_free_fixed_5p_25Apr2025_2panel.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/CameraCalibration1_images/Sony_ILCE-7RM5_35mm_checkerboard_free_fixed_5p_25Apr2025_2panel.png"></a>
</figure>
</center>
<figcaption>Figure 2: Visualization of the radial and tangential camera calibration parameters for the 35 mm lens (Sony 7RM5). The blue cross marks the camera center and the orange triangle the (cx,cy) coordinate. Arrows indicate the direction of pixel offset when performing camera calibration. Colors and contour lines show magnitude of offset. There are about 20 pixels offsets in the far corners. Calibration was carried out with more than 100 photos for each setting (fixed camera and moving camera). </figcaption>

<center>
<figure >
    <a href="Sony_ILCE-7RM5_35mm_checkerboard_free_fixed_5p_25Apr2025_2panel_diff.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/CameraCalibration1_images/Sony_ILCE-7RM5_35mm_checkerboard_free_fixed_5p_25Apr2025_2panel_diff.png"></a>
</figure>
</center>
<figcaption>Figure 3: Offset difference between fixed and moving cameras. The absolute magnitude (left) shows the distortion difference in pixels when using the different camera acquisition setups. The difference is low to moderate, given that the camera has 9504x6336 pixels. The factor difference (difference of both calibrations divided by fixed camera calibration) shows that there are some spots where the difference in camera calibration is about three times as high as distortion offset amount. This likely indicates that there were not enough calibration points taken in this area of the camera field.  </figcaption>

<center>
<figure >
    <a href="Sony_ILCE-7RM5_50mm_checkerboard_free_fixed_5p_25Apr2025_2panel_diff.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/CameraCalibration1_images/Sony_ILCE-7RM5_50mm_checkerboard_free_fixed_5p_25Apr2025_2panel_diff.png"></a>
</figure>
</center>
<figcaption>Figure 4: Same as Figure 3, but for 50 mm lens. Again the difference between fixed and moving (free) camera results in comparable calibration results. The difference between the calibration parameters results in a low to moderate pixel offset. </figcaption>


## Radial (2 parameter) vs. Radial and Tangential Distortion (5 parameters) Models
We explore using a limited number of camera calibration parameters to prevent overfitting and explore the lens optics. We use a radial distortion model with only two parameters (k1 and k2 corresponding to a second and fourth order polynome describing the radial field) and no tangential distortion. We compare this to a 5-parameter distortion model that is often applied (k1, k2, k3 describe radial distortion and p1 and p2 describe tangential distortion). 

<center>
<figure >
    <a href="Sony_ILCE-7RM5_35mm_checkerboard_free_2p5p_25Apr2025_2panel_diff.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/CameraCalibration1_images/Sony_ILCE-7RM5_35mm_checkerboard_free_2p5p_25Apr2025_2panel_diff.png"></a>
</figure>
</center>
<figcaption>Figure 5: Difference between 2 and 5 parameter calibration models for the 35 mm lens with moving camera acquistions. We note that the 5 parameter model with higher orders of polynomes better captures the steep curvature in the far corner. Overall, the difference is rather low, suggesting that a two parameter model may be sufficient for some cases.  </figcaption>

<center>
<figure >
    <a href="Sony_ILCE-7RM5_50mm_checkerboard_fixed_2p5p_25Apr2025_2panel_diff.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/CameraCalibration1_images/Sony_ILCE-7RM5_50mm_checkerboard_fixed_2p5p_25Apr2025_2panel_diff.png"></a>
</figure>
</center>
<figcaption>Figure 6: Difference between 2 and 5 parameter calibration models for the 50 mm lens for a fixed setup. A longer focal length has lower distortion on the sides of the lens and the 2 parameter calibration is a reasonable model for this lense. However, in subsequent runs, we will rely on the 5 parameter model, because the overall RPE (relative pose error) is lower.  </figcaption>
 

## Checkerboard vs. Charuco (Kalibr) Board
A comparison between the checkerboard and Charuo board reveals that results are comparable. We note the large relative pose error of the Charuco boards because of less precise subpixel corner detection and fewer calibration points. 

<center>
<figure >
    <a href="Sony_ILCE-7RM5_35mm_checkerboard_charuco_free_5p_25Apr2025_2panel_diff.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/CameraCalibration1_images/Sony_ILCE-7RM5_35mm_checkerboard_charuco_free_5p_25Apr2025_2panel_diff.png"></a>
</figure>
</center>
<figcaption>Figure 7: Difference between the distortion model for the calibration performed with the checkerboard and Charuco board. Results for the 35 mm lens are shown. The calibration results tend to agree with generally low differences.  </figcaption>

## Refining Camera Calibration parameters
A reasonably reliable camera calibration can be used as a starting point for further refinement. Camera calibration relies on the detection of specific markers (e.g., squares), but SIFT features identified during structure from motion processing can also be used. Refining camera calibration within openMVS or Agisoft Metashape is really only useful if there is a very strong camera geometry (i.e., many photos taken from different angles - similar to a calibration processes). The advantage of a SIFT based refinement is that there are usually many more features to perform calibration on. Here, we use the camera calibration parameters generated with the checkerboard and perform a photo alignment using SIFT features within Agisoft Metashape. We use the camera calibration as starting point and allow them to be refined during the optimization process. The setup consists of 124 photos for a 2x2 m area and results in a strong camera geometry. We furthermore have additional markers in the field (24 Agisoft markers and scales). An alternative way to look at this step is to validate the camera calibration.

We note that camera alignment with pre-calibrated lenses is faster and results in much better constrained tie points. The covariances of the tie points are lower than using the same setup without pre- calibration. The resulting calibration parameter differ, suggesting that the matrix inversion solving for camera position (6 parameters) and camera distortion (8 parameters) is not well constrained.

<center>
<figure >
    <a href="Sony_ILCE-7RM5_50mm_checkerboard_fixed_MetashapeOptimized_5p_25Apr2025_2panel_diff.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/CameraCalibration1_images/Sony_ILCE-7RM5_50mm_checkerboard_fixed_MetashapeOptimized_5p_25Apr2025_2panel_diff.png"></a>
</figure>
</center>
<figcaption>Figure 8: Difference between the distortion model generated from a fixed checkerboard setting and a Metashape Agisoft optimized camera calibration from a scene with strong camera geometry. Results for the 50 mm lens are shown. The optimization process in Agisoft Metashape only slightly changed the camera calibration parameters. The tie point cloud and the surface mesh model generated from depth map after the optimization step have high qualities. </figcaption>

# Conclusion

A careful camera calibration results in faster and more accurate photo alignment during the structure from motion process. The point clouds and mesh surfaces generated within Metashape Agisoft with a pre-calibrated camera were more precise with less noise. The photo alignment step also ran faster. The optimized camera calibration parameters with a pre-calibrated camera are different than the optimized results without camera calibration. This suggests that the inversion step optimizing for camera position and distortion poses an ill defined matrix inversion problem. We suggest to always provide pre-calibration parameters.

Our results indicate that reliable results can be generated from various setups. Free or fixed camera setups provide similar parameters. The photo taking with a moving camera is likely faster, although a tripod can provide extra stability in low-light condition. The type of board does not matter, but we prefer to use checkerboards for the ease of use and faster processing.


