---
title: 'Example of SAOCOM processing with ISCE'
author: "Bodo Bookhagen"
author_profile: true
date: 2020-11-08
permalink: /posts/2020/11/SAOCOM-Ifgs-and-ISCE/
toc: true
toc_sticky: true
toc_label: "Example of SAOCOM processing with ISCE"
header:
  overlay_image: https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/SAOCOM_filt_topophase.unw.geo.crop.jpg
  overlay_filter: 0.3 # same as adding an opacity of 0.5 to a black background
  caption: "SAOCOM Interferogram calculated with ISCE"
read_time: false
tags:
  - ISCE
  - InSAR
  - SAOCOM
  - Argentina
  - Central Andes
  - interferogram
  - ionosphere
---

First results from processing interferograms from [SAOCOM](https://en.wikipedia.org/wiki/SAOCOM) - an Argentinean L-band SAR satellite - and [ISCE](https://github.com/isce-framework/isce2).

These outputs here show processing of the sample data from [CONAE](https://www.argentina.gob.ar/ciencia/conae).
Obtain sample data from [CONAE SAOCOM sample data download](https://catalogos.conae.gov.ar/catalogo/catalogoSatSaocomAdel.html). ISCE2.4 includes a reader for SAOCOM and allows to process the slc images (provided by CONAE). We rely on the Interferometric synthetic aperture radar Scientific Computing Environment (ISCE) environment, but processing will work with other InSAR processors as well.
These specific example SAR images are from the National Park El Leoncito (*Parque Nacional El Leoncito*) in the San Juan province.


## Setup config and input files
We generate three files to control the ISCE-run of SAOCOM data:

- XML file controlling the parameters of *stripmapApp.py*
- an XML file containing information about the reference data
- an XML file containing information about the secondary data

*You will need to adjust directories if you are planing to run this on your own ISCE instance.*

**StripmapApp_SAOCOM.xml:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<insarApp>
  <component name="insar">
    <property name="sensor name">SAOCOM_SLC</property>
    <component name="reference">
        <catalog>/home/bodo/Dropbox/Argentina/SAOCOM/reference_SAOCOM.xml</catalog>
    </component>
    <component name="secondary">
        <catalog>/home/bodo/Dropbox/Argentina/SAOCOM/secondary_SAOCOM.xml</catalog>
    </component>
    <property name="demFilename">
        <value>/home/bodo/Dropbox/Argentina/SAOCOM/demLat_S33_S31_Lon_W070_W068.dem.wgs84</value>
    </property>
    <property name="do denseoffsets">True</property>
    <property name="do split spectrum">True</property>
    <property name="unwrapper name">snaphu</property>
    <property name="do dispersive">True</property>
    <property name="dispersive filter kernel x-size">800</property>
    <property name="dispersive filter kernel y-size">800</property>
    <property name="dispersive filter kernel sigma_x">100</property>
    <property name="dispersive filter kernel sigma_y">100</property>
    <property name="dispersive filter kernel rotation">0</property>
    <property name="dispersive filter number of iterations">5</property>
    <property name="dispersive filter mask type">connected_components</property>
    <property name="dispersive filter coherence threshold">0.6</property>

  </component>
</insarApp>
```

**reference_SAOCOM.xml:**
```xml
<component name="reference">
    <property name="IMAGEFILE">
        /raid/InSAR/SAOCOM/Master/67496-EOL1ASARSAO1A515794/Data/slc-acqId0000008546-a-sm7-0000000000-s7dp-vv
    </property>
    <property name="XEMTFILE">
        /raid/InSAR/SAOCOM/Master/67496-EOL1ASARSAO1A515794/S1A_OPER_SAR_EOSSP__CORE_L1A_OLF_20200221T122503.xemt
    </property>
    <property name="XMLFILE">
        /raid/InSAR/SAOCOM/Master/67496-EOL1ASARSAO1A515794/Data/slc-acqId0000008546-a-sm7-0000000000-s7dp-vv.xml
    </property>
    <property name="OUTPUT">
        /raid/InSAR/SAOCOM/Master/67496-EOL1ASARSAO1A515794/slc-acqId0000008546-a-sm7-0000000000-s7dp-vv
    </property>
</component>
```

**secondary_SAOCOM.xml:**
```xml
<component name="reference">
    <property name="IMAGEFILE">
        /raid/InSAR/SAOCOM/Slave/67498-EOL1ASARSAO1A515796/Data/slc-acqId0000010907-a-sm7-0000000000-s7dp-vv
    </property>
    <property name="XEMTFILE">
        /raid/InSAR/SAOCOM/Slave/67498-EOL1ASARSAO1A515796/S1A_OPER_SAR_EOSSP__CORE_L1A_OLF_20200221T122606.xemt
    </property>
    <property name="XMLFILE">
        /raid/InSAR/SAOCOM/Slave/67498-EOL1ASARSAO1A515796/Data/slc-acqId0000010907-a-sm7-0000000000-s7dp-vv.xml
    </property>
    <property name="OUTPUT">
        /raid/InSAR/SAOCOM/Slave/67498-EOL1ASARSAO1A515796/slc-acqId0000010907-a-sm7-0000000000-s7dp-vv.slc
    </property>
</component>
```

## Get SRTM DEM
Make sure to obtain the DEM and download with *dem.py*. Alternatively, this will be automatically downloaded from the NASA ftp page, if you have properly setup permission in ~/.netrc.

We use the DEM: *demLat_S33_S31_Lon_W070_W068.dem.wgs84*.

```
fixImageXml.py -f -i demLat_S33_S31_Lon_W070_W068.dem.wgs84
```

## Additional Preparation steps
Best to uncompress into one folder */raid/InSAR/SAOCOM* and process data there.

# Create Interferogram - Run *stripmapApp.py*

```
cd /raid/InSAR/SAOCOM
stripmapApp.py --steps /home/bodo/Dropbox/Argentina/SAOCOM/stripmapApp_SAOCOM.xml 2>&1 | tee SAOCOM_test.log
```

## Quick views of interferogram and coherence
Use *mdx.py* to create a quick outputs of filtered, unwrapped topophase and coherence (filtered phsig).

```bash
mdx.py -P interferogram/filt_topophase.unw.geo
mv out.ppm SAOCOM_filt_topophase.unw.geo.ppm
convert -density 300 -fuzz 1% -trim SAOCOM_filt_topophase.unw.geo.ppm SAOCOM_filt_topophase.unw.geo.jpg
```

<figure>
    <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/SAOCOM_filt_topophase.unw.geo.jpg"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/SAOCOM_filt_topophase.unw.geo.jpg"></a>
    <figcaption>Filtered and unwrapped SAOCOM interferogram.</figcaption>
</figure>


Same for *phsig.cor.geo*:
```bash
mdx.py -P interferogram/phsig.cor.geo
mv out.ppm SAOCOM_phsig.cor.geo.ppm
convert -density 300 -fuzz 1% -trim SAOCOM_phsig.cor.geo.ppm SAOCOM_phsig.cor.geo.jpg
```

<figure>
    <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/SAOCOM_phsig.cor.geo.jpg"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/SAOCOM_phsig.cor.geo.jpg"></a>
    <figcaption>Filtered coherence calculation using the phsig output.</figcaption>
</figure>

Generate quick view shown in banner of this page using imagemagick *convert*:
```bash
convert -density 300 -crop 2000x400+0+1000 +repage SAOCOM_filt_topophase.unw.geo.jpg SAOCOM_filt_topophase.unw.geo.crop.jpg
```

## Quick views of ionospheric impact
Using split-spectrum processing included in ISCE (see [paper by Heresh Fattahi et al.](https://ieeexplore.ieee.org/document/7987747) and for C-band the [paper by Cunren Liang et al.](https://ieeexplore.ieee.org/document/8706258?source=authoralert)), we can estimate the dispersive and non-dispersive components of the ionosphere and correct the interferogram. We note that this specific SAOCOM example contains some ionospheric disturbances.


<figure>
    <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/iono_dispersive.bil.unwCor.filt.geo.jpg"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/iono_dispersive.bil.unwCor.filt.geo.jpg"></a>
    <figcaption>Ionospheric component (dispersive), unwrapped and filtered data. .</figcaption>
</figure>


<figure>
    <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/iono_nondispersive.bil.unwCor.filt.geo.jpg"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/iono_nondispersive.bil.unwCor.filt.geo.jpg"></a>
    <figcaption>Ionospheric component (non-dispersive), unwrapped and filtered data. Color Scale equals to dispersive ionospheric component shown above.</figcaption>
</figure>
