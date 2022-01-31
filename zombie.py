import random

def zonbue(looting):
    num = random.randrange(1, 1000)
    if looting == 0:
        if num < 25:
            print ("Zombie dropped an iron ingot")
        elif num < 50:
            print ("zombie dropped potato")
        elif num < 75:
            print ("Zombie dropped carrot")
        else:
            if num < 333:
                print ("You got 0 rotten flesh")
            elif num < 666:
                print("You got 1 rotten flesh")
            else:
                print("You got 2 rotten flesh")
    if looting == 1:
        if num < 35:
            print ("Zombie dropped an iron ingot")
        elif num < 60:
            print ("zombie drop potato")
        elif num < 85:
            print("zombie dropped carrot")
        else:
            if num < 333:
                print ("You got 0 rotten flesh")
            elif num < 666:
                print("You got 1 rotten flesh")
            else:
                print("You got 2 rotten flesh")
    if looting == 2:
        if num < 45:
            print ("Zombie dropped an iron ingot")
        elif num < 70:
            print ("zombie drop potato")
        elif num < 95:
            print("zombie dropped carrot")
        else:
            if num < 333:
                print ("You got 0 rotten flesh")
            elif num < 666:
                print("You got 1 rotten flesh")
            else:
                print("You got 2 rotten flesh")
    if looting == 3:
        if num < 55:
            print ("Zombie dropped an iron ingot")
        elif num < 80:
            print ("zombie drop potato")
        elif num < 105:
            print("zombie dropped carrot")
        else:
            if num < 333:
                print ("You got 0 rotten flesh")
            elif num < 666:
                print("You got 1 rotten flesh")
            else:
                print("You got 2 rotten flesh")
choice = 'a'
while choice != 'q':
    print("Enter looting level or q to quit")
    choice = input()
    if choice != 'q':
        zonbue(int (choice))
