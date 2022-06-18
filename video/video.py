import time
from moviepy.editor import *
import cv2

f = open("data.txt","r+")
clips = []
text = []
frame_ = 1

thisVid = VideoFileClip("video.mp4")
thisVid.audio.write_audiofile("audio.mp3")
bgMusic = AudioFileClip("audio.mp3")

for number in range(1139):
    image = cv2.imread(f"imgs/frame{number}.jpg")
    cv2.putText(image, f.readline(number+1), (50, 670), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imwrite(f"imgs/frame{number}.jpg", image)
    cv2.waitKey(0)
    img = ImageClip(f"imgs/frame{number}.jpg").set_duration(0.04166666666)
    clips.append(img)
    print(number)

final_clip = concatenate_videoclips(clips)
final_clip = final_clip.set_audio(bgMusic)
final_clip.write_videofile("jpgStuff.mp4", fps=24)

time.sleep(2)