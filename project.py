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

# list = listOfVideoClips('Clips')
# print()
# print(list)

# finalVideo = concatenate_videoclips(list)
# finalVideo.write_videofile('finalProduct.mp4')


iceCreamFlavors = ['Vanilla', 'Strawberry', 'Matcha', 'Chocolate Lover', 'Cookies \'n\' Cream', 'Campfire S\'mores', 'Strawberry Cheesecake']

toppings = ['Fruity Pebbles', 'Coconut Flakes', 'Crushed Oreos', 'Granola', 'Mochi', 'Diced Peanuts', 'Whipped Cream', 'Pocky Sticks', 'Fresh Fruit']

drizzles = ['Chocolate Syrup', 'Strawberry Syrup', 'Condensed Milk', 'Caramel Syrup']

def waffleCombos():
    # Starting with waffle, the total number of combinations that can be made
    # with 7 ice cream flavors, 9 toppings, and 4 drizzles is 1610
    # This function loops through every ice cream flavor which can each have two
    # toppings and 1 drizzle on a case by case basis
    combosList = ['Waffle']

    # Loop through every ice cream flavor
    for iceCream in iceCreamFlavors:
        remToppings = toppings.copy()
        combosList.append(iceCream)
        yield combosList

        # Case 1: Just ice cream and drizzle
        for drizzle in drizzles:
            combosList.append(drizzle)
            yield combosList
            combosList.pop()

        # Case 2: Ice Cream + 1 Topping + Drizzle
        for topping1 in toppings:
            combosList.append(topping1)
            yield combosList
            remToppings.remove(topping1)
            for drizzle in drizzles:
                combosList.append(drizzle)
                yield combosList
                combosList.pop()

            # Case 3: Ice cream + 2 topping + drizzle
            for topping2 in remToppings:
                combosList.append(topping2)
                yield combosList
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
        
combos = waffleCombos()
numOfCombos = sum(1 for _ in waffleCombos())
for combo in combos:
    print(combo)
print(numOfCombos)