from PIL import Image
import os

img = Image.open("pngs/Untitled0.jpg")
img = img.convert("RGB")
img.save("pngs/Untitled0.png")

os.remove("pngs/Untitled0.jpg")