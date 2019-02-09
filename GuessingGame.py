import random
from random import randint

#Generate a random number to begin the game
x = randint(1,100)
print(x)

#Placeholder global win condition for game loop
w = False

#Start game loop
  
while w == False:
    try: 
        p = input ("Guess my number between One and One-Hundred:")
        g = int(p)+0
    except ValueError: 
        print ("Eat a dick, pick an integer between 1 and 100") 
    v = ""

    if str(p) == "q" or "quit": 
        w = True

    g = int(p)

    if g == x: 
        print("You chose wisely, you WON!!!") 
        w = True
        break
    if g < x  : v = "You are lower." 
    if g > x  : v = "You are higher." 
    if g > 100: v = "Under 101 please..."
    if g < 1  : v = "Above 0 please..."
    print(v)
    continue
    
    