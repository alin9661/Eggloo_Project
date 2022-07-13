from moviepy.editor import *
import random
import os

def listRandomizer(listOfVideos):
    random.shuffle(listOfVideos)

def listOfVideoClips(folder_name):
    listOfFiles = os.listdir(folder_name)
    pathName = os.path.abspath(folder_name)
    listRandomizer(listOfFiles)
    return [VideoFileClip(os.path.join(pathName, video)) for video in listOfFiles]

list = listOfVideoClips('Clips')
print()
print(list)

finalVideo = concatenate_videoclips(list)
finalVideo.write_videofile('finalProduct.mp4')