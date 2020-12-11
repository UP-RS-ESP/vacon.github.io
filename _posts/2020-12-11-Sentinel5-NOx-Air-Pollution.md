---
title: 'Causes of reduction in airborne NO<sub>2</sub> and CO emissions in Europe during COVID-19 crisis'
author: "Bashini Mahaarachchi"
supervisors: "Prof. Dr. Bodo Bookhagen and Dr. Taylor Smith"
date: 2020-12-10
toc: true
toc_sticky: true
toc_label: "Causes of reduction in airborne NO<sub>2</sub> and CO emissions in Europe during COVID-19 crisis"
header:
overlay_image: https://raw.githubusercontent.com/Bashinim/COVID19-EU/main/Cropped%20Images/Background.jpg
  overlay_filter: 0.3
  caption: "Causes of reduction in airborne NO<sub>2</sub> and CO emissions in Europe during COVID-19 crisis"
read_time: false
---

The most presumed causes of reduction in observed reduction in air pollution are reduction in surface traffic and people staying at home due to the travel bans imposed. In this analysis changes of NO<sub>2</sub> and CO emissions are compared against the three variables:

- The average population in Europe
- Road density in Europe
- Vessel routes density in the Mediterranean Sea and the black sea

### Main air pollutants and their sources in Europe

<a href="https://www.eea.europa.eu/publications/air-quality-in-europe-2019">EEA’s Air Quality 2019 report </a> illustrates the total emissions of pollutants in the EU-28, indexed as a percentage of their value in the reference year 2000. This report further gives an overview of each sector’s contribution to total emissions for all chosen pollutants in the EU-28, for 2017.


<a href="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.2.1.jp?raw=true"><img src="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.2.1.jpg?raw=true"></a>
    <figcaption>Trends in EU-28 emissions, 2000-2017 (as a % of 2000 levels): SO<sub>x</sub>, NO<sub>x</sub>, NH<sub>3</sub>, PM<sub>10</sub>, PM<sub>2.5</sub>, NMVOCs, CO, CH<sub>4</sub> and BC. Also for comparison EU-28 gross domestic product (GDP) is shown (GDP, expressed in chain linked volumes as a % of 2000 level. This shows that there were fewer emissions for each unit of GDP produced per year consecutively.  </figcaption>
    </figure> </center>

<a href="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.2.2.jpg?raw=true"><img src="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.2.2.jpg?raw=true"></a>
    <figcaption>Contribution to EU-28 emissions from the main source sectors in 2017 of SO<sub>x</sub>, NO<sub>x</sub>, primary PM<sub>10</sub>, primary
PM<sub>2.5</sub>, NH<sub>3</sub>, NMVOCs, CO, BC and CH<sub>4</sub>. The road transport sector was the most significant contributor to total NO<sub>x</sub> (nitrogen oxides is a generic term for the mono-nitrogen oxides NO and NO<sub>2</sub>) emissions and the second largest contributor for NO<sub>2</sub> emissions was the energy production and distribution sector. The highest and 50% contributor to total CO emissions was the commercial, institutional and households sector and the second largest contributor to total CO emissions was the transport sector. </figcaption>
    </figure> </center>

The contributions from different emission source sectors to air pollutant concentrations and air pollution impacts depend not only on the amount of pollutants emitted but also on the proximity to the source, emission/dispersion conditions and other factors such as topography. Emission sectors with low emission heights, such as traffic and household emissions, generally make larger contributions to surface concentrations and health impacts in urban areas than emissions from high stacks.


### Processing candidate variables

<center>
<figure>
    <a href="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/1.annex.jpg?raw=true"><img src="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/1.annex.jpg?raw=true"></a>
    <figcaption>The estimated average number of persons for a square kilometer in 2020 in Europe [<a href = "https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_Basic_Demographic_Characteristics">NASA SEDAC at the Center for International Earth Science Information Network</a>].  </figcaption>
    </figure> </center>

<a href="https://yadi.sk/d/Vnwc4kut3LCBFm?raw=true">OpenStreetMap Europe data</a> was used to extract the road network of Europe. First, the ".pbf" file was split into sub-parts using <a href="https://yadi.sk/d/Vnwc4kut3LCBFm?raw=true">OSM converter</a>, with the option; <b>  using a border-box to limit the geographical region. </b> Then the linestring geometries of the split files were filtered and the ".pbf" file was converted to a GeoJSON using <a href="https://yadi.sk/d/Vnwc4kut3LCBFm?raw=true">GDAL.</a>

```bash
#UK is the name of a single .pbf file that was split before and 'lines' at the end instructs GDAL to extract only the line geometries from the file.
ogr2ogr -f GeoJSON UK.json UK.pbf lines
```

Then these datasets were merged in Python, in a way that the final dataset doesn’t have duplicated roads because of the clipping boundaries considered. Each distinctive road is identified by a unique ‘Osm id’.

<center>
<figure>
    <a href="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.3.1.jpg?raw=true"><img src="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.3.1.jpg?raw=true"></a>
    <figcaption>Road network of Europe extracted from OSM data; the highways tagged as a motorway, trunk, primary,
secondary, tertiary, unclassified, and residential in OSM [<a href = "https://zenodo.org/record/4284076#.X8VIHbMo_IW">Processed dataset</a>].  </figcaption>
    </figure> </center>

Next, the road densities and the vessel densities of geolocation points used to create the pollutant gas maps and population maps were calculated.
The number of roads passing through a 7 km radius from each of these points was calculated using Rtree spatial joins
and spatial index, in python.

```bash
#Defining radius as 7 km (7km ≈ 0.063063̇°).
Radius = 0.063063

#Adding this buffer to all geolocation points (grided points)
grid_df['geometry'] = grid_df.geometry.buffer(Radius)

#Importing Geopands as gpd
import geopandas as gpd

#Taking the spatial joins of the two data frames created above (grid_df has point geometries as the geometry and roads_df has Linestring geometries as the geometry.)
grided_roads = gpd.sjoin(grid_df, roads_df, how='inner', op='intersects')

#Taking the sum of roads crossing the boundary of each buffered point.
roads_num_df = grided_roads.groupby('Point_ID').size().reset_index()

```

<center>
<figure>
    <a href="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.2.jpg?raw=true"><img src="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.2.jpg?raw=true"></a>
    <figcaption>Road density of Europe; the number of roads within a 7 km radius from each considered geolocation point. Each
distinctive road is identified by a unique ‘Osm id’. </figcaption>
    </figure> </center>

<center>

<figure>
    <a href="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.1.jpg?raw=true"><img src="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.1.jpg?raw=true"></a>
    <figcaption>Vessel routes density in the Mediterranean Sea and the Black Sea; the number of vessel routes within 7 km radius from each
considered geolocation point. Each distinctive route is identified by a unique ‘Osm id’.   </figcaption>
    </figure> </center>


### Processing air pollution variables

In this analysis, the time between 1<sup>st</sup> of March 2020 to 31<sup>st</sup> of April 2020 is considered as the time where strict
confinement policies were applied across Europe, thus as the <b>‘lock-down period’</b>.

The following three variables are used to indicate the changes in  NO<sub>2</sub> and CO emissions. Data was preprocessed in Google Earth Engine (GEE) Code editor and further analysis was done with python.

- Average NO<sub>2</sub> and CO emissions during Covid-19 in Europe
- The slope of the time series change of NO<sub>2</sub> and CO emissions during the lock-down period
- Percentage change of NO<sub>2</sub> and CO emissions during the lock-down period compared to the average values of the previous year in the same period

Two videos below show the weekly average NO<sub>2</sub> and CO emissions from 1<sup>st</sup> of January to 31<sup>st</sup> of July 2020. Areas with no data values are displayed in black colour. Codes used to create the videos can be found here [<a href="https://code.earthengine.google.com/a968bd2c8a502ccba6a6af3dfc4f0eb6?noload=true">NO<sub>2</sub></a>,<a href="https://code.earthengine.google.com/c3e02c47cf15255a0f61baa9744fbe94?noload=true"> CO</a>].

<center>
<figure>
    <a href="https://drive.google.com/file/d/1Lp6GMMKtILuKKBBwf0gmqFnctCxwIJ39/view?usp=sharing"><img src="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/NO2_weekly_average.gif?raw=true"></a>
    <figcaption>Weekly average NO<sub>2</sub> emissions of Europe from 1<sup>st</sup> of January to 31<sup>st</sup> of July 2020, measured in mol/m<sup>2</sup>.  </figcaption>
    </figure> </center>

<center> <figure>
    <a href="https://drive.google.com/file/d/1D4hfbxcE7bk2suDp2b_2ocJLfKrU6Xkn/view?usp=sharing"><img src="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/CO_weekly_average.gif?raw=true"></a>
    <figcaption>Weekly average CO emissions of Europe from 1<sup>st</sup> of January to 31<sup>st</sup> of July 2020, measured in mol/m<sup>2</sup>.  </figcaption>
    </figure> </center>


<figure>
    <a href="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.4.jpg?raw=true"><img src="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.4.jpg?raw=true"></a>
    <figcaption>Mean NO<sub>2</sub> emission volumes during the lock-down period, during the previous two months and the same maps
for 2019 emissions. The emission volumes have dropped significantly compared to the 2019 levels in all of the areas in Europe during the first two months of the year, except in Milan and Turin in Italy. During the lock-down period, NO<sub>2</sub> emissions have dropped in these two cities as well. </figcaption>
    </figure> </center>


<figure>
    <a href="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.5.jpg?raw=true"><img src="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.5.jpg?raw=true"></a>
    <figcaption>Mean CO emission volumes during the lock-down period, during the previous two months and the same maps for 2019 emissions. The last two maps show the difference in CO mean values of the two periods in 2019 and 2020 respectively. Difference maps show reductions in Europe wide CO emissions in each following month. </figcaption>
    </figure> </center>


<center><figure>
    <a href="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.6.jpg?raw=true"><img src="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.6.jpg?raw=true"></a>
    <figcaption>The slope of NO<sub>2</sub> emission data during the lock-down period. Negative slopes indicate reductions in NO<sub>2</sub> emission volumes and positive slopes indicate
increases in NO<sub>2</sub> emission volumes. </figcaption>
    </figure> </center>


<center><figure>
    <a href="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.7.jpg?raw=true"><img src="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.7.jpg?raw=true"></a>
    <figcaption>The slope of CO emission data during the lock-down period. Negative slopes indicate reductions in CO emission volumes and positive slopes indicate increases in CO emission volumes. </figcaption>
    </figure> </center>


<center><figure>
    <a href="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.10.jpg?raw=true"><img src="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.10.jpg?raw=true"></a>
    <figcaption>Percentage change of average NO<sub>2</sub> emissions during the lock-down period compared to the previous year. Percentages less than zero indicate reductions in NO<sub>2</sub> emission volumes and percentages greater than zero indicate increases in NO<sub>2</sub> emission volumes compared to
the average values of the previous year in the same period.</figcaption>
    </figure> </center>


<center><figure>
    <a href="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.11.jpg?raw=true"><img src="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.11.jpg?raw=true"></a>
    <figcaption>Percentage change of average CO emissions during the lock-down period compared to the previous year. Percentages less than zero indicate reductions in CO emission volumes and percentages greater than zero indicate increases in CO emission volumes compared to
the average values of the previous year in the same period.</figcaption>
    </figure> </center>

<center><figure>
    <a href="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.13.jpg?raw=true"><img src="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.13.jpg?raw=true"></a>
    <figcaption>Mean NO<sub>2</sub> and CO emission volumes over the vessel routes in the Mediterranean Sea and the Black Sea during the lock-down period. </figcaption>
    </figure> </center>

<center><figure>
    <a href="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.12.jpg?raw=true"><img src="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.12.jpg?raw=true"></a>
    <figcaption>The slope of NO<sub>2</sub> and CO emissions over the vessel routes in the Mediterranean Sea and the Black Sea during the lock-down period. Negative slopes of NO<sub>2</sub> emission in the
coastal areas in the Mediterranean Sea indicate reductions in NO<sub>2</sub> emission in these areas.</figcaption>
    </figure> </center>

<center><figure>
    <a href="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.14.jpg?raw=true"><img src="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.14.jpg?raw=true"></a>
    <figcaption>Percentage change average of NO<sub>2</sub> and CO emission volumes over the vessel routes in the Mediterranean Sea and the Black Sea during the lock-down period compared to the previous year's same time period.</figcaption>
    </figure> </center>

### Assessing the relationships


<center><figure>
    <a href="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/T.4.1.jpg?raw=true"><img src="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/T.4.1.jpg?raw=true"></a>
    <figcaption>Correlation statistics between emission variables and road density, vessel routes density and population density. Mean CO and NO<sub>2</sub> are measured
in mol/m<sup>2</sup> and road density and vessel density are measured in the number of roads/number of vessel routes within a 7 km
radius from each geolocation point. Population density is measured as the number of people living in a 7 km radius from
each geolocation point.</figcaption>
    </figure> </center>

Road density has the highest correlation with the pollutant gas variables. All three candidate variables have the highest correlation with the ‘Mean NO<sub>2</sub> volume’ compared to other emission variables.‘Percentage change of NO<sub>2</sub>’ has the next highest correlation with all three candidate variables and they are negative because as expected the NO<sub>2</sub> emissions are lower during the lock-down period than in the previous year. In places where there is a high traffic density or a high population density, reduced NO<sub>2</sub> emission volumes are observed.‘Slope of NO<sub>2</sub> volume’ has the next highest correlation with the candidate variables and these correlation statistics are negative. ‘Slope of NO<sub>2</sub> volume’ and the three candidate variables together provide the best explanation for the
reduction of NO<sub>2</sub> emissions during the lock-down period because the slope (coefficient of linear time series trend of air pollutants) during the lock-down period is a measurement that shows how rapidly the emission volumes have dropped
during the lock-down.


### Time series analysis

<center><figure>
    <a href="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.28.jpg?raw=true"><img src="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.28.jpg?raw=true"></a>
    <figcaption>NO<sub>2</sub> emission time series change in Lisbon-Portugal, Madrid-Spain and Roam-Italy, and RD of these places. NO<sub>2</sub> emissions have dropped significantly during the lock-down period in all these places. Volumes start to drop from mid March and start to increase again in late May.</figcaption>
    </figure> </center>

<center><figure>
    <a href="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.30.jpg?raw=true"><img src="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.30.jpg?raw=true"></a>
    <figcaption>NO<sub>2</sub> emission time series and the smoothened series change in Barcelona-Spain, Venice-Italy and ˙Istanbul-
Turkey, and VD of these places. NO<sub>2</sub> emissions have dropped significantly during the lock-down period in all these places. Similar to the above figure, this drop has also started in mid March but it continues until the end of July with some irregular spikes in between.</figcaption>
    </figure> </center>


<center><figure>
    <a href="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.29.jpg?raw=true"><img src="https://github.com/Bashinim/COVID19-EU/blob/main/Cropped%20Images/F.4.29.jpg?raw=true"></a>
    <figcaption>CO emission time series change and the smoothened series in Ilford-United Kingdom, Barcelona-Spain and Frederiksberg-Denmark, and PD of these places. CO emission has increased during the lock-down period in all these places. The emission volumes have started decreasing again from early May.</figcaption>
    </figure> </center>



### Key takeaways


- Road traffic reduction has been the primary cause of the reduction in NO<sub>2</sub> emissions during the lock-down period in Europe.

- The places that have higher drops in NO<sub>2</sub> volumes during the confinement period have higher road, vessel and population densities.

- Road, vessel and population density data do not provide strong reasoning for the reduction in CO emissions due to two reasons:

	1. CO is a highly dispersing gas, and therefore, it might not be a good approach to compare the geographical location of the sensed CO gas and its sources

	1. People staying at home during lock-down could have created events that have both positive and negative effects on changes in CO emission levels.

- It would add further insights to this analysis if the locations of the industries that contribute to a high level of NO<sub>2</sub> and CO emissions in Europe could be checked against the changes in CO and NO<sub>2</sub> emission levels in these locations during the lock-down period because 50% of the CO emissions and 8% of NO<sub>2</sub> emissions are coming from commercial
institutions.


<script type="text/javascript"> DiscourseEmbed = { discourseUrl: 'https://discourse.up-rs-esp-3.geo.uni-potsdam.de/', discourseEmbedUrl: 'https://up-rs-esp.github.io//posts/2020/12/Sentinel5-NOx-Air-Pollution' };
(function() { var d = document.createElement('script'); d.type = 'text/javascript'; d.async = true; d.src = DiscourseEmbed.discourseUrl + 'javascripts/embed.js'; (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(d); })(); </script>
