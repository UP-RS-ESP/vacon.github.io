---
title: 'Miniconda Environments Oct 2020'
layout: archive
date: 2020-10-18
permalink: /posts/2020/10/conda-install/
author_profile: true
author: "Bodo Bookhagen"
classes: wide
read_time: false
toc: true
toc_label: "Conda Installation"
-- tags:
  - conda
  - installation
  - setup
---

Update on [Conda Install](https://up-rs-esp.github.io/posts/2018/12/conda-install/).

## Installation on Linux
This is a Python 3.x code that will run on any OS, which supports the packages. It runs and has been tested on Linux (Ubuntu/Debian), Windows 10, and Mac OS X. We are using [conda/miniconda](https://conda.io/docs/) to install the required packages, which can be [downloaded here](https://conda.io/miniconda.html). Follow [these instruction](https://conda.io/docs/user-guide/install/index.html) to get miniconda installed. In short:
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

# Installing environments
It is useful to install different environments for different purposes. Here is a list of useful environments with different purposes:
For some of these examples, you want to add:
```bash
conda config --prepend channels conda-forge/label/dev
conda config --prepend channels conda-forge
```

Or in order to reset the channel list
```bash
conda config --prepend channels defaults
```

| What for? | Conda commands |
|:---------:|:--------------|
| GMT 5 and Python Processing |```conda create -y -n gmt5 gmt=5* python=3* scipy pandas numpy matplotlib scikit-image gdal spyder imagemagick``` |
| GMT 6 and Python Processing |```conda create -y -n gmt6 gmt=6* python=3* scipy pandas numpy matplotlib scikit-image gdal spyder imagemagick``` |
| PointCloud Processing Python 3.8 | ```conda create -y -n PC_py3 -c anaconda -c conda-forge -c defaults ipython spyder python=3.8 gdal=3 numpy scipy dask h5py pandas pytables hdf5 cython matplotlib tabulate scikit-learn pykdtree pyflann cyflann scikit-image opencv ipywidgets scikit-learn gmt=6*  imagemagick``` <br> Activate the environment ```conda activate PC_py3``` <br> and install laspy with ```pip install laspy``` and tables ```pip install tables```|
| PointCloud Processing Python 3.6 | ```conda create -y -n PC_py36 -c anaconda -c conda-forge -c defaults python=3.6 pip scipy pandas numpy matplotlib scikit-image gdal pdal xarray packaging ipython multiprocess h5py lastools pykdtree spyder gmt=6* imagemagick``` <br> Activate the environment ```conda activate PC_py36``` <br> and install laspy with ```pip install laspy``` and tables ```pip install tables```|
| DEM processing Python 3.8 | ```conda create -y -n DEM_py3 -c anaconda -c conda-forge -c defaults python=3.8 pip scipy pandas numpy matplotlib scikit-image gdal=3 ipython spyder statsmodels jupyter pyproj gmt=6*``` <br> Activate the environment ```conda activate DEM_py3``` <br> and install additional packages with ```conda install -y -c conda-forge richdem landlab``` |
| CUDA 10.2 PointCloud Processing | ```conda create -y -n PC_cudf -c rapidsai-nightly -c nvidia -c anaconda -c conda-forge -c defaults  ipython spyder python=3.8 rapids=0.16 cudatoolkit=10.2 cuspatial gdal=3 numpy scipy dask h5py pandas pytables hdf5 cython matplotlib tabulate scikit-learn pyflann cyflann scikit-image opencv ipywidgets scikit-learn laszip liblas``` <br> Activate the environment ```conda activate PC_cudf``` <br> and install additional packages with ```pip install laspy``` and tables ```pip install tables```|
| CUDA 11.0 PointCloud Processing | ```conda create -y -n PC_cudf -c rapidsai-nightly -c nvidia -c anaconda -c conda-forge -c defaults  ipython spyder python=3.8 rapids=0.16 cudatoolkit=11.0 cuspatial gdal=3 numpy scipy dask h5py pandas pytables hdf5 cython matplotlib tabulate scikit-learn pyflann cyflann scikit-image opencv ipywidgets scikit-learn laszip liblas``` <br> Activate the environment ```conda activate PC_cudf``` <br> and install additional packages with ```pip install laspy``` and tables ```pip install tables```|



<script type="text/javascript"> DiscourseEmbed = { discourseUrl: 'https://discourse.up-rs-esp-3.geo.uni-potsdam.de/', discourseEmbedUrl: 'https://up-rs-esp.github.io/conda/' };
(function() { var d = document.createElement('script'); d.type = 'text/javascript'; d.async = true; d.src = DiscourseEmbed.discourseUrl + 'javascripts/embed.js'; (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(d); })(); </script>



