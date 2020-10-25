---
title: 'NVIDIA CUDA Install on Ubuntu 18.04 / 20.04'
layout: archive
date: 2020-10-19
permalink: /posts/2020/10/CUDA-install-ubuntu/
author_profile: true
author: "Bodo Bookhagen"
classes: wide
read_time: false
toc: true
toc_label: "CUDA Installation"
-- tags:
  - Ubuntu
  - CUDA
  - NVIDIA
---

CUDA processing has become an integral part of data-intensive processing. Installation is still cumbersome and changes when new versions become available.
 There are several resources available on the net that guide you through the installation procedure - all tailored at different purposes. First and foremost, you should look at the official [NVIDIA Documentation](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html).

**The following installation procedure is tailored at Ubuntu 18.04 and 20.04.**

I advise to manually install the CUDA driver - especially if you are on a compute node and don't need the CUDA display drivers. Otherwise the system may become unstable with an automatic driver update and may result in nvcc incompatibility.

## General steps to install CUDA Drivers and Toolkits on Ubuntu Systems
It is best to install the CUDA 10.2/11.0 drivers directly from the [NVIDIA webpage](https://developer.nvidia.com/cuda-11.0-download-archive). On Ubuntu 18.04 we use CUDA 10.2, because 18.04 still runs with GCC v8 and on Ubuntu 20.04 we use CUDA 11.0 (GCC v9). By updating your GCC environment, you can also run 11.0 on Ubuntu 18.04. We have not noticed any differences between the versions.

1. **Deinstall all NDVIDIA repository drivers.** `sudo apt-get purge nvidia-*`. If (for some reason) you want to keep the drivers, use `sudo apt-get purge nvidia-cuda*`.
2. **Download CUDA drivers** from the [NVIDIA webpage](https://developer.nvidia.com/cuda-downloads). For Ubuntu 18.04 use [Download 10.2](https://developer.nvidia.com/cuda-10.2-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=runfilelocal) or
```wget http://developer.download.nvidia.com/compute/cuda/10.2/Prod/local_installers/cuda_10.2.89_440.33.01_linux.run```
and the [Patch 10.2 Aug-26 2020](http://developer.download.nvidia.com/compute/cuda/10.2/Prod/patches/1/cuda_10.2.1_linux.run) with ```wget http://developer.download.nvidia.com/compute/cuda/10.2/Prod/patches/1/cuda_10.2.1_linux.run```. For Ubuntu 20.04 use [Download 11.0](https://developer.nvidia.com/cuda-11.0-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=2004&target_type=runfilelocal) or ```wget http://developer.download.nvidia.com/compute/cuda/11.0.2/local_installers/cuda_11.0.2_450.51.05_linux.run```
3. **Before Installation** If you are using the NVIDIA card also for the X Server, you have to turn off the xserver. You can simply switch to the console with Ctrl-Alt-F2, logging in and turning off the xserver with `sudo init 3` or in some cases you can use `sudo service lightdm stop`. For compute-only servers, you should not be running an X Server.
4. **Install the driver** with (here for 10.2. Make sure you are root (`sudo -i`): ```sh ./cuda_10.2.89_440.33.01_linux.run```. Apply patch ```sh ./cuda_10.2.1_linux.run```.
5. You want to add the binary directory to you PATH variable: `export PATH=$PATH:/usr/local/cuda-10.2/bin`.
6. Make sure that `/usr/local/cuda-10.2/lib64` is either in LD_LIBRARY PATH with `export LD_LIBRARY PATH=$LD_LIBRARY PATH:/usr/local/cuda-10.2/lib64` or add /usr/local/cuda-10.2/lib64 to /etc/ld.so.conf: `echo /usr/local/cuda-10.2/lib64 > /etc/ld.so.conf.d/cuda.conf` and run `ldconfig`
7. Reboot (`sudo reboot`). You should now run a fairly recent NDVIDIA driver (440.33) and also should have all nvidia tools installed.
8. Verify by running `nvcc --version` and `nvidia-smi`.

With `nvidia-smi` you should see something along these lines (system _aconcagua_):
```
Sun Oct 18 07:36:33 2020       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 440.33.01    Driver Version: 440.33.01    CUDA Version: 10.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla V100-PCIE...  Off  | 00000000:3B:00.0 Off |                    0 |
| N/A   35C    P0    34W / 250W |      0MiB / 32510MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   1  Tesla V100-PCIE...  Off  | 00000000:AF:00.0 Off |                    0 |
| N/A   35C    P0    36W / 250W |      0MiB / 32510MiB |      4%      Default |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```

or on system _kailash_:
```
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 440.33.01    Driver Version: 440.33.01    CUDA Version: 10.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla P40           Off  | 00000000:02:00.0 Off |                    0 |
| N/A   26C    P0    51W / 250W |      0MiB / 22919MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   1  Tesla P40           Off  | 00000000:83:00.0 Off |                    0 |
| N/A   26C    P0    47W / 250W |      0MiB / 22919MiB |      3%      Default |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```
