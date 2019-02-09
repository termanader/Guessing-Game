import random
import math
from random import randint

#Generate a random number to begin the game
x = randint(1,100)
print(x)

#Placeholder global win condition for game loop


#Start game loop
while True:  
    while True:
        try:
            g = int(input('Guess my number between One and One-Hundred:'))
            break
        except:
            print("An integer greater than 0 and less than one-hundred please...")

    v = ""
    if g == x: 
        print("You chose wisely, you WON!!!") 
        break
    if g < x  : v = "You are lower." 
    if g > x  : v = "You are higher." 
    if g > 100: v = "Under 101 please..."
    if g < 1  : v = "Above 0 please..."
    print(v)
