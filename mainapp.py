import imagtoAscii as im
import videotoImg as vi
import time
import os
# vi.convert("badapple.mp4")
frames=sorted([f for f in os.listdir("data")])

for i in range(len(frames)):
    print(im.imgtoAscii(f"data/frame{i}.jpg"))
    time.sleep(0.018)#frameratepersec
    os.system('clear')