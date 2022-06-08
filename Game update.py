# James Saward-Anderson
# A Nightmare In Space
# description: Text-based space adventure game

import random
import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1.8)


def displayIntro():
    print_pause("Your starship emerges from warp speed")
    print_pause("you are now in a new star system")
    print_pause("Up ahead you see two worm holes")
    string = "One leads to home planet and the other leads to a black hole"
    print_pause(string)
    print()


def main_choice():
    print_pause("What do you want to do next? Please enter number:")
    choice = valid_input("1. Go down the left wormhole \n"
                         "2. Go down the right wormhole\n")
    if choice == '1':
        fight_intro()
    else:
        flee_intro()


def fight_intro():
    print_pause("You travel down the wormhole.")
    print_pause("Everything is speeding up!")
    print_pause("You hear a noise!")
    print_pause("'A monster from the warp emerges! "
                "The Monster begins to attack your ship!")


def flee_intro():
    print_pause("You travel to your home world.")
    print_pause("You can see so many sights!")
    print_pause("But you gasp, your planet is burning!")
    print_pause("'A beast from hell is attacking it! "
                "The Monster turns its sights and attacks!")


def valid_input(message):
    user_input = input(message)
    while user_input != "1" and user_input != "2":
        user_input = input(message)
    return user_input


def choosePath():
    path = valid_input("How do you defend your ship? (1 or 2): ")
    return path


def checkPath(chosenPath):
    print("You attack the monster with a ray gun")
    time.sleep(2)
    print("The monster smashes your ship...")
    time.sleep(2)
    print("The ships hull begins to shake...")
    print()
    time.sleep(2)

    correctPath = random.randint(1, 2)

    if chosenPath == str(correctPath):
        print("You return fire and the monster flees!")
        print("You can travel onwards to saftey!")
    else:
        print("The ship begins to split apart")
        print("causing all of the atoms in your body to dissociate")
        print("there is no record left of your existence.")


playAgain = "1"
while playAgain == "1":
    displayIntro()
    main_choice()
    choice = choosePath()
    checkPath(choice)  # choice is equal to "1" or "2"
    string = "Play again?(enter 1 to continue playing or 2 to stop): "
    playAgain = valid_input(string)
