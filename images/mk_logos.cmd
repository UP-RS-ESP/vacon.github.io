magick -quality 99 -density 300 UP_1200x_logo.png IBIGEO_1200x_logo.jpg 1200px-Emblema_Parque_Nacional_Los_Cardones.jpg 1200_pozuelos_logo.jpg -fuzz 1% -trim -bordercolor white -border 800x0 +repage +append 4logos_1200x.jpg
magick /Dropbox/Argentina/NGL/NWArg_GNSS_VACON_fixedSA.png -resize 600x NWArg_GNSS_VACON_fixedSA.jpg 
magick 4logos_1200x.jpg -resize 600x 4logos_1200x.jpg
magick -quality 99 -density 300 4logos_1200x.jpg NWArg_GNSS_VACON_fixedSA.jpg -fuzz 1% -trim -bordercolor white -border 0x10 +repage -gravity center -append 4Logo_map_VACON.jpg
