from moviepy.editor import *
import itertools
import os
import random

# finalVideo = concatenate_videoclips(list)
# finalVideo.write_videofile('finalProduct.mp4')

# final_clip.write_videofile(op.join(movie_fol, out_movie_name)) 
# add folder name to path to send to that directory
# default is to send it to the current directory (current folder)

iceCreamFlavors = ['Vanilla', 'Strawberry', 'Matcha', 'Chocolate Lover', 'Cookies \'n\' Cream', 'Campfire S\'mores', 'Strawberry Cheesecake']

drizzles = ['Chocolate Syrup', 'Strawberry Syrup', 'Condensed Milk', 'Caramel Syrup']

whippedAndPocky = ['Whipped Cream', 'Chocolate Pocky']

def waffleCombos():  
    # waffleCombos returns lists of all possible combinations
    # and permutations of waffle orders

    # Combination starting with Waffle
    combosList = ['Waffle']

    # Case 1: Just ice cream
    for iceCream in iceCreamFlavors:
        combosList.append(iceCream)
        yield combosList

        # Case 2: Ice cream + drizzles
        for drizzle in drizzles:
            combosList.append(drizzle)
            yield combosList

            # Whipped cream and pocky stick combinations
            # Case 3: Ice Cream + drizzle + toppings
            for i in range(1, len(whippedAndPocky)+1):
                combinations = itertools.combinations(whippedAndPocky, i)
                for combination in combinations:
                    combosList.extend(list(combination))
                    yield combosList

                    for j in range(i):
                        combosList.pop()
            # Backtrack as many drizzles as we added
            combosList.pop()

        # Backtrack to new ice cream flavor
        combosList.pop()

def makeVideo(listOfStrings):
    # makeVideo takes a list of strings generated from waffleDrizzleCombos
    # and creates a list of videos by searching through folders with the respective
    # name of the video we are looking for
    # If a video isn't found we print out the reason why and return None
    
    hasWhipped = False
    hasPocky = False
    pathName = os.path.abspath('Clips')
    listOfDirectory = os.listdir(pathName)
    videos = []

    def findRandomWaffle():
        # Search for random video in "Waffle" folder
        pathName = os.path.join(pathName, 'Waffle')
        listOfVideos = os.listdir(pathName)
        # If there exist a video, return it
        if listOfVideos:
            video = random.choice(listOfVideos)
            return VideoFileClip(os.path.join(pathName, video))
        
        # Else print no video found
        print('Waffle video couldn\'t be found')
        return

    def findRandomIceCream(iceCream):
        # Search for random video in "Ice Cream" folder
        pathName = os.path.join(pathName, 'Ice Cream')
        listOfVideos = os.listdir(pathName)
        # If there exist a video, return it
        if listOfVideos:
            video = random.choice(listOfVideos)
            return VideoFileClip(os.path.join(pathName, video))

        # Else print no video found
        print(iceCream ,'video couldn\'t be found')
        return

    def findRandomDrizzle(drizzle):
        # Search for random video in "Drizzle" folder
        pathName = os.path.join(pathName, 'Drizzle')
        listOfVideos = os.listdir(pathName)
        # If there exist a video, return it
        if listOfVideos:    
            video = random.choice(listOfVideos)
            return VideoFileClip()

        # Else print no video found
        print(drizzle ,'video couldn\'t be found')
        return

    def findRandomTopping(topping):
        # Allows us to update hasWhipped bool
        nonlocal hasWhipped
        # Check if topping is Whipped Cream
        if topping == 'Whipped Cream':
            hasWhipped = True
            pathName = os.path.join(pathName, 'Whipped Cream')
            listOfVideos = os.listdir(pathName)
            # If there exist a video, return it
            if listOfVideos:    
                video = random.choice(listOfVideos)
                return VideoFileClip()

            # Else print no video found
            print(topping ,'video couldn\'t be found')
            return

        # Else it is Chocolate Pocky

        # hasWhipped and function was called again
        if hasWhipped:
            pathName = os.path.join(pathName, 'WC CP')
            listOfVideos = os.listdir(pathName)
            # If there exist a video, return it
            if listOfVideos:    
                video = random.choice(listOfVideos)
                return VideoFileClip()

            # Else print no video found
            print(topping ,'video couldn\'t be found')
            return
        # !hasWhipped and function was called, topping is Chocolate Pocky 
        else:
            pathName = os.path.join(pathName, 'Chocolate Pocky')
            listOfVideos = os.listdir(pathName)
            # If there exist a video, return it
            if listOfVideos:    
                video = random.choice(listOfVideos)
                return VideoFileClip()

            # Else print no video found
            print(topping ,'video couldn\'t be found')
            return


    # Loop through each element of listOfStrings to search for the video
    # that has the item name
    for item in listOfStrings:
        # Item is Waffle
        if item == 'Waffle':
            video = findRandomWaffle()
            # If video was found
            if video:
                videos.append(video)
            # video wasn't found, exit combo
            else:
                return
        # Item is Ice Cream
        elif item in iceCreamFlavors:
            pathName = os.path.join(pathName, item)
            video = findRandomIceCream(item)
            if video:
                videos.append(video)
            else:
                return
        # Item is drizzle
        elif item in drizzles:
            pathName = os.path.join(pathName, item)
            video = findRandomDrizzle(item)
            if video:
                videos.append(video)
            else:
                return
        # Item is a topping
        elif item in whippedAndPocky:
            video = findRandomTopping()
            if video:
                videos.append(video)
            else:
                return

    # All videos were found, return list containing videos
    return videos


def videoCreator(startNum=0):
    # videoCreator calls waffleDrizzleCombos and begins creating videos from each
    # video combination.
    # It takes in a starting number parameter, default 0, to skip video processing
    # of videos before the startNum index
    combos = waffleCombos()
    for i, combo in enumerate(combos):
        # Skip video at this index
        if i < startNum:
            continue

        print(i, end=' ')
        listOfVideos = makeVideo(combo)
        # All videos were found for this combination, so we create video
        if listOfVideos:
            # Merge clips into one video
            finalVideo = concatenate_videoclips(listOfVideos)
            # Writing video as mp4 file and sending them to Output Videos folder
            finalVideo.write_videofile(os.path.join('Output Videos',str(i) + '.mp4'))

        # Else video couldn't be found, continue to next combo

# videoCreator()
   
# combos = waffleCombos()
# for i, combo in enumerate(combos):
#     print(i, combo)

# Brute force solution
# Every video will be inside its respective folder name, search through the folder for the video
# If video is found, append and keep searching until list is empty
# Else print reason for why video wasn't printed

# Videos will be name with drizzles in order of being place
# Assuming they are in the proper folder there is no need to name them
# by ice cream or topping

# Searching through video files,
# if video found create it
# else print that video couldn't be created due to 'insert reason'



# Make a function to print the videos with numbers as the output.
# If the program stops print the number it stopped at.
# Use the number as input for the function to start again at the number
# rather than resetting from 0, set default arguement to 0

# Possibly ask for user input, but it could be obnoxious 