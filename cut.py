from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip("jpgStuff.mp4", 0, 2, targetname="test.mp4")
