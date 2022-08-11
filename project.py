from moviepy.editor import *
import itertools
import os

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

        # Case 2: Ice cream + drizzles
        for j in range(1, len(drizzles)+1):
            # Permutation function allows us to pass a list of items to
            # find the permutations of with an integer input of how long 
            # desired sequence to be
            permutations = itertools.permutations(drizzles, j)
            for permutation in permutations:
                combosList.extend(list(permutation))
                yield combosList

                # Backtrack as many drizzles as we added
                for k in range(j):
                    combosList.pop()

        # Whipped cream and pocky stick combinations
        for i in range(1, len(whippedAndPocky)+1):
            combinations = itertools.combinations(whippedAndPocky, i)
            for combination in combinations:
                combosList.extend(list(combination))
                yield combosList

        # Case 3: Ice cream + toppings + drizzle drizzle (All permutations of drizzle)
                for j in range(1, len(drizzles)+1):
                    permutations = itertools.permutations(drizzles, j)
                    for permutation in permutations:
                        combosList.extend(list(permutation))
                        yield combosList

                        # Backtrack as many drizzles as we added
                        for k in range(j):
                            combosList.pop()
                
                # Backtracking for whipped cream and pocky sticks
                for j in range(i):
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

    # Loop through each element of listOfStrings to search for the video
    # that has the item name
    for item in listOfStrings:
        # Item is Waffle
        if item == 'Waffle':
            # Search folder for video with item name
            for video in listOfDirectory: 
                # Add video to list
                if item in video:
                    videos.append(VideoFileClip(os.path.join(pathName, video)))
                    break

            # Video wasn't found in folder, error
            else:
                print(item, 'video couldn\'t be found')
                return

        # Item is an ice cream
        elif item in iceCreamFlavors:
            pathName = os.path.join(pathName, item)
            listOfDirectory = os.listdir(pathName)
            # Search folder for video with item name
            for video in listOfDirectory:
                # Add video to list
                if item in video:
                    videos.append(VideoFileClip(os.path.join(pathName, video)))
                    break

            # Video wasn't found
            else:
                print(item, 'video couldn\'t be found')
                return
        
        # Item is whipped cream/Chocolate pocky
        elif item in whippedAndPocky:
            # Item is in Whipped Cream folder
            if item == 'Whipped Cream':
                hasWhipped = True
                pathName = os.path.join(pathName, item)
                listOfDirectory = os.listdir(pathName)
                # Search folder for video with item name
                for video in listOfDirectory:
                    # Add video to list
                    if item in video:
                        videos.append(VideoFileClip(os.path.join(pathName, video)))
                        break

                # Video wasn't found
                else:
                    print(item, 'video couldn\'t be found')
                    return

            # Item is in Chocolate Pocky folder 
            elif item == 'Chocolate Pocky' and hasWhipped:
                hasPocky = True
                pathName = os.path.join(pathName, item)
                listOfDirectory = os.listdir(pathName)
                # Search folder for video with item name
                for video in listOfDirectory:
                    # Add video to list
                    if item in video:
                        videos.append(VideoFileClip(os.path.join(pathName, video)))
                        break

                # Video wasn't found
                else:
                    print(item, 'video couldn\'t be found')
                    return

            # Edge case: Chocolate Pocky without whipped cream
            # Move path into No Whipped Cream folder
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
                    print(item, 'video couldn\'t be found')
                    return

        # Item is a drizzle
        elif item in drizzles:
            # Edge case: Drizzles with NO Pocky or Whipped Cream
            # Move path into No Whipped Cream and No Pocky Stick
            if not hasWhipped and not hasPocky:
                pathName = os.path.join(pathName, 'No Whipped Cream', 'No Pocky Stick')
                listOfDirectory = os.listdir(pathName)

            # Create a string of drizzle names to search for video
            stringOfDrizzles = ''
            if not stringOfDrizzles:
                stringOfDrizzles = item
            else:
                stringOfDrizzles += ', ' + item
            
            # Find video from drizzles
            # Looping through sorted listOfDirectory allows us to obtain the first
            # occurence of the video we are looking for sake of video concatenation order
            for video in sorted(listOfDirectory):
                # Add video to list
                if stringOfDrizzles in video:
                    videos.append(video)
                    break

            # Video wasn't found
            else:
                print(stringOfDrizzles, 'video couldn\'t be found')
                return

    # All videos were found, return list
    return videos


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

# videoCreator(1000)

combos = waffleDrizzleCombos()
for i, combo in enumerate(combos):
    print(i, combo)

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