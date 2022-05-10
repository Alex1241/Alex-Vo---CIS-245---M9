# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Alex Vo
# Creation Date: May 10, 2022
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you,
    you see two caves. In one cave, the dragon is friendly
    and will share his treasure with you. The other dragon
    is greedy and hungry, and will eat you on sight.''')
    #print()
    #This print command also does nothing.

def chooseCave():
    cave = ''
    #while cave != '1' and cave != '2':
    while cave != '1' and cave != '2':
        #There was an indentation error. I had to google how to fix it and figured out there is a setting that helps me see it. I ended up shifting everything in this function to four dots since I am unsure how to reproduce the arrow.
        print('Which cave will you go into? (1 or 2)')
        cave = input()
    #return caves
    return cave
        # I removed the s because there are no variables with caves. Only cave exists and therefore the return command does not know where to get the variable from if it has an s.

#def checkCave(chosenCave):
def checkCave(caveNumber):
        #I changed the variable inside the parenthesis to match the logic being used that the rest of the code talks about. caveNumber replaces chosenCave.
    print('You approach the cave...')
    #sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    #sleep for 2 seconds
    time.sleep(3)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    #print()
    # This print command does absolutely nothing. Removed it.
	#sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

	#if chosenCave == str(friendlyCave):
    if caveNumber == str(friendlyCave):
        #This line also used chosenCave. I replaced it with caveNumber for logic.
        print('Gives you his treasure!')
    else:
        #print 'Gobbles you down in one bite!'
        print('Gobbles you down in one bite!')
            #The original print command was missing a parenthesis.

playAgain = 'yes'
#while playAgain = 'yes' or playAgain = 'y':
while playAgain == 'yes' or playAgain == 'y':
        #This line does not use the proper expression that python can understand. I replaced both = with ==.
    displayIntro()
    #caveNumber = choosecave()
    caveNumber = chooseCave()
    #This line of code had a simple mistype error where the C in cave was not capitalized to match the function defined above.
    checkCave(caveNumber)
    
    print('Do you want to play again? (yes or no)')
    playAgain = input()
    if playAgain == "no":
        #print("Thanks for planing")
        print("Thanks for playing!")
            #This line required a simple spelling correction. Changed planing to playing and added an exclamation point since a period makes the voice sound dull compared to the excitement the exclamation point voice gives.