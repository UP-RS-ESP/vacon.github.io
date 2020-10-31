---
title: 'Converting BBB recordings to MP4 with Webcam on Deskshare Movie'
layout: archive
date: 2020-10-28
permalink: /posts/2020/10/BBB-to-MP4-Webcam-and-Deskshare/
author_profile: true
author: "Bodo Bookhagen"
read_time: false
toc: true
toc_label: "BBB recordings to MP4"
-- tags:
  - BBB
  - MP4
  - Webcam
  - teaching
---
Convert your BBB recordings to a compressed MP4 stream with webcam overlay and logo.

Similar to several other academic institutions, we are hosting our own [Big Blue Button Server (BBB)](https://bigbluebutton.org/). This is an open-source and free conference and teaching server tailored for academic environments. The standard player showing recorded teaching session is fairly simple and does not allow to download a video stream (e.g. MP4). However, the necessary files - movie of the shared desktop/presentation and webcamera - are stored on the BBB server and can be converted with [ffmpeg](https://ffmpeg.org/) to a combined stream. Also, ffmpeg allows to apply audio-filtering steps that will enhance audio quality.

The next steps are tailored towards combining shared desktops and webcameras and applying a FFT-based noise canceling and speech filter ([afftdn](https://ffmpeg.org/ffmpeg-filters.html#afftdn)). We experimented with different low- and high-pass filtering options, but found this to be most useful. If you have a particularly noisy audio stream, you may need to filter this manually or use [audacity](https://www.audacityteam.org/).

These steps also allow you to convert existing recordings. If you plan to record new, high resolution recording, please look at [OBS](https://obsproject.com/).

On the BBB server change to the directory that contains the processed and published recordings. These are usually stored in `/var/bigbluebutton/published/presentation/`. Change directory to the meeting id of the recording - these are usually long digits and number combinations that you see in the http address when playing the recording (e.g., *bda894a68f6d2aa38dc62dd788e19d357e17948c-1603807633429*.)

First, extract audio from webcam stream (stored in *video/webcams.webm*), filter audio with *afftdn*, and combine with desktop stream (stored in *deskshare/deskshare.webm*). We convert the WEBM format to MP4.
```
ffmpeg -nostdin -threads 4 -i video/webcams.webm -i deskshare/deskshare.webm -af afftdn deskshare_with_sound.mp4
```

Next, reduce size of video recording by 1/4 (scale by 4). This depends on your video resolution, we are currently using a resolution of
```
video_output_width: 640
video_output_height: 480
```
set in */usr/local/bigbluebutton/core/scripts/presentation.yml*.

```
ffmpeg -nostdin -threads 4 -i video/webcams.webm -vf "scale=iw/4:ih/4" webcams_sc4.mp4
```

Add scaled webcam stream and deskshare video and place webcam stream in upper right corner (often referred to as 'picture in picture'):
```
ffmpeg -nostdin -i deskshare_with_sound.mp4 -vf "movie=webcams_sc4.mp4[inner]; [in][inner] overlay=W-w:0 [out]" completed_ur.mp4
```

We also add the Institute of Geoscience logo to the upper left corner. We scale the (almost) squared logo to 100x100 pixels.
```
ffmpeg -nostdin -i completed_ur.mp4 -i geowiss__cmyk_blue_2000px.png -filter_complex "[1:v]scale=100:100[v1];[0:v][v1]overlay[outv]" -map "[outv]" -c:a copy -map 0:a completed_ur_logo.mp4
```

This file is now ready to be uploaded to a media server for further distribution!

**Note that the following video has been downscaled to 640x360 (from 1280x720) with ffmpeg:**
`ffmpeg -nostdin -ss 00:18:06 -i completed_afftdn_ll.mp4 -t 00:05:00 -vf scale=640:360 -vc copy NB_linearregression.mp4`

<div style="text-align:center;">
<video width="330" height="270" src="https://github.com/UP-RS-ESP/up-rs-esp.github.io/raw/master/_posts/mp4/NB_linearregression.mp4" type="video/mp4" width="320" height="180" frameborder="0" scrolling="no"  allowfullscreen></video>
</div>


**Here is a high-res link to a Media-UP recording of an entire lecture:**
<div style="text-align:center;">
<iframe width="330" height="270" src="https://mediaup.uni-potsdam.de/player?autostart=n&videoId=djJACa1J&captions=y&chapterId=0" frameborder="0" scrolling="no"  allowfullscreen></iframe>
</iframe>
</div>


# A Shell script combining these steps:
```bash
#!/bin/sh
# Convert the deskshare and webcam to a combined video stream including logo
# cd /var/bigbluebutton/published/presentation/
meetingId=$1
cd $meetingId

# add webcam sound to deskshare
ffmpeg -nostdin -threads 4 -i video/webcams.webm -i deskshare/deskshare.webm -af afftdn deskshare_with_sound.mp4
ffmpeg -nostdin -threads 4 -i video/webcams.webm -vf "scale=iw/4:ih/4" webcams_sc4.mp4

#add picture in picture
ffmpeg -nostdin -i deskshare_with_sound.mp4 -vf "movie=webcams_sc4.mp4[inner]; [in][inner] overlay=W-w:0 [out]" completed_ur.mp4

# add logo in upper right corner (could be combined with previous command)
ffmpeg -nostdin -i completed_ur.mp4 -i /var/bigbluebutton/published/presentation/geowiss__cmyk_blue_2000px.png -filter_complex "[1:v]scale=100:100[v1];[0:v][v1]overlay[outv]" -map "[outv]" -c:a copy -map 0:a completed_afftdn_ll.mp4

rm -fr deskshare_with_sound.mp4 webcams_sc4.mp4 completed_ur.mp4
```
