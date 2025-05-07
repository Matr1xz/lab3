import os
import time

url = "http://192.168.13.2:8000/video.zip"

for i in range(2):
   
    os.system(f"wget -O video.zip {url}")
    time.sleep(2)  
