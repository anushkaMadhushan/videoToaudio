import moviepy.editor as mp

Clip = mp.VideoFileClip("sample.mp4")
Clip.audio.write_audiofile("myAudio.mp3")