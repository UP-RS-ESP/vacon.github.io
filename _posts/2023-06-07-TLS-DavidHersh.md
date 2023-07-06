---
title: 'Terrestrial Laser Scanning in Campus Golm: Data Acquisition and Attributes'
author: "David Hersh"
author_profile: true
date: 2023-06-07
permalink:
toc: true
toc_sticky: true
toc_label: "Terrestrial laser scanning"
header:
  overlay_image: https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/title_background_lr.jpg
  overlay_filter: 0.3
  caption: "Golm campus TLS data reflectance"
read_time: false
tags:
  - Terrestrial laser scanning
  - LiDAR
  - Point Clouds
---

Terrestrial Laser Scanning (TLS) has applications in natural sciences such as in forestry, where common applications include estimation of above-ground biomass (Gonzales, et al., 2017), and estimation of biophysical parameters (Calders, et al., 2018). Natural hazards such as coastal retreat, glacier movement, lava flows, and landslides can also be monitored with TLS (Jones and Hobbs, 2021). Applications also include infrastructure monitoring including detecting cracks in concrete (Turkan, et al., 2018) and monitoring bridge displacement (Erdélyi, et al., 2020).

The aims of this internship was to create a point cloud of the University of Potsdam Golm campus using a terrestrial laser scanner. This blog describes data acquisition and extra attributes.

*This internship was supervised by Prof. Dr. Bodo Bookhagen*

# Scanning Process

Scans were collected from August 22nd to 25th, 2022 using a Riegl VZ-400i scanner. Scan positions were chosen according to the trade-off between time limitations and a complete coverage of the campus. Each scan required approximately 60 seconds to turn 360 degrees, after which the scanner was moved to the next scan position. The distance between scan positions was chosen to be around 30 meters. The Riegl scanner has a real-time viewer which shows the current scan position in purple and previous scans in blue, as well as varying surface brightness to indicate coverage.

<figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig1_VZ_app.jpg?raw=True"><img align="right" width="800" src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig1_VZ_app.jpg?raw=True"></a>
 <figcaption> Figure 1. Scan Position and scan intensity. Brighter areas indicate a higher point density.</a>  </figcaption>
    </figure>

During scanning, the scanner screen showed objects which are captured in the point cloud as well as unreliable points (shown in red in figure 2).


<figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig2_scanpos91_filter.jpg?raw=True"><img width="800" src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig2_scanpos91_filter.jpg?raw=True"></a>
 <figcaption>Figure 2. Automated removal during scanning of unreliable points based on pulse return shape.</a>  </figcaption>
    </figure>

The unreliable points are based on the pulse shape using a proprietary Riegl algorithm. An example of a theoretical difference between filtered and unfiltered returns is shown in figure 3.

<figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig3_full_waveform_comparison.png?raw=True"><img width="800" src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig3_full_waveform_comparison.png?raw=True"></a>
 <figcaption>Figure 3. General shape of full waveform data (left) where each peak represents a return point. When multiple returns are close together, as may be case of vegetation, the return waveform can be filtered to remove this unreliable point (right). Modified from Ullrich & Pfennigbauer, 2011. </a>  </figcaption>
    </figure>

In total, the 222 scans created a complete point cloud of the Golm campus. Scanning from the roofs of buildings 27, 29, and 11 added point data to the top of buildings as well.

<figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig4_roofscanning_clip_lr.jpg?raw=True"><img width="800" src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig4_roofscanning_clip_lr.jpg?raw=True"></a>
  <figcaption>Figure 4. VZ-400i scanning from the roof of building 11. The scanner has an attached GNSS receiver at the top and a DSLR camera.</a>  </figcaption>
    </figure>

<figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig5_Scan_position_map_lr.jpg?raw=True"><img align="center" width="800" src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig5_Scan_position_map_lr.jpg?raw=True"></a>
 <figcaption>Figure 5. Overview of scan positions around the Golm campus.</a>  </figcaption>
    </figure>

The distance between scans was maintained at around 30 meters as shown in figure 6 below. When moving from the ground to roofs, the distance between scans spiked, which causes problems for the on-board registration of the Riegl scanner, resulting in mis-aligned scans.

<figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig6_Scan-scan_distances.png?raw=True"><img align="center" width="800" src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig6_Scan-scan_distances.png?raw=True"></a>
 <figcaption>Figure 6. Distances between consecutive scans.</a>  </figcaption>
    </figure>

# Notes on errors in data collection

During planning and the scanning processing, numerous factors can influence the data quality. Some important to consider include:

1. Weather conditions
- Data collection is not possible in rain or dense fog due to the interaction with water (Rasshofer and Spies, 2011)

2. Scan position
- Avoid occlusions due to objects
- Keep scan-scan distances as short as possible within time constraints
- Continuity of scan pattern (eg. pick up where you left off)

<figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig7_scanpos106_data_occlusion.png?raw=True"><img width="800" src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig7_scanpos106_data_occlusion.png?raw=True"></a>
 <figcaption>Figure 7. A scan position close to a large vehicle resulting in a gap in data behind the vehicle. This can be avoided by choosing scan positions away from large objects such as cars and trees. </a>  </figcaption>
    </figure>

# Data characteristics and attributes

After collecting data, the data was pre-processed in the Riegl software and files were exported in .laz format. Each scan had around 9 million points, giving a total number of points collected for the project at around 2 billion.

<figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig8_points_per_scan.jpg?raw=True"><img width="800" src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig8_points_per_scan.jpg?raw=True"></a>
 <figcaption>Figure 8. Number of points collected for each scan. Locations closely surrounded by buildings such as the courtyard between 27 and 29 have higher point numbers, while roof scans have as low as approx. 5 million points. </a>  </figcaption>
    </figure>

 Unlike with airborne lidar, the point densities of TLS drop quickly with distance from the scanner, therefore, each scan is considered an "unstructured" point cloud where densities are varying primarily with distance from the scanner, but also by the viewing geometry (eg. a building orthogonal to the scanner will be sampled more densely than if scanned from an oblique angle).

<figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig9_Distance_from_scanner_example.jpg?raw=True"><img width="800" src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig9_Distance_from_scanner_example.jpg?raw=True"></a>
 <figcaption>Figure 9. Example of the distribution of points based on the distance from the scanner for a single scan. Most points are within a few meters of the scanner. </a>  </figcaption>
    </figure>

Along with XYZ coordinates, each point has the following data:
- RGB data from the attached DSLR camera
- Reflectance
- Deviation
- Return number
- Number of returns

The attached DSLR camera takes 8 photos during scanning. RGB information is added to each scan automatically. The RGB information may be incomplete or incorrect, especially for partially obscured objects such as the far side of a scanned tree. Figure 10 shows common incorrect and missing data.

<figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig10_scanpos50_rgb_annotated.jpg?raw=True"><img width="800" src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig10_scanpos50_rgb_annotated.jpg?raw=True"></a>
 <figcaption>Figure 10. Examples of incorrect or missing RGB data common in vegetation. </a>  </figcaption>
    </figure>


One of the important attributes is reflectance. Reflectance is a measure of the strength of the backscatter, which is valuable for classification, object detection and other uses, but has numerous noise components, especially viewing geometry (Kashani, et al., 2015). Using the Riegl scanner, the reflectance values are not corrected for viewing geometry. Therefore, using reflectance for classification or other tasks may require correction for viewing angle first.

<figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig11_scan52_reflectance.png?raw=True"><img width="800" src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig11_scan52_reflectance.png?raw=True"></a>
 <figcaption>Figure 11. Difference in reflectance value across the same material. As the scan angle becomes more oblique, more energy is directed away from the scanner, so reflectance decreases along the building height. </a>  </figcaption>
    </figure>

Another attribute of the data is deviation, an integer value describing how many different elements contribute to a given return pulse (Calders et al., 2017). This value is also a function of the distance from the scanner (Li et al., 2018).

<figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig12_Deviation_example_scanpos40_lr.jpg?raw=True"><img width="800" src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig12_Deviation_example_scanpos40_lr.jpg?raw=True"></a>
 <figcaption>Figure 12. Pulse deviation values for a single scan. High values in vegetation indicate that mutiple components are present (eg. an irregular return pulse shape). </a>  </figcaption>
    </figure>

A last important extra attribute is the return number and number of returns. Most points in TLS are close to the scanner, and the beam divergence for the Riegl VZ-400i is ~0.3 mrad, resulting in a very small beam footprint. However, the return characteristics may be useful (eg. the first return of multiple returns could indicate vegetation). The return characteristics are shown below.

<figure>
  <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig13_return_characteristics_scanpos5.png?raw=True"><img width="2000" src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/TLS_figs_Hersh/fig13_return_characteristics_scanpos5.png?raw=True"></a>
 <figcaption>Figure 13. Example return characteristics for 7,566,659 points from scan position 5 include the return number (a), number of returns (b) and with these attributes, the return ratio (c) can be computed as return number/number of returns. </a>  </figcaption>
    </figure>

# Final remarks

Terrestrial laser scanning in the (semi-) urban environment of the Golm campus using the Riegl VZ-400i generated a large (over 2 billion points) point cloud. The full waveform data has extra attributes which can be used for classification. Some attributes, such as RGB information, is immediately usable. Other attributes, such as reflectance, may require further processing (eg. correction for viewing geometry) before further use. Data acquisition is time-consuming and susceptible to numerous errors. Therefore, planning for scanning requires careful consideration of weather conditions, objects in the scene (such as vehicles) and ideal scan patterns.



# References

Calders, K., Disney, M., Armston, J., Burt, A. J., Brede, B., Origo, N., Muir, J., & Nightingale, J. (2017). Evaluation of the Range Accuracy and the Radiometric Calibration of Multiple Terrestrial Laser Scanning Instruments for Data Interoperability. IEEE Transactions on Geoscience and Remote Sensing, 55(5), 2716–2724. https://doi.org/10.1109/tgrs.2017.2652721

Calders, K., Origo, N., Burt, A. J., Disney, M., Nightingale, J., Raumonen, P., Åkerblom, M., Malhi, Y., & Lewis, P. (2018). Realistic Forest Stand Reconstruction from Terrestrial LiDAR for Radiative Transfer Modelling. Remote Sensing, 10(6), 933. https://doi.org/10.3390/rs10060933

Erdélyi, J., Kopáčik, A., & Kyrinovič, P. (2020). Spatial Data Analysis for Deformation Monitoring of Bridge Structures. Applied Sciences, 10(23), 8731. https://doi.org/10.3390/app10238731

Jones, L., & Hobbs, P. V. (2021). The Application of Terrestrial LiDAR for Geohazard Mapping, Monitoring and Modelling in the British Geological Survey. Remote Sensing, 13(3), 395. https://doi.org/10.3390/rs13030395

Kashani, A., Olsen, M. H., Parrish, C. C., & Wilson, N. (2015). A Review of LIDAR Radiometric Processing: From Ad Hoc Intensity Correction to Rigorous Radiometric Calibration. Sensors, 15(11), 28099–28128. https://doi.org/10.3390/s151128099

Li, X., Yang, B., Xie, X., Li, D., & Xu, L. (2018). Influence of Waveform Characteristics on LiDAR Ranging Accuracy and Precision. Sensors, 18(4), 1156. https://doi.org/10.3390/s18041156


Rasshofer, R. H., Spies, M., & Spies, H. (2011). Influences of weather phenomena on automotive laser radar systems. Advances in Radio Science, 9, 49–60. https://doi.org/10.5194/ars-9-49-2011

Turkan, Y., Hong, J., Laflamme, S., & Puri, N. (2018). Adaptive wavelet neural network for terrestrial laser scanner-based crack detection. Automation in Construction, 94, 191–202. https://doi.org/10.1016/j.autcon.2018.06.017

Ullrich, A., & Pfennigbauer, M. (2011, September). Echo digitization and waveform analysis in airborne and terrestrial laser scanning. In Photogrammetric week (Vol. 11, pp. 217-228).
