---
title: 'Detecting ENSO events using GRACE satellites in South America'
author: "Andyara Callegare"
author_profile: true
date: 2021-06-15
permalink: /posts/2021/06/GRACE
toc: true
toc_sticky: true
toc_label: "Detecting ENSO events using GRACE satellites in South America"
header:
  overlay_image: https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/banner.jpg
  overlay_filter: 0.3
  caption: "Detecting ENSO events using GRACE satellites in South America"
read_time: false
tags:
  - ENSO
  - GRACE
  - total water storage
  - South America
---

Changes in global Total Water Storage (TWS) can be measured with satellites sensitive to gravity acceleration using the *Gravity Recovery and Climate Experiment* (*GRACE*) and its successor the *Gravity Recovery and Climate Experiment-Follow-On* (*GRACE-FO*). Here is an example research study from South America.

In South America is no abundant network of in-situ hydrometeorologic stations, but over the last decades, an increased number of remote-sensing sensors showed an unprecedented view of the region. The unique *Gravity Recovery and Climate Experiment* (*GRACE*) and its successor the *Gravity Recovery and Climate Experiment-Follow-On* (*GRACE-FO*) have been orbiting the earth since 2002 and use gravity to map water masses and their changes. Its variable Total Water Storage (TWS) change is defined as changes in water stored on the surface (e.g., lakes and reservoirs, rivers, and snow water equivalent), over the entire soil profile, and in groundwater (Long et al., 2015).

The El Nino-Southern Oscillation (ENSO) is the dominant interannual variability of Earth’s climate system and plays a central role in global climate prediction. Outlooks of ENSO and its impacts often follow a two-tier approach: predicting ENSO sea surface temperature anomaly in tropical Pacific and then predicting its global impacts (Lin & Qian, 2019). El Niño and La Niña events denote sea-surface temperature (SST) conditions in the tropical Pacific that are, respectively, warmer and colder than average (McPhaden et al., 2006), as seen in Figure 1 by Chiodi & Harrison, 2015.

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_01.png?raw=true"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_01.png?raw=true"></a><figcaption>Figure 1: The familiar ENSO concept in a cartoons, illustrating the subsurface (thermocline) surface (SSTA, SLP,and near-surface winds) and atmospheric convection conditions commonly associated with (left) La Niña, (center) ENSO-neutral, and (right) El Niño states. From <a href="https://www.researchgate.net/publication/277901561_Global_seasonal_precipitation_anomalies_robustly_associated_with_El_Nino_and_La_Nina_events_-_an_OLR_perspective">Chiodi & Harrison (2015)</a>. </figcaption>
</figure>
</center>

Muñoz et al., 2016, describes the effects of this system in Latin Americas (Figure 2). As a starting point to understand the variability in South America the analysis will focus on the two major river basins, the Amazon and La Plata. The expected pattern during El Niño the Amazon (La Plata) basin is dry (wet) from June (September) to march (January). The pattern during La Niña for the Amazon (La Plata) basin is wet (dry) from June (August) to march (December).

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_02.png?raw=true"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_02.png?raw=true"></a><figcaption>Figure 2: El Niño (left) and La Niña (right) rainfall impacts in Latin America and the Caribbean. From <a href="https://www.researchgate.net/publication/303471112_The_Latin_American_and_Caribbean_Climate_Landscape_for_ZIKV_Transmission"> Muñoz et al. (2016)</a>. </figcaption>
</figure>
</center>

Since precipitation is an important component in hydrological and climate change studies (Jia et al., 2020) and anomalies of GRACE TWS have a close relationship with precipitation, Abelen et. al, 2015 concluded that it tends to be shifted by a few months in the La Plata Basin. It is expected to see a relationship between strong ENSO events, both positive and negative, reflected in TWS. This internship seeks out to give insight into the following questions:


- *What are the seasonal patterns of TWS?*

- *Can GRACE TWS be fit into a simple sine model?*

- *Is there a relationship between ENSO and TWS?*

**This internship was supervised by Prof. Dr. Bodo Bookhagen and Dr. Taylor Smith.**

# Oceanic Niño Index (ONI)

The Oceanic Niño Index (ONI) is NOAA's primary indicator for monitoring El Niño and La Niña, which are opposite phases of the climate pattern called the El Niño-Southern Oscillation, or “ENSO” for short. NOAA considers El Niño conditions to be present when the Oceanic Niño Index is +0.5 or higher, indicating the east-central tropical Pacific is significantly warmer than usual. La Niña conditions exist when the Oceanic Niño Index is -0.5 or lower, indicating the region is cooler than usual. The data set is available at [https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt](https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt).

The ONI tracks the running 3-month average sea surface temperatures in the east-central tropical Pacific between 120°-170°W. This area is called the Niño 3.4 region, and its shown in Figure 3.

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_03.png?raw=true"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_03.png?raw=true"></a><figcaption>Figure 3: Location of the Niño regions for measuring sea surface temperature in the eastern and central tropical Pacific Ocean. The sea surface temperature in the Niño3.4 region, spanning from 120˚W to 170˚W longitude, when averaged over a 3-month period, forms NOAA’s official Oceanic Niño Index (the ONI). NOAA Climate.gov image by Fiona Martin. Figure from <a href="https://www.climate.gov/news-features/understanding-climate/climate-variability-oceanic-ni%C3%B1o-index"> Dahlman, L. (2016)</a>. </figcaption>
</figure>
</center>

The most intense months recorded events - or both El Nino and La Nina - are described in the tables bellow.


## El Niño

| Date       | Anomaly   |
|------------|-----------|
| 15.12.2015 | 2.64      |
| 15.11.1205 | 2.57      |
| 15.01.2016 | 2.48      |
| 15.10.2015 | 2.42      |
| 15.11.1997 | 2.40      |
| 15.12.1997 | 2.39      |
| 15.10.1997 | 2.33      |
| 15.01.1998 | 2.24      |
| 15.12.1982 | 2.23      |
| 15.01.1983 | 2.18      |

For El Nino the most intense 10 months have SST anomalies ranging from 2.18 to 2.64 °C. These values are divided into 3 episodes.

1. The most intense one has its peak in 1982-12, values above 0.5 started in 1982-05 and were continuously above this threshold until 1983-08, 15 months in total. The two highest values were registered during this episode.

2. The second most intense episode has its peak in 1997-10, values above 0.5 started in 1997-05 and were continuously above this threshold until 1998-04, 12 months in total. The 3rd to 6th highest values were registered during this episode.

3. And the third one has its peak in 2015-12, values above 0.5 started in 2014-10 and were continuously above this threshold until 2016-04, 19 months in total. The 7th to 10th highest values were registered during this episode.


## La Niña

| Date       | Anomaly   |
|------------|-----------|
| 15.12.1973 | -2.03     |
| 15.11.1973 | -1.95     |
| 15.12.1988 | -1.85     |
| 15.01.1974 | -1.84     |
| 15.11.1988 | -1.8      |
| 15.10.1973 | -1.71     |
| 15.01.1989 | -1.69     |
| 15.11.1955 | -1.67     |
| 15.01.2000 | -1.66     |
| 15.12.1999 | -1.65     |


For La Nina the most intense 10 months have anomalies ranging from -2.03 to -1.65 °C. These values are divided into 4 episodes.

1. The most intense one has its peak in 1955-11, values below -0.5 started in 1954-05 and were continuously below this threshold until 1956-08, 28 months in total. The lowest value was registered during this episode.

2. The second most intense episode has its peak in 1973-11, values below -0.5 started in 1973-05 and were continuously below this threshold until 1976-03, 35 months in total. The 1st, 2nd, 4th and 6th lowest values were registered during this episode.

3. The third most intense has its peak in 1988-12, values below -0.5 started in 1988-05 and were continuously below this threshold until 1989-05, 13 months in total. The 3rd, 5th and 7th lowest values were registered during this episode.

4. And the fourth most intense episode has its peak in 2000-01, values bellow -0.5 started in 1998-06 and were continuously below this threshold until 2001-02, 31 months. The 9th and 10th lowest values were registered during this episode.

Positive episodes have a higher amplitude and shorter length compared with the positive ones.

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_04.png?raw=true"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_04.png?raw=true"></a><figcaption>Figure 4: Oceanic Niño Index from 1950 to 2021 and its most intense El Nino (red) and La Nina (blue) episodes, the colour transparency is related to the intensity of the episodes, intense episodes are more opaque. </figcaption>
</figure>
</center>

# GRACE and GRACE-FO

The Gravity Recovery and Climate Experiment (GRACE) and the Gravity Recovery and Climate Experiment Follow-On (GRACE-FO) missions are a partnership between NASA and the German Research Centre for Geosciences (GFZ). GRACE-FO from 2018 and onwards is a successor to the original GRACE mission that orbited the earth from 2002-2017. These satellites map the gravity field, and since the surface changes at a very slow rate in comparison with water, these monthly changes are mostly attributed to water moving over and below the surface and on the oceans. Data were acquired from the PO.DAAC Drive ([https://podaac-tools.jpl.nasa.gov/drive/files/allData/grace/L3/land_mass/RL06/v03/](https://podaac-tools.jpl.nasa.gov/drive/files/allData/grace/L3/land_mass/RL06/v03/) and [https://podaac-tools.jpl.nasa.gov/drive/files/allData/gracefo/L3/land_mass/RL06/v03/](https://podaac-tools.jpl.nasa.gov/drive/files/allData/gracefo/L3/land_mass/RL06/v03/)) for all the different centres' solutions processing: *Center for Space Research* (CSR), the *Jet Propulsion Laboratory* (JPL) and the *German Research Centre for Geosciences* (GFZ). The monthly data have a spatial resolution of 1° latitude x 1° longitude for all the landmasses. The variable total water storage anomalies (TWS) represents the anomalies of the sums the total of the water mass contained in different hydrological reservoirs, including surface, soil moisture, groundwater, and snowpack component (Hasan et al., 2019).
A spatial sum for the area inside of the shapefile (and individual geometries) was performed, resulting in a time series of 163 months for GRACE, starting from April 2002 to June 2017; and for GRACE-FO a time series of 31 months, starting from June 2018 to February 2021.

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_05.png?raw=true"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_05.png?raw=true"></a><figcaption>Figure 5: GRACE's global total water storage change for the different processing centers (CSR, JPL, and GFZ). The period without data is highlighted in grey. </figcaption>
</figure>
</center>

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_06.png?raw=true"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_06.png?raw=true"></a><figcaption>Figure 6: GRACE's global total water storage change difference from processing centers (CSR, JPL, and GFZ). The period without data is highlighted in grey. </figcaption>
</figure>
</center>

The above graphs have a few interesting features:

- it seems that the global water storage change has a negative linear trend
- it has a seasonal behaviour, maintaining a similar amplitude
- the centres' solutions are very similar, specially between CSR and JPL
- The differences are higher after 2011 until 2017, when GRACE stopped its mission

With this knowledge some decisions for the further steps were made:

- the final solution will be the mean of the 3 centres'
- the data set it's going to be fit into a sine model, because this will allow to fill in the gap between the months without data in 2017-2018.

# Study Area
The study area comprehends the 2 biggest major river basins from South America, Amazon and Rio de La Plata, shown in Figure 7. The geometry was extracted from the WMO Basins 3rd, revised and extended edition 2020, available at [https://www.bafg.de/GRDC/EN/02_srvcs/22_gslrs/223_WMO/wmo_regions_node.html#doc2763412bodyText7](https://www.bafg.de/GRDC/EN/02_srvcs/22_gslrs/223_WMO/wmo_regions_node.html#doc2763412bodyText7.).
Amazon has approximately 4.9 M km<sup>2</sup>, followed by Rio de La Plata with 3.0 M km<sup>2</sup>.

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Figure_07_new.png?raw=true"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Figure_07_new.png?raw=true"></a><figcaption>Figure 7: Major river basins in South America, with Amazon and Rio de La Plata containing GRACE's TWS for Dezember 2015. Amazon (La Plata) is the upper (lower) Basin. On this date there's an El Niño happening, and TWS is reflecting the expected behaviour, with the Amazon (La Plata) Basin having a negative (positive) anomaly, meaning that it is drier (wetter) than usual. </figcaption>
</figure>
</center>

# Models
Using python 3.8 it was possible to fit GRACE TWS into the following models:

## Non-Linear Least-Squares Minimization and Curve-Fitting (LMFIT)

```python
from scipy.signal import find_peaks
from lmfit.model import Model

# find amplitude
positive_peaks_idx = find_peaks(obs)[0]
neagtive_peaks_idx = find_peaks(-obs)[0]

amplitudes =[]
for i in range(0,len(positive_peaks_idx)):
    amplitudes.append(obs[positive_peaks_idx[i]] - obs[neagtive_peaks_idx[i]])

# fit sine
def mysine(x, amp, freq, shift):
    return amp * np.sin(x*freq + shift)

# define x and y
x = dates
y = obs

# initialize model
model = Model(mysine)

# initial guess
params = model.make_params(amp=np.mean(amplitudes), freq=1/2, shift=0)
params['shift'].max = 10
params['shift'].min = -10
params['amp'].min = 10
params['amp'].max = 50
params['freq'].min = 1/10
params['freq'].max = 2

result = model.fit(y, params, x=x)
 # result
yy = result.best_fit
print(result.fit_report())

 # inital guess
yyy = result.init_fit
```

## Seasonal Decomposition using moving averages

```python
from statsmodels.tsa.seasonal import seasonal_decompose

# decompose
# model is additive because the amplitude is the same
# period is 12 because we are interested interannual variability
SD = seasonal_decompose(obs, model='additive', period=12)

SD_seasonal = SD.seasonal # seasonal signal
SD_trend = SD.trend # trend signal
SD_resid = SD.resid # residue
```

This function will return seasonal, trend, and residual signals. Adding then will reconstruct the original observation.

## Seasonal-Trend decomposition using LOESS
```python
from statsmodels.tsa.seasonal import STL as STL_decompose
seasonal = 12 + ((12 % 2) == 0)  # Ensure odd

# non robust
STL = STL_decompose(obs, period=12, seasonal=seasonal)
STL = STL.fit()

# robust
STL_robust = STL_decompose(obs, period=12, seasonal=seasonal, robust=True)
STL_robust = STL_robust.fit()
```

This function also return seasonal, trend, and residual signals. Adding then will reconstruct the original observation.


# Compare Models
For each Basin a spatial sum of TWS for the area inside of the shapefile (and individual geometries) was performed, resulting in a single time series of 163 months for GRACE, starting from April 2002 to June 2017; and for GRACE-FO into a time series of 31 months, starting from June 2018 to February 2021. The months without data were left empty and the models were able to fill this period with data.

## Amazon

The seasonal signal is out of phase in the LMFIT initial guess, but this is corrected by the model with a shift of -4.79 months.
All models correlate between 0.86 and 0.89, the frequency is 12 months, and the amplitude varies between 114.86 to 155.02.
overall all models converge to similar patterns.

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_08.png?raw=true"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_08.png?raw=true"></a><figcaption>Figure 8: Seasonal Signal for the Amazon Basin. 1st row is Non-Linear Least-Squares Minimization and Curve-Fitting (LMFIT) initial guess, 2nd row is LMFIT model, 3rd row is the seasonal signal from the Seasonal Decomposition using moving averages (SD), 4th row is the seasonal signal from Seasonal-Trend decomposition using LOESS (STL), 5th row is the seasonal signal from STL robust. For all rows, the observed signal is in black. </figcaption>
</figure>
</center>

| Model               | Correlation | Frequency | Amplitude |
|---------------------|-------------|-----------|-----------|
| LMFIT_init          | -0.20       | 13.0      | 75.35     |
| LMFIT               | 0.87        | 12.0      | 155.02    |
| SD                  | 0.87        | 12.0      | 125.00    |
| STL                 | 0.89        | 12.0      | 114.86    |
| STL_robust          | 0.87        | 12.0      | 141.35    |

The interannual seasonality described by the trend is also in agreement between all models (cf. Figure 9).

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_09.png?raw=true"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_09.png?raw=true"></a><figcaption>Figure 9: Interannual trend for the Amazon Basin. Non-Linear Least-Squares Minimization and Curve-Fitting (LMFIT) was estimated by subtracting the observation from the model and applying a moving average of 12 months. Seasonal Decomposition using moving averages (SD), Seasonal-Trend decomposition using LOESS (STL), and STL robust are extracted directly from the models' trend signal. </figcaption>
</figure>
</center>


## La Plata

La Plata TWS is less regular than the Amazon, but still has a seasonal pattern to it.
The shift between LMFIT and its initial guess is -4.37 months.
The models have a lower correlation, between 0.56 and 0.57. And the frequency is 12 months for LMFIT and SD, but 9 and 7.5 months for STL and STL robust. But the amplitudes are in agreement varying between 11.44 and 15.29 meters.

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_10.png?raw=true"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_10.png?raw=true"></a><figcaption>Figure 10: Seasonal Signal for the La Plata Basin. 1st row is Non-Linear Least-Squares Minimization and Curve-Fitting (LMFIT) initial guess, 2nd row is LMFIT model, 3rd row is the seasonal signal from the Seasonal Decomposition using moving averages (SD), 4th row is the seasonal signal from Seasonal-Trend decomposition using LOESS (STL), 5th row is the seasonal signal from STL robust. For all rows, the observed signal is in black. </figcaption>
</figure>
</center>

| Model               | Correlation | Frequency | Amplitude |
|---------------------|-------------|-----------|-----------|
| LMFIT_init          | -0.12       | 13.0      | 12.20     |
| LMFIT               | 0.56        | 12.0      | 11.95     |
| SD                  | 0.56        | 12.0      | 11.44     |
| STL                 | 0.59        | 9         | 14,01     |
| STL_robust          | 0.57        | 7.5       | 15.29     |

The interannual seasonality is in agreement between all models (Figure 11).

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_11.png?raw=true"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_11.png?raw=true"></a><figcaption>Figure 11: Interannual trend for the La Plata Basin. Non-Linear Least-Squares Minimization and Curve-Fitting (LMFIT) was estimated by subtracting the observation from the model and applying a moving average of 12 months. Seasonal Decomposition using moving averages (SD), Seasonal-Trend decomposition using LOESS (STL), and STL robust are extracted directly from the models' trend signal. </figcaption>
</figure>
</center>

# ONI x Models

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_12.png?raw=true"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_12.png?raw=true"></a><figcaption>Figure 12: Oceanic Niño Index (ONI) in Celcius and the average interannual trends for Amazon and La Plata Basins in meters. Highlighted are the ENSO events, El Niño in red and La Niña in Blue. </figcaption>
</figure>
</center>

ONI registered 8 (8) El Nino (La Nina) episodes. Notably, there's one big interval of neutrality between 2012-04 and 2014-10.

Amazon and La Plata seem to be inversely related, as expected, but not in a regular way.

Although ENSO episodes are determined from a threshold of 0.5 (-0.5) for El Nino (La Nina), applying this threshold to GRACE Trends won't produce suitable results. But, the slope of the curve seems to be related to ENSO episodes. For Amazon (La Plata) when its curve has a negative (positive) slope usually it's in sync with an El Nino (La Nina) episode. So, calculating the slope of the curve can be useful in relating to ENSO events.

<center>
<figure>
<a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_13.png?raw=true"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/GRACE_figs/Fig_13.png?raw=true"></a><figcaption>Figure 13: Oceanic Niño Index (ONI) in Celcius and derived slope from the average interannual trends for Amazon and La Plata Basins in meters. For each row, ENSO events are highlighted, El Niño in red and La Niña in Blue. For ONI the threshold is 0.5 (-0.5) Celcius for El Niño (La Niña). For The Amazon Basin the threshold is 1.5 (-1.5) meters for El Niño (La Niña). And for La Plata Basin the threshold is 0.75 (-0.75) meters for El Niño (La Niña). </figcaption>
</figure>
</center>

The slope of the curves produces a similar pattern to ONI, although the same threshold can't be applied to it.

For the Amazon, it was adjusted to 1.5 and for La Plata to 0.75. Since Amazon is inversely related to ONI the signal was inverted when determining El Nino and La Nina events.

Amazon registered 11 (12) El Nino (La Nina) episodes. This method was capable to identify most of the events, but not their duration. It underestimated the length of long La Ninas and overestimated the length of short ones. Between 2005 and 2012, all events were represented. But during ONI's long period of neutrality, the analysis indicated 1 El Nino and 4 short La Ninas. In the end, it matched 6 (6) episodes for El Nino (La Nina), detecting 75% of all ENSO events.

La Plata registered 4 (8) El Nino (La Nina) episodes. Until 2006 it didn't represent ENSO episodes well, it was unable to detect 2 El Ninos and indicated a La Nina when it didn't happen. After this period, it was able to represent all episodes, except a short El Nino by the end of 2014. In the middle of 2019, La Plata indicates a long La Nina, when ONI represents a short El Nino by the end of 2019 and then a longer La Nina on the second semester of 2020. Despite getting the length wrong, it was able to match 7 (4) of El Nino (La Nina) episodes, having a detection rate of 87.5% (50%). For El Nino (La Nina) there was a tendency in overestimating (underestimating) the length.

# Conclusions
GRACE TWS solutions from the 3 different centres' were very similar. They all show the existence of a wet and dry season with one cycle takes approximately 12 months to complete. For the Amazon basin, the dry (wet) season is during the austral summer (winter). La Plata has an inverse relation, exhibiting wet (dry) summer (winter).

Since GRACE has a cyclic pattern on its signal it was possible to fit into a sine function using several approaches, such as Non-Linear Least-Squares Minimization and Curve-Fitting, Seasonal decomposition using moving averages, and Seasonal-Trend decomposition using LOESS. They all yield similar results in the seasonal signal analysis. Although there are some notable differences, LMFIT and SD provide a solution with a fixed amplitude, while STL can adjust its amplitude according to the input data. Amazon has a clear seasonality on its signal, this resulted in a correlation between 86% and 88%, La Plata signal is very noisy, hence the lower correlation between 55% and 59%. In both cases, STL had the highest correlation.

A simple comparison between the computed trend and ONI was not precise in pointing the relationship between them. An untrained eye might think about a phase shift, but a closer inspection of the curve pattern indicates that the slope has a closer relationship with ONI and can be used to detect ENSO events. The Amazon basin was able to detect 75% of all ENSO events, but the duration was not matched, it tends to underestimate the length of long La Nina and overestimate the short ones. La Plata detected 87.5% of El Ninos but only 50% of La Nina, and again the duration was not matched, there was a tendency in overestimating El Nino and underestimating La Nina.

All models are capable of representing GRACE's TWS signal, and the slope of the trend is useful in identifying ENSO episodes, albeit it should be used carefully and more refinement in the method is needed.

# References
Abelen, S., Seitz, F., Abarca-del-Rio, R., & Güntner, A. (2015). Droughts and floods in the La Plata basin in soil moisture data and GRACE. Remote Sensing, 7(6), 7324-7349. [https://mediatum.ub.tum.de/doc/1323693/file.pdf](https://mediatum.ub.tum.de/doc/1323693/file.pdf)

Alexander, M. A., Bladé, I., Newman, M., Lanzante, J. R., Lau, N. C., & Scott, J. D. (2002). The atmospheric bridge: The influence of ENSO teleconnections on air–sea interaction over the global oceans. Journal of climate, 15(16), 2205-2231. [https://www.researchgate.net/profile/Matthew-Newman-7/publication/241092472_The_Atmospheric_Bridge_The_Influence_of_ENSO_Teleconnections_on_Air-Sea_Interaction_over_the_Global_Oceans/links/02e7e528e3c9ba9707000000/The-Atmospheric-Bridge-The-Influence-of-ENSO-Teleconnections-on-Air-Sea-Interaction-over-the-Global-Oceans.pdf](https://www.researchgate.net/profile/Matthew-Newman-7/publication/241092472_The_Atmospheric_Bridge_The_Influence_of_ENSO_Teleconnections_on_Air-Sea_Interaction_over_the_Global_Oceans/links/02e7e528e3c9ba9707000000/The-Atmospheric-Bridge-The-Influence-of-ENSO-Teleconnections-on-Air-Sea-Interaction-over-the-Global-Oceans.pdf)

Cai, W., McPhaden, M. J., Grimm, A. M., Rodrigues, R. R., Taschetto, A. S., Garreaud, R. D., ... & Vera, C. (2020). Climate impacts of the El Niño–Southern Oscillation on South America. Nature Reviews Earth & Environment, 1(4), 215-231. [https://par.nsf.gov/servlets/purl/10187393](https://par.nsf.gov/servlets/purl/10187393)

Chiodi, A. M., & Harrison, D. E. (2015). Global seasonal precipitation anomalies robustly associated with El Niño and La Niña events—An OLR perspective. Journal of Climate, 28(15), 6133-6159. [https://www.researchgate.net/publication/277901561_Global_seasonal_precipitation_anomalies_robustly_associated_with_El_Nino_and_La_Nina_events_-_an_OLR_perspective](https://www.researchgate.net/publication/277901561_Global_seasonal_precipitation_anomalies_robustly_associated_with_El_Nino_and_La_Nina_events_-_an_OLR_perspective)

Dahlman, L. (2016). Climate Variability: Oceanic Niño Index. [https://www.climate.gov/news-features/understanding-climate/climate-variability-oceanic-ni%C3%B1o-index](https://www.climate.gov/news-features/understanding-climate/climate-variability-oceanic-ni%C3%B1o-index)

Hasan, E., Tarhule, A., Hong, Y., & Moore, B. (2019). Assessment of physical water scarcity in Africa using GRACE and TRMM satellite data. Remote Sensing, 11(8), 904. [https://pdfs.semanticscholar.org/c240/58013bdb5fb671adeaa2d94ff8289734dc76.pdf](https://pdfs.semanticscholar.org/c240/58013bdb5fb671adeaa2d94ff8289734dc76.pdf)

Jia, Y., Lei, H., Yang, H., & Hu, Q. (2020). Terrestrial Water Storage Change Retrieved by GRACE and Its Implication in the Tibetan Plateau: Estimating Areal Precipitation in Ungauged Region. Remote Sensing, 12(19), 3129. [https://www.researchgate.net/profile/Hanbo-Yang-4/publication/345491380_Terrestrial_Water_Storage_Change_Retrieved_by_GRACE_and_Its_Implication_in_the_Tibetan_Plateau_Estimating_Areal_Precipitation_in_Ungauged_Region/links/5fb4da2545851518fdb0947b/Terrestrial-Water-Storage-Change-Retrieved-by-GRACE-and-Its-Implication-in-the-Tibetan-Plateau-Estimating-Areal-Precipitation-in-Ungauged-Region.pdf](https://www.researchgate.net/profile/Hanbo-Yang-4/publication/345491380_Terrestrial_Water_Storage_Change_Retrieved_by_GRACE_and_Its_Implication_in_the_Tibetan_Plateau_Estimating_Areal_Precipitation_in_Ungauged_Region/links/5fb4da2545851518fdb0947b/Terrestrial-Water-Storage-Change-Retrieved-by-GRACE-and-Its-Implication-in-the-Tibetan-Plateau-Estimating-Areal-Precipitation-in-Ungauged-Region.pdf)

Lin, J., & Qian, T. (2019). A new picture of the Global impacts of el nino-Southern oscillation. Scientific reports, 9(1), 1-7. [https://www.researchgate.net/publication/337543775_A_New_Picture_of_the_Global_Impacts_of_El_Nino-Southern_Oscillation](https://www.researchgate.net/publication/337543775_A_New_Picture_of_the_Global_Impacts_of_El_Nino-Southern_Oscillation)

Long, D., Longuevergne, L., & Scanlon, B. R. (2015). Global analysis of approaches for deriving total water storage changes from GRACE satellites. Water Resour. Res, 51, 3. [https://hal-insu.archives-ouvertes.fr/insu-01137851/document](https://hal-insu.archives-ouvertes.fr/insu-01137851/document)

Muñoz, Á. G., Thomson, M. C., Goddard, L. M., & Aldighieri, S. (2016). The Latin American and Caribbean climate landscape for ZIKV transmission. [https://www.researchgate.net/publication/303471112_The_Latin_American_and_Caribbean_Climate_Landscape_for_ZIKV_Transmission](https://www.researchgate.net/publication/303471112_The_Latin_American_and_Caribbean_Climate_Landscape_for_ZIKV_Transmission)

Ni, S., Chen, J., Wilson, C. R., Li, J., Hu, X., & Fu, R. (2018). Global terrestrial water storage changes and connections to ENSO events. Surveys in Geophysics, 39(1), 1-22. [https://www.researchgate.net/profile/Shengnan-Ni-2/publication/318665950_Global_Terrestrial_Water_Storage_Changes_and_Connections_to_ENSO_Events/links/5be4e8e692851c6b27b12924/Global-Terrestrial-Water-Storage-Changes-and-Connections-to-ENSO-Events.pdf](https://www.researchgate.net/profile/Shengnan-Ni-2/publication/318665950_Global_Terrestrial_Water_Storage_Changes_and_Connections_to_ENSO_Events/links/5be4e8e692851c6b27b12924/Global-Terrestrial-Water-Storage-Changes-and-Connections-to-ENSO-Events.pdf)

Phillips, T., Nerem, R. S., Fox‐Kemper, B., Famiglietti, J. S., & Rajagopalan, B. (2012). The influence of ENSO on global terrestrial water storage using GRACE. Geophysical Research Letters, 39(16). [https://escholarship.org/uc/item/9p53g2p8](https://escholarship.org/uc/item/9p53g2p8)
