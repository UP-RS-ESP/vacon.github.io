---
title: 'Using an iPad or Samsung Galaxy with Android as Whiteboard'
layout: archive
date: 2020-10-24
permalink: /posts/2020/10/Android-as-Whiteboard/
author_profile: true
author: "Bodo Bookhagen"
read_time: false
toc: true
toc_label: "iPad and Android-as-Whiteboard"
-- tags:
  - Ubuntu
  - Android
  - iPad
  - Galaxy
  - Whiteboard
  - teaching
  - PDF
  - Annotating
---

Can you use your Samsung Galaxy or iPad as an input device / whiteboard for online teaching?

There are different commercial options available for iOS and Windows - but I am working on Ubuntu. In the past weeks, I have been searching for an easy and straight forward way to link an Ubuntu Desktop system with a touch-sensitive iPad or Samsung Galaxy - mostly for teaching purposes and as a white-board replacement. *Note that the iPad and Galaxy Note Series will not replace a professional graphic and drawing tablet.*

I found and looked at the following two options:

1. There is [GfxTablet+](https://www-fourier.ujf-grenoble.fr/~demailly/GfxTablet+.html) that is build on the older (and now unmaintained [GfxTablet](https://github.com/rfc2822/GfxTablet)). This contains a driver `networktablet+` that emulates an input device in X11. Using an app on Android (*GfxTablet+.apk*), you can connect via Wifi to the host and mirror your stylus output. However, I found this difficult to control (although other users really liked it) and I could not draw on existing images or graphs and could not annotate PDFs.
2. [Weylus](https://github.com/H-M-H/Weylus) uses a similar input device scheme, but mirrors the screen in a web browser on your tablet. The input is considerable more laggy with a few ms delay. But the big bonus is that you can control any open window on your desktop in your webbrowser on the tablet. Since I am not using an Android tablet for extensive writing (there is much better hardware available for that), but rather edit and annotate/enhance existing images, Weylus appeared to be a good option.

# Installation
Installation of Weylus is straightforward. Get the latest binary releases from
[https://github.com/H-M-H/Weylus/releases](https://github.com/H-M-H/Weylus/releases) and setup the `uinput` device as described on their [github page](https://github.com/H-M-H/Weylus).

When starting `weylus`, you should use a passphrase. Identify your IP - I found the NVIDIA hardware acceleration to be slightly faster and turned it on (see below).

<figure>
    <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/weylus1.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/weylus1.png"></a>
    <figcaption>Setup screen (use proper binding address) and turn on hardware acceleration if applicable.</figcaption>
</figure>


# Running Weylus
For drawing on sheets and PDFs, the [Xournal++](https://github.com/xournalpp/xournalpp) app comes in handy. It allows to annotate PDFs and images and has a variety of drawing options. Also, you can directly add LaTeX equations and you can combine input from a Stylus Pen with keyboard input.

From your Android device use * (I didn't succeed in using the Samsung Webbrowser) or *iPAD's Safari* and log in to your device. When you are successfully logged in, select the application you want to work in (this could also be *gimp*) and start drawing!

<figure>
    <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/Android_screenshot.jpg"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/Android_screenshot.jpg"></a>
    <figcaption>Screenshot from an Android Galaxy Note S6 at first login. You can select a specific application or your entire desktop.</figcaption>
</figure>


<figure>
    <a href="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/apple_ipod_weylus_example.png"><img src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/images/apple_ipod_weylus_example.png"></a>
    <figcaption>Screenshot from an iPad showing xournal++ with edits on an image (copy and paste from a Jupyter Notebook).</figcaption>
</figure>
