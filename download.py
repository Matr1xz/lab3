import os
import time

url = "http://172.17.0.3:8000/video.zip"

for i in range(2):
    print(f"Download lần {i+1}...")
    os.system(f"wget -O video.zip {url}")
    time.sleep(2)  # chờ 2 giây giữa 2 lần tải (tuỳ chọn)
