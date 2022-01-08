import random

#global vars
spot1 = "Car"
spot2 = "Goat"
spot3 = "Goat"
spots = [spot1, spot2, spot3]
doors = """
    |-----------|   |-----------|   |-----------|
    |           |   |           |   |           |
    |           |   |           |   |           |
    |     1     |   |     2     |   |     3     |
    |           |   |           |   |           |
    |           |   |           |   |           |
    |-----------|   |-----------|   |-----------|
    """

def spotDoor():
    global door1
    spotChosen = random.randint(0,2)
    door1 = spots[spotChosen]
    spots.pop(spotChosen)
    global door2
    spotChosen = random.randint(0,1)
    door2 = spots[spotChosen]
    spots.pop(spotChosen)
    global door3
    door3 = spots[0]
    spots.pop(0)

def userFirstChoice():
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