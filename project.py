from importlib.resources import path
from moviepy.editor import *
import random
import os

def listRandomizer(listOfVideos):
    return random.shuffle(listOfVideos)