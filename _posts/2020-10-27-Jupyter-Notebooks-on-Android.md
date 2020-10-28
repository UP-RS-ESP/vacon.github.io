---
title: 'Running Jupyter Notebooks on a Android tablet'
layout: archive
date: 2020-10-27
permalink: /posts/2020/10/Jupyter-Notebooks-on-Android/
author_profile: true
author: "Bodo Bookhagen"
read_time: false
toc: true
toc_label: "Jupyter Notebooks on Android"
-- tags:
  - Android
  - Jupyter Notebook
  - Python
  - Galaxy
  - teaching
---
Connect your keyboard to your tablet and get ready to run *Jupyter Notebooks* on Android systems!

Jupyter Notebooks provide a great learning and coding environment. For serious coding and data processing, you most likely would like to have access to powerful computing resources - not always provided by tablets. However, many times you are developing and would like to continue fine tuning and debugging existing code - that's where Jupyter Notebooks on tablets come in very handy. Here, we briefly describe setting up an environment on Android systems using PyDroid, but there are other options to run Notebooks, too.

Running Jupyter Notebooks on tablets is often sufficient for teaching purposes. But you definitely want to have an external keyboard (Bluetooth keyboard) and mouse. You can also hook up a monitor and use your Android tablet as a substitute for a laptop. With that setup, you can also remotely connect to existing ipython kernels and Jupyter Notebook instances that run on much more powerful hardware (network connection is required).

Setup is easy and straightforward. On Android (here we use an Samsung Galaxy S6) download [PyDroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3&hl=en_US&gl=US) and look at the following steps:

<figure>
    <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/weylus1.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/Pydroid0_install.jpg"></a>
    <figcaption>Get PyDroid 3 from the Play Store (here the German Play Store is shown). </figcaption>
</figure>

Next, you can start using *pip* to install packages for your coding experience, just like on a PC. Pydroid 3 comes with an interface that allows you to install packages by selecting *pip* in the menu. In addition to Jupyter Notebook, you should install all the packages you would like to use (*scipy*, *numpy*, *pandas*, ...)

<p float="middle">
<img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/Pydroid1_run_terminal_pip.jpg" width="45%"/>
<img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/Pydroid2_pip_install_jupyter.jpg" width="45%"/>
</p>


After successful installation, you start *jupyter notebook* from the terminal from the menu (type `jupyter notebook`). You also should set a password for your notebooks or use the provided token to use other web browsers. An example Notebook running *pandas* is shown below.

<p float="middle">
<img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/Pydroid3_run_jupyter.jpg" width="45%"/>
<img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/Pydroid4_Pandas.jpg" width="45%"/>
</p>

**Happy coding!**
