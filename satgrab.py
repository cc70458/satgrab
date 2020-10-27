import re
import wget
import os
import ctypes
from pathlib import Path

webfile = Path("d:/wallpaper/conus.php")
if webfile.is_file():
    res = os.system('del *.php')

url = 'https://www.star.nesdis.noaa.gov/GOES/conus.php?sat=G16'
wget.download(url)
print ('Choosing the latest Satellite Image')
pattern = re.compile("[0-9]+_GOES16-ABI-CONUS-GEOCOLOR-5000x3000.jpg")
textfile = open("conus.php", 'r')
filetext = textfile.read()
textfile.close()
match = str(re.findall(pattern,filetext))
filename = str(match[:-2][2:])
header = "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/" + str(match[:-2][2:])
print(header)

my_file = Path("d:/wallpaper/wallpaper.jpg")
if my_file.is_file():
    os.remove('d:/wallpaper/wallpaper.jpg')
print ('Downloading the file')    
wget.download(header, 'D:/wallpaper/wallpaper.jpg')

print ('Changing the Wallpaper to the lastest downloaded file')
drive = "D:\\"
folder = "wallpaper"
image = "wallpaper.jpg"
image_path = os.path.join(drive, folder, image)
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
