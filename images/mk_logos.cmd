convert -quality 99 -density 300 UP_1200x_logo.png IBIGEO_1200x_logo.jpg 1200px-Emblema_Parque_Nacional_Los_Cardones.jpg -fuzz 1% -trim -bordercolor white -border 800x0 +repage +append 3logos_1200x.jpg
convert 3logos_1200x.jpg -resize 600x 3logos_1200x.jpg
convert -quality 99 -density 300 3logos_1200x.jpg NWArg_GNSS_VACON_fixedSA.jpg -fuzz 1% -trim -bordercolor white -border 0x10 +repage -gravity center -append 3Logo_map_VACON.jpg
