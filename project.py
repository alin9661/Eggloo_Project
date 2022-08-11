import string
from moviepy.editor import *
import itertools
import random
import os

# list = listOfVideoClips('Clips')
# print()
# print(list)

# finalVideo = concatenate_videoclips(list)
# finalVideo.write_videofile('finalProduct.mp4')

# final_clip.write_videofile(op.join(movie_fol, out_movie_name)) 
# add folder name to path to send to that directory
# default is to send it to the current directory (current folder)

iceCreamFlavors = ['Vanilla', 'Strawberry', 'Matcha', 'Chocolate Lover', 'Cookies \'n\' Cream', 'Campfire S\'mores', 'Strawberry Cheesecake']

toppings = ['Fruity Pebbles', 'Coconut Flakes', 'Crushed Oreos', 'Granola', 'Mochi', 'Diced Peanuts', 'Whipped Cream', 'Pocky Sticks', 'Fresh Fruit']

drizzles = ['Chocolate Syrup', 'Strawberry Syrup', 'Condensed Milk', 'Caramel Syrup']

whippedAndPocky = ['Whipped Cream', 'Chocolate Pocky']

def waffleDrizzleCombos():  
    # Whipping cream or no WC, Pocky or no pocky
    # All 4 drizzle permutations, which means the order in which
    # we put the drizzle matters in calculation
    combosList = ['Waffle']

    # Case 1: Just ice cream
    for iceCream in iceCreamFlavors:
        combosList.append(iceCream)
        yield combosList

        # Whipped cream and pocky stick combinations
        for i in range(1, len(whippedAndPocky)+1):
            combinations = itertools.combinations(whippedAndPocky, i)
            for combination in combinations:
                combosList.extend(list(combination))
                yield combosList

        # Case 3: Ice cream + toppings + drizzle drizzle (All permutations of drizzle)
                for j in range(1, len(drizzles)+1):
                    # Permutation function allows us to pass a list of items to
                    # find the permutations of with an integer input of how long 
                    # desired sequence to be
                    permutations = itertools.permutations(drizzles, j)
                    for permutation in permutations:
                        combosList.extend(list(permutation))
                        yield combosList

                        # Backtrack as many toppings as we added
                        for k in range(j):
                            combosList.pop()
                
                # Backtracking for whipped cream and pocky sticks
                for j in range(i):
                    combosList.pop()

        # Backtrack to new ice cream flavor
        combosList.pop()

def makeVideo(listOfStrings):
    # makeVideo takes a list of strings generated from waffleDrizzleCombos
    # and creates a video by concatenating clips using the corresponding name
    # of the string with respect to the order at which they appear in the string
    
    hasWhipped = False
    hasPocky = False
    pathName = os.path.abspath('Clips')
    listOfDirectory = os.listdir(pathName)
    listOfDrizzles = []
    videos = []
    

    for item in listOfStrings:
        if item == 'Waffle':
            # Find video in folder
            for video in listOfDirectory: 
                # Add video to list
                if item in video:
                    videos.append(VideoFileClip(os.path.join(pathName, video)))
                    break

            # Video wasn't found in folder, error
            else:
                print('Waffle video couldn\'t be found')
                return

        elif item in iceCreamFlavors:
            pathName = os.path.join(pathName, item)
            listOfDirectory = os.listdir(pathName)
            for video in listOfDirectory:
                # Add video to list
                if item in video:
                    videos.append(VideoFileClip(os.path.join(pathName, video)))
                    break

            # Video wasn't found
            else:
                print(item, 'video couldn\'t be found')
                return
        
        elif item in whippedAndPocky:
            if item == 'Whipped Cream':
                hasWhipped = True
                pathName = os.path.join(pathName, item)
                listOfDirectory = os.listdir(pathName)
                for video in listOfDirectory:
                    # Add video to list
                    if item in video:
                        videos.append(VideoFileClip(os.path.join(pathName, video)))
                        break

                # Video wasn't found
                else:
                    print(item, 'video couldn\'t be found')
                    return

            # It is possible to reach this statement without reaching whipped cream
            # In that case whipped cream wasn't a topping and we should go straight
            # into no whipped cream folder
            elif item == 'Chocolate Pocky' and hasWhipped:
                hasPocky = True
                pathName = os.path.join(pathName, item)
                listOfDirectory = os.listdir(pathName)
                for video in listOfDirectory:
                    # Add video to list
                    if item in video:
                        videos.append(VideoFileClip(os.path.join(pathName, video)))
                        break

                # Video wasn't found
                else:
                    print(item, 'video couldn\'t be found')
                    return

            elif item == 'Chocolate Pocky' and not hasWhipped:
                hasPocky = True
                pathName = os.path.join(pathName, 'No Whipped Cream', item)
                listOfDirectory = os.listdir(pathName)
                for video in listOfDirectory:
                    # Add video to list
                    if item in video:
                        videos.append(VideoFileClip(os.path.join(pathName, video)))
                        break

                # Video wasn't found
                else:
                    print(item, 'couldn\'t be found')
                    return

        elif item in drizzles:
            # Possible to reach here without adding a pocky or whipped cream
            # in that case we would have to go to no whipped and no pocky
            if not hasWhipped and not hasPocky:
                pathName = os.path.join(pathName, 'No Whipped Cream', 'No Pocky Stick')
                listOfDirectory = os.listdir(pathName)

            # Continue where we left off
            # Add drizzles into a list, when for loop finishes create a string of words with the list
            # Using the string search for video name, else print video couldn't be found
            listOfDrizzles.append(item)
    
    stringOfDrizzles = ', '.join(listOfDrizzles)
    for video in listOfDirectory:
        # Add video to list
        if stringOfDrizzles in video:
            videos.append(VideoFileClip(os.path.join(pathName, video)))
            break
    # Video wasn't found
    else:
        print(item, 'couldn\'t be found')
        return

    # Return list of vids or create vid

def videoCreator(startNum=0):
    # Takes in list of videos and creates result video
    # Prints out the number of the video
    combos = waffleDrizzleCombos()
    for i, combo in enumerate(combos):
        # Skip video at this index
        if i < startNum:
            continue

        print(i, end=' ')
        listOfVideos = makeVideo(combo)
        # All videos were found for this combination, so we create video
        if listOfVideos:
            finalVideo = concatenate_videoclips(listOfVideos)
            finalVideo.write_videofile(os.path.join('Output Videos',str(i) + '.mp4'))

        # Else video couldn't be found, continue to next combo

videoCreator()

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