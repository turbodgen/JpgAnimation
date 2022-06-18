from PIL import Image
import os
import cv2

vidcap = cv2.VideoCapture('video.mp4')
success,image = vidcap.read()
count = 0
quali = 100
keepQuali = quali

f = open("data.txt", "r+")

while success:
    print(f"{count}", end="\r")
    cv2.imwrite("imgs/frame%d.jpg" % count, image)     # save frame as png file      
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1

print("\n\n")
allFiles = len(os.listdir("imgs"))

for number in range(allFiles):
    img = Image.open(f"imgs/frame{number}.jpg")
    img = img.convert("RGB")
    img.save(f"imgs/frame{number}.jpg", quality=quali, compress_level=5)
    img.close()
    print(quali)
    f.write(f"imgs/frame{number}.jpg - {quali}\n")
    print(f"number {number}")
    keepQuali = keepQuali - (keepQuali/count)
    quali = round(keepQuali)

f.close()