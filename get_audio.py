import os


command = "ffmpeg -i $(youtube-dl -f best --get-url https://youtu.be/5qap5aO4i9A) -f s16le -ac 2 -ar 48000 -acodec pcm_s16le input.raw"

os.remove("input.raw")
os.system(command)

