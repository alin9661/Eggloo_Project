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

# Method 1
# Inside 'Clips' folder create folders to separate the ice cream flavors
# Inside the ice cream folders separate them by toppings (i.e. whipped/no whipped, pocky/no pocky)
# From their consider order of name

#  Method 2
# Use some data structure (Dictionary, Tree)

# test code (To be deleted)
listOfFolders = os.listdir('Clips')
print(listOfFolders)
pathname = os.path.abspath('Clips')
listOfVanilla = os.listdir(os.path.join(pathname, 'Vanilla'))
print(listOfVanilla)
    
# combos = waffleDrizzleCombos()
# for i, combo in enumerate(combos):
#     print(i, combo)



# Make a function to print the videos with numbers as the output.
# If the program stops print the number it stopped at.
# Use the number as input for the function to start again at the number
# rather than resetting from 0, set default arguement to 0
