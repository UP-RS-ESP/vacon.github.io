# Install Spatial Data Analysis (SDA) relevant environment
```bash
conda create -y -n SDA python=3.10 pip scipy pandas numpy matplotlib scikit-image gdal ipython statsmodels jupyter pyproj lastools pdal pykdtree h5py plotly seaborn pytables pdal python-pdal scikit-learn jupyterlab numba jupyter-resource-usage geopandas rasterio xarray dask netCDF4 bottleneck lmfit xlrd -c conda-forge
conda activate SDA
pip install open3d laspy laszip jakteristics structure_tensor
```
This should install open3d-0.17.x. or newer.

You can additionally install `spyder` if required.

Make sure to add your conda environment to the Jupyter Notebook environment:
```bash
conda activate SDA
python -m ipykernel install --user --name=SDA
```

# Install Mintpy
```bash
conda create -n mintpy -c conda-forge
conda activate mintpy
conda install -c conda-forge mintpy
```
