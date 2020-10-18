---
title: 'RAPIDS.AI Install on Ubuntu'
layout: archive
date: 2020-10-19
permalink: /posts/2020/10/RAPIDS-install-ubuntu/
author_profile: true
author: "Bodo Bookhagen"
classes: wide
read_time: false
toc: true
toc_label: "RAPIDS Installation"
-- tags:
  - Ubuntu
  - CUDA
  - NVIDIA
  - cudf
  - CUDA Data Frame
  - cuspatial
---

There are different software packages available for using NVIDIA CUDA/OPENCL architectures. In addition to Google-supporeted [Tensorflow](https://www.tensorflow.org/) and other packages, [RAPIDS.AI]()(https://rapids.ai/) is a useful open GPU environment. Installation has become more straight forward (after you setup your [CUDA NDVIDIA drivers](/posts/2020/10/CUDA-install-ubuntu/))
RAPIDS has useful and well maintained [documentation](https://docs.rapids.ai/) and [Jupyter Notebooks](https://github.com/rapidsai/notebooks) (for example, see [Jupyter Notebooks for Machine Learning](https://github.com/rapidsai/cuml/tree/branch-0.16/notebooks)).

# Installation
Follow [conda package selection](https://rapids.ai/start.html#get-rapids) for a pure rapids installation.

In order to install an environment useful for **point cloud processing**, use one of the following.

## CUDA 10.2 PointCloud Processing (Ubuntu 18.04)

```
conda create -y -n PC_cudf -c rapidsai-nightly -c nvidia -c anaconda -c conda-forge -c defaults \
  ipython spyder python=3.8 rapids=0.16 cudatoolkit=10.1 cuspatial gdal=3 numpy scipy dask h5py pandas \
  pytables hdf5 cython matplotlib tabulate scikit-learn pyflann cyflann scikit-image opencv ipywidgets \
  scikit-learn laszip liblas
```

Activate the environment `conda activate PC_cudf` and install additional packages with `pip install laspy` and tables `pip install tables`

## CUDA 11.0 PointCloud Processing (Ubuntu 20.04)

```
conda create -y -n PC_cudf -c rapidsai-nightly -c nvidia -c anaconda -c conda-forge -c defaults \
  ipython spyder python=3.8 rapids=0.16 cudatoolkit=11.0 cuspatial gdal=3 numpy scipy dask h5py pandas \
  pytables hdf5 cython matplotlib tabulate scikit-learn pyflann cyflann scikit-image opencv ipywidgets \
  scikit-learn laszip liblas
```

Activate the environment `conda activate PC_cudf` and install additional packages with `pip install laspy` and tables `pip install tables`
