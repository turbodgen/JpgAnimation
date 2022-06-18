from multiprocessing.connection import wait
from PIL import Image
import os, shutil

quali = 100
loops = 100
resizing = False

for file in os.listdir("pngs"):
    if file != "Untitled0.png":
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
            print(os.path.abspath(file))
            os.rename("pngs/"+file, os.path.basename(file))
            img = Image.open(file)
            img = img.convert("RGB")
            img.save("pngs/Untitled0.png")
            
# resize
while resizing:
    if img.size[0] > 1080:
        img.close()
        try:
            os.rename("pngs/Untitled0.png","Untitled0.png")
            img = Image.open("Untitled0.png")
            img = img.resize((int(img.size[0]/2), int(img.size[1]/2)))
            img.save("pngs/Untitled0.png")
            print("Resizing..")
        except:
            pass
        img = Image.open("pngs/Untitled0.png")
        img = img.resize((int(img.size[0]/2), int(img.size[1]/2)))
        img.save("pngs/Untitled0.png")
        print("Resizing..")
    resizing = False
    img = Image.open("pngs/Untitled0.png")

# create images
for number in range(loops):
    img = Image.open(f"pngs/Untitled{number}.png")
    img = img.convert("RGB")
    img.save(f"jpgs/Untitled{number}.jpg", quality=quali, compress_level=5) # I think the compression level is useless rn
    img = Image.open(f"jpgs/Untitled{number}.jpg")
    img.save(f"pngs/Untitled{number+1}.png")
    img.close()
    if quali >= 2: # if quality isnt 1
        quali-=1
    print(str("█" * round((number+1)/3) + '-' * round((loops - (number+1))/3))+" "+str(number+1)+"%", end="\r")  # multipy █, multiply -. add percentage, rewrite on line.

