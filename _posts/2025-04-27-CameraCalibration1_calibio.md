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

The Charuco or Kalibr boards have individual markers for each field. This allows to take photos with only part of the board in the photo. This is a benefit for taking photos from the corner areas. However, the marker detection is much slower than for checkerboards and also less precise, because different sub-pixel refinement methods are chosen. The Charuco board is not that sensitive toward reflection, because if the subpixel detection fails for part of the board, the other corners are still used for the calibration process.

We find the checkerboards to be more straight forward to use for camera calibration, especially with a large number of photos (faster). But both boards produce comparable results.

The [Kalibr board](https://calib.io/products/kalibr-targets) has 10 columns, 7 rows, and a spacing of 2.5 mm. These values will need to be entered manually. The subpixel refinement method is a *Polynomial fit*.


<div style="display: flex; flex-direction: row; justify-content: center;">
    <figure style="flex: 1; margin-right: 0px;">
        <a href="high_point_cloud.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/CameraCalibration1_images/Kalibr_parameters_col10_row7.png"></a>
    </figure>
</div>
<br/>
<figcaption>Figure 1: Depending on the size of the board and spacing of features, the settings have to be manually adjusted. We have used these settings for the Kalibr board.</figcaption>


# Results

We have performed several tests to elucidate the most practical setting for camera calibration. We emphasize that the camera calibration does not need to be done during every photo taking session, but it is useful to have reliable camera calibration parameters. The calibration results were processed with tools available in out github repository [Camera Calibration](https://github.com/UP-RS-ESP/CameraCalibration). The python codes 'calib-to-opencv.py' was used to convert the json output from the Calibrator software to OpenCV xml, and the code 'compareDistortion_from_CC_xml.py' was used to create the figures shown below.

We tested the following scenarios:
- Fixed vs. moving camera calibration
- Varying camera calibration parameters (only radial vs. radial and tangential parameters)
- Comparison of checkerboard vs. Charuco boards
- Optimization of an existing camera calibration file during Metashape Agisoft photo alignment step


## Fixed and Moving-Camera Calibration
There appears to be only very small differences between fixed and free-board calibrations. 
![Sony 7RM5 35 mm calibration with checkerboard and 5 distortion parameters. Differences shows calibration with fixed camera and moving camera (both datasets have more than 100 photos). There are about 6 pixel difference in calibration offset.](Sony_ILCE-7RM5_35mm_checkerboard_free_fixed_5p_25Apr2025_3panel.png)

![Sony 7RM5 50 mm calibration with checkerboard and 5 distortion parameters. Differences shows calibration with fixed camera and moving camera (both datasets have more than 100 photos). There are about 2 pixel difference in calibration offset.](Sony_ILCE-7RM5_50mm_checkerboard_free_fixed_5p_25Apr2025_3panel.png)

## Radial (2 parameter) vs. Radial and Tangential Distortion (5 parameters) Models
We note some differences between the 2 and 5 parameter calibration routines. 
![The 35 mm lens shows different patterns and an overall lower relative pose error with 5 parameters. There are up to 15 pixel difference in calibration offsets at the borders.](Sony_ILCE-7RM5_35mm_checkerboard_free_2p5p_25Apr2025_3panel.png)

![The 55 mm lens behaves very well and there is only a small difference between 2 and 5 parameter calibration approaches. This suggests that the 2 parameter distortion model may be sufficient to describe and model offsets. The overall relative pose error is lower with the 5 parameter model.](Sony_ILCE-7RM5_50mm_checkerboard_free_fixed_5p_25Apr2025_3panel.png)

## Checkerboard vs. Charuco (Kalibr) Board

