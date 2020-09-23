from ftplib import FTP
import wget
import os
import ctypes
from pathlib import Path

ftp = FTP('ftp.nnvl.noaa.gov')
ftp.login()
ftp.cwd('GOES')
ftp.cwd('GER')
files = []
ftp.dir(files.append)

ftp.quit()
print(len(files))
filename = files[-1]
filename = filename[-29:]
print(filename)

url = "ftp://ftp.nnvl.noaa.gov/GOES/GER/"+filename
print(url)

my_file = Path('d:/wallpaper/wallpaper.jpg')
if my_file.is_file():
    os.remove('d:/wallpaper/wallpaper.jpg')
wget.download(url, 'D:/wallpaper/wallpaper.jpg')

drive = "D:\\"
folder = "wallpaper"
image = "wallpaper.jpg"
image_path = os.path.join(drive, folder, image)
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)