import os

from moviepy.editor import *

def extract():
    sound = AudioFileClip(os.path.join(os.getcwd(), "guardians_of_children/static/video/reference.mp4"))
    sound.write_audiofile(os.path.join(os.getcwd(), "guardians_of_children/audio_classification/reference_audio.wav"), 44100, 2, 2000, "pcm_s32le")