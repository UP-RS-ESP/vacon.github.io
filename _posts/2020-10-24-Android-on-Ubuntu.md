---
title: 'Using an Samsung Galaxy with Android as Whiteboard'
layout: archive
date: 2020-10-24
permalink: /posts/2020/10/Android-as-Whiteboard/
author_profile: true
author: "Bodo Bookhagen"
read_time: false
toc: true
toc_label: "Android-as-Whiteboard"
-- tags:
  - Ubuntu
  - Android
  - Galaxy
  - Whiteboard
  - teaching
---

Can you use your Samsung Galaxy or iPad as an input device / whiteboard for online teaching?
There are different commercial options available for iOS and Windows - but I am working on Ubuntu. I looked at two options:

1. There is [GfxTablet+](https://www-fourier.ujf-grenoble.fr/~demailly/GfxTablet+.html) that is build on the older (and now unmantainted [GfxTablet](https://github.com/rfc2822/GfxTablet)). This contains a driver `networktablet+` that emulates an input device. Using an app on Android (GfxTablet+.apk), you can connect via Wifi to the host and mirror your stylus output. However, I found this difficult to control (although other users really liked it) - I could not draw on existing images or graphs and could not commont on PDFs.
2. [Weylus](https://github.com/H-M-H/Weylus) uses a similar input device scheme, but mirrors the screen in a web browser. The input is considerable more laggy with a few ms delay. But the big bonus is that you can control any open windows in your desktop. Since I am not using an Android tablet for extensive writing (there is much better hardware available for that), but rather edit and annotate enhance existing images, Weylus appears to be a good option.

# Installation
Installation of Weylus is straightforward. Get the latest binary releases from
[https://github.com/H-M-H/Weylus/releases](https://github.com/H-M-H/Weylus/releases) and setup the `uinput` device as described on their [github page](https://github.com/H-M-H/Weylus).

When starting weylus, you should use a passphrase. Identify your IP - I found the NVIDIA hardware acceleration to be slightly faster and turned it on (see )

![Setup screen (use proper binding address) and turn on hardware acceleration if applicable.](https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/weylus1.png)

# Running Weylus
For drawing on sheets and PDFs, the [Xournal++](https://github.com/xournalpp/xournalpp) app comes in handy. It allows to annotate PDFs and images and has a variety of drawing options. Also, you can directly add LaTeX equations and you can combine input from a Stylus Pen with keyboard input.

From your Android device use Chrome (I didn't succeed in using the Samsung Webbrowser) or iPAD's Safari and log in to your device. When you are successfully logged in, select the application you want to work in (this could also be gimp) and start writing!

![Setup screen (use proper binding address) and turn on hardware acceleration if applicable.](https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/Android_screenshot.jpg)

![Screenshot from an iPad showing xournal++ with edits on an image (copy and paste from a Jupyter Notebook).](https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/apple_ipod_weylus_example.png)
