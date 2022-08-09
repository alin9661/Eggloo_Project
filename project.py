from moviepy.editor import *
import itertools
import random
import os

def listRandomizer(listOfVideos):
    random.shuffle(listOfVideos)

def listOfVideoClips(folder_name):
    listOfFiles = os.listdir(folder_name)
    pathName = os.path.abspath(folder_name)
    listRandomizer(listOfFiles)
    return [VideoFileClip(os.path.join(pathName, video)) for video in listOfFiles]

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

def waffleCombos():
    # Starting with waffle, the total number of combinations that can be made
    # with 7 ice cream flavors, 9 toppings, and 4 drizzles is 1610
    # This function loops through every ice cream flavor which can each have two
    # toppings and 1 drizzle on a case by case basis
    combosList = ['Waffle']

    # Case 1: Just ice cream
    for iceCream in iceCreamFlavors:
        remToppings = toppings.copy()
        combosList.append(iceCream)
        yield combosList

        # Case 2: Ice cream + drizzle
        for drizzle in drizzles:
            combosList.append(drizzle)
            yield combosList
            combosList.pop()

        # Case 3: Ice Cream + 1 Topping
        for topping1 in toppings:
            combosList.append(topping1)
            yield combosList
            remToppings.remove(topping1)

            # Case 4: Ice Cream + 1 topping + drizzle
            for drizzle in drizzles:
                combosList.append(drizzle)
                yield combosList
                combosList.pop()

            # Case 5: Ice cream + 2 topping
            for topping2 in remToppings:
                combosList.append(topping2)
                yield combosList

                # Case 6: Ice Cream + 2 topping + drizzle
                for drizzle in drizzles:
                    combosList.append(drizzle)
                    yield combosList
                    combosList.pop()
                # Backtrack to new 2nd topping
                combosList.pop()
            # Backtrack to new 1st topping
            combosList.pop()
        # Backtrack to new ice cream flavor
        combosList.pop()
        
# combos = waffleCombos()
# numOfCombos = sum(1 for _ in waffleCombos())
# for combo in combos:
#     print(combo)
# print(numOfCombos)

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
    videos = []

    for item in listOfStrings:
        if item == 'Waffle':
            # Find video in folder
            for video in listOfDirectory: 
                # Add video to list
                if item in video:
                    videos.append(video)
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
                    videos.append(video)
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
                        videos.append(video)
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
                        videos.append(video)
                        break

                # Video wasn't found
                else:
                    print(item, 'video couldn\'t be found')
                    return

            elif item == 'Chocolate Pocky' and not hasWhipped:
                pathName = os.path.join(pathName, 'No Whipped Cream')
                listOfDirectory = os.listdir(pathName)

        elif item in drizzles:
            # Possible to reach here without adding a pocky or whipped cream
            # in that case we would have to go to no whipped and no pocky
            pass


# path = os.path.abspath('Clips')
# listOfStuff = os.listdir(path)
# print(listOfStuff)
# for item in listOfStuff:
#     if 'Cookies' in item:
#         print(item)

# nums = list(range(1,11))
# for i, num in enumerate(nums):
#     print(i, end=' ')
#     print(num)

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

# test code (To be deleted)
# listOfFolders = os.listdir('Clips')
# print(listOfFolders)
# pathname = os.path.abspath('Clips')
# listOfVanilla = os.listdir(os.path.join(pathname, 'Strawberry Cheesecake'))
# print(listOfVanilla)
    
# combos = waffleDrizzleCombos()
# for i, combo in enumerate(combos):
#     print(i, combo)



# Make a function to print the videos with numbers as the output.
# If the program stops print the number it stopped at.
# Use the number as input for the function to start again at the number
# rather than resetting from 0, set default arguement to 0

# Possibly ask for user input, but it could be obnoxious 