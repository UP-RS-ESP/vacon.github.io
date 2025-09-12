#!/bin/bash

. /home/bodo/miniconda3/etc/profile.d/conda.sh
conda activate py310

cd /raid/nwarg/vacon.github.io/ClimData/
python3 /raid/nwarg/vacon.github.io/ClimData/codes/read_meteorologic_data.py /raid/nwarg/vacon/clim_data/qt01/ "La Paya" 01_LaPaya /raid/nwarg/vacon.github.io/ClimData/

cd /raid/nwarg/vacon.github.io/ClimData/
python3 /raid/nwarg/vacon.github.io/ClimData/codes/read_meteorologic_data.py /raid/nwarg/vacon/clim_data/qt02/ "Rosaria de Lerma" 02_RosariodeLerma /raid/nwarg/vacon.github.io/ClimData/

cd /raid/nwarg/vacon.github.io/ClimData/
python3 /raid/nwarg/vacon.github.io/ClimData/codes/read_meteorologic_data.py /raid/nwarg/vacon/clim_data/qt03/ "Cafayate" 03_Cafayate /raid/nwarg/vacon.github.io/ClimData/

cd /raid/nwarg/vacon.github.io/ClimData/
python3 /raid/nwarg/vacon.github.io/ClimData/codes/read_meteorologic_data.py /raid/nwarg/vacon/clim_data/qt04/ "Angastaco" 04_Angastaco /raid/nwarg/vacon.github.io/ClimData/

cd /raid/nwarg/vacon.github.io/ClimData/
python3 /raid/nwarg/vacon.github.io/ClimData/codes/read_meteorologic_data.py /raid/nwarg/vacon/clim_data/qt05/ "La Poma" 05_LaPoma /raid/nwarg/vacon.github.io/ClimData/

cd /raid/nwarg/vacon.github.io/ClimData/
python3 /raid/nwarg/vacon.github.io/ClimData/codes/read_meteorologic_data.py /raid/nwarg/vacon/clim_data/qt06/ "Santa Maria" 06_SantaMaria /raid/nwarg/vacon.github.io/ClimData/

cd /raid/nwarg/vacon.github.io/ClimData/
python3 /raid/nwarg/vacon.github.io/ClimData/codes/read_meteorologic_data.py /raid/nwarg/vacon/clim_data/qt07/ "Las Cardones" 07_LosCardones /raid/nwarg/vacon.github.io/ClimData/

cd /raid/nwarg/vacon.github.io/ClimData/
python3 /raid/nwarg/vacon.github.io/ClimData/codes/read_meteorologic_data.py /raid/nwarg/vacon/clim_data/qt08/ Alfarcito 08_Alfarcito /raid/nwarg/vacon.github.io/ClimData/

cd /raid/nwarg/vacon.github.io/ClimData/
python3 /raid/nwarg/vacon.github.io/ClimData/codes/read_meteorologic_data.py /raid/nwarg/vacon/clim_data/qt09/ "San Antonio de los Cobres" 09_SAdelosCobres /raid/nwarg/vacon.github.io/ClimData/

cd /raid/nwarg/vacon.github.io/ClimData/
python3 /raid/nwarg/vacon.github.io/ClimData/codes/read_meteorologic_data.py /raid/nwarg/vacon/clim_data/qt10/ "Tolar Grande" 10_TolarGrande /raid/nwarg/vacon.github.io/ClimData/

cd /raid/nwarg/vacon.github.io/ClimData/
python3 /raid/nwarg/vacon.github.io/ClimData/codes/read_meteorologic_data.py /raid/nwarg/vacon/clim_data/qt11/ "Salar Llullaillaco" 11_SalarLlullaillaco /raid/nwarg/vacon.github.io/ClimData/

cd /raid/nwarg/vacon.github.io/ClimData/
python3 /raid/nwarg/vacon.github.io/ClimData/codes/read_meteorologic_data.py /raid/nwarg/vacon/clim_data/qt12/ "San Jose de Metan" 12_Metan /raid/nwarg/vacon.github.io/ClimData/

