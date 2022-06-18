import os
try: # Try move Untitled0.png
    os.rename("pngs/Untitled0.png","Untitled0.png")
except OSError:
    os.remove("pngs/Untitled0.png")

try: # Try to remove 2 files.
    os.remove("jpgs/Untitled0.jpg")
    os.remove("pngs/Untitled100.png")
except OSError:
    print("issue deleting file")

for number in range(99): # delete all files
    print(f"deleting {number+1}", end="\r")
    try:
        os.remove(f"pngs/Untitled{number+1}.png")
        os.remove(f"jpgs/Untitled{number+1}.jpg")
    except OSError:
        print(f"issue deleting {number+1}")
os.rename("Untitled0.png","pngs/Untitled0.png")