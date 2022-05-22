from moviepy.editor import *

clips = []
bgMusic = AudioFileClip("sound.mp3")

for number in range(100):
    img = ImageClip(f"jpgs/Untitled{number}.jpg").set_duration(0.05)
    clips.append(img)

final_clip = concatenate_videoclips(clips)
final_clip = final_clip.set_audio(bgMusic)
final_clip.write_videofile("jpgStuff.mp4", fps=24)