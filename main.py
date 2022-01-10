import random

#global vars
spots = ["GOAT", "GOAT", "CAR"]
doors = ["door1", "door2", "door3"]
doorsVisual = """
    |-----------|   |-----------|   |-----------|
    |           |   |           |   |           |
    |           |   |           |   |           |
    |     1     |   |     2     |   |     3     |
    |           |   |           |   |           |
    |           |   |           |   |           |
    |-----------|   |-----------|   |-----------|
    """

def spotDoor():
    #door1
    spotChosen = random.randint(0, 2)
    doors[0] = spots[spotChosen]
    spots.pop(spotChosen)
    #door2
    spotChosen = random.randint(0,1)
    doors[1] = spots[spotChosen]
    spots.pop(spotChosen)
    #door3
    doors[2] = spots[0]
    spots.pop(0)


def userFirstChoice():
    print(doorsVisual)
    global selectedDoor
    #input-check
    while True:
        try:
            print("which doors would you like to open?")
            selectedDoor = int(input())
        except:
            print("Please enter an integer from 1 to 3")
            continue
        if  selectedDoor >= 1 and selectedDoor <= 3:
            break
        else:
            print("Please enter an integer from 1 to 3")
            continue
    selectedDoor -= 1

def reveal():
    global revealedDoor
    revealedDoor = random.randint(0,2)
    while revealedDoor == selectedDoor or doors[revealedDoor] == "CAR":
        revealedDoor = random.randint(0,2)
    global doorsVisual
    doorsVisual = doorsVisual.replace(("|     " + str(revealedDoor+1) + "     |"), "|    GOAT   |")
    print(doorsVisual)
    print("There is a" + doors[revealedDoor] + "behind the door number" + str(revealedDoor + 1))
    print("Would you like to swtich? y/n")
    global switch
    switch = str(input())
    while switch != "y" and switch != "n":
        print("Please enter y for yes or n for no")
        switch = str(input())
    if switch == "y":
        switch = True
    else: switch = False

def switchingDoor(switch):
    if switch == True:
        global switchTo
        switchTo = random.randint(0,2)
        while switchTo == revealedDoor or switchTo == selectedDoor:
            switchTo = random.randint(0,2)
        print("There is a " + doors[switchTo] + "behind the door number " + str(switchTo+1))
        global doorsVisual
        if doors[switchTo] == "CAR":
            doorsVisual = doorsVisual.replace(("|     " + str(switchTo+1) + "     |"), "|    CAR    |")
            doorsVisual = doorsVisual.replace(("|     " + str(selectedDoor+1) + "     |"), "|    GOAT   |")
            print(doorsVisual)
            print('')
            print("You Won!")
        else:
            doorsVisual = doorsVisual.replace(("|     " + str(selectedDoor+1) + "     |"), "|    CAR    |")
            doorsVisual = doorsVisual.replace(("|     " + str(switchTo+1) + "     |"), "|    GOAT   |")
            print(doorsVisual)
            print('')
            print("You Suck")



#Game Loop
spotDoor()
userFirstChoice()
reveal()
switchingDoor(switch)