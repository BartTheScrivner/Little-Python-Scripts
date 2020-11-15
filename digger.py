# -*- coding: utf-8 -*-
import random

turn = 10
brick = "#"
ground = 64*brick
space = ' '*30
character = "&"
position = space + character
directions = ['A','S','D']

print("It's dark...")
print("The walls are close.")

for i in range(turn):
    start = input(position + '\n' + ground + '\n' + '\n \n Which way? A left / S down / D right:  ')
    choice = start.upper()
    out = random.choice(directions)
    oxlvl = (turn-i)*10
    if choice == out and i > 5:
        print("You made it out!");
        break;
    elif choice == out and i < 5:
        print("You found treasure! But no exit.");
    else:
        if choice == "A":
            space = ' '*5
            character = "&"
            position = space + character;
        elif choice == "S":
            space = '.'*27
            character = ' #         #' + '.'*25 + ' \n' + space + ' #         #' + '.'*25 + ' \n' + space + ' #    &    #' + '.'*25;
            position = space + character;
        elif choice == "D":
            space = ' '*50
            character = "&"
            position = space + character;
        else: 
            print("Uh oh. Invalid Choice. Try Again!");
        print("You dig deeper")
        print('Oxygen Level: ' + str(oxlvl) + '%');
    if oxlvl == 0:
        print('You die cold and alone in the dark.')
        break;
print("GAME OVER!");