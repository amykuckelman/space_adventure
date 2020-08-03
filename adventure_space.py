import time
import random


# this is where you will collect your items during game-play
your_list = []

alien_creatures = ["Bog-smorfer", "Gorgonmorpher", "Orion-Beetlelorgon"]
space_weapons = ["Lazer-Blaster", "Light-sword", "Speed-of-light Hammer"]


global random_alien
global space_weapon
random_alien = random.choice(alien_creatures)
space_weapon = random.choice(space_weapons)


# this will print everything in a timely order not all at once
def print_pause(print_info):
    print(print_info)
    time.sleep(2)


# this will let the player make decisions using two options given
# they can enter wrong imput but will be printed a response
def correct_input(question, op1, op2):
    while True:
        decision = input(question).lower()
        if op1 == decision:
            break
        elif op2 == decision:
            break
        else:
            print_pause("That is not an option.")
    return decision


# this is the intro tells the player where we are
def begin():
    print_pause("You have just landed on Mars.")
    print_pause("Your mission is to terminate an aggressive \n"
                + random_alien + " that has been terrorizing\n"
                "the native creatures on this planet.")
    print_pause("There is a crater ahead of you.")
    print_pause("To your left is a local pawn shop.")


def choose_route():
    decision = correct_input("Would you like to go to the crater[1]\n"
                             "Or the pawn shop[2]?\n", "1", "2")
    if "1" in decision:
        print_pause("You walk toward the crater. \nAt the bottom you "
                    "see a large structure.")
        print_pause("As you approach \nyou trip on some space "
                    "rocks.")
        print_pause("When you gather yourself, \nyou realize the "
                    + random_alien + " is standing before you.")
        print_pause("You can see their anger streaming out of"
                    " every pore!")
        what_next()
    else:
        pawn_shop()


# this definition will decide if you want to stay and fight the alien
# or run back to your space ship
def what_next():
    decision = correct_input("Would you like to fight off the creature?\n"
                             "Or you can run back to your space ship.\n"
                             "type [1] to fight, or [2] to run!\n", "1", "2")
    if "1" in decision:
        alien_crater()
    else:
        print_pause("You run back to your spaceship!")
        choose_route()


# you will collect your weapon here unless you have been here before
def pawn_shop():
    print_pause("You walk up to the entryway.")
    if "space_weapon" in your_list:
        print_pause("You have already collected what you need.")
        choose_route()
    else:
        print_pause("A small martian greets you, \n"
                    "He says its your lucky day!")
        print_pause("He points toward an illuminated platform. \n"
                    "On this platform you see an object.")
        print_pause("The martian informs you that they have \n"
                    "been waiting for you.")
        print_pause("He then gives you the " + space_weapon + ".")
        print_pause("He points you back to your ship and wishes you well.")
        your_list.append("space_weapon")
        choose_route()


# things that happen in the crater
def alien_crater():
    if "space_weapon" in your_list:
        print_pause("You prepare yourself as the " + random_alien +
                    " rushes toward you!")
        print_pause("You pull out your " + space_weapon + ", the "
                    + random_alien + "\n"
                    "sees your deadly new toy and \n"
                    "races back to the safety of their home.")
        print_pause("You realize that killing this pathetic creature")
        print_pause("would be the wrong decision.")
        print_pause("By scaring the " + random_alien + " away ")
        print_pause("you have saved the martians!!!")
        print_pause("You are victorious!")
    else:
        print_pause("You try to fight, but without any weapons \nthe angry "
                    + random_alien + " rips a hole \nin your space suit.")
        print_pause("You Lose!!")


# this code will be to restart or end game.
def try_again():
    decision = correct_input("Play again?\n"
                             "Type [yes] or [no].\n", "yes", "no")
    if "yes" in decision:
        print_pause("You will be arriving in...")
        print_pause("3")
        print_pause("2")
        print_pause("1")
        go_to_space()
    else:
        print_pause("Live long and prosper (^_^)/ ")


# this will start the game over with new random variables
def go_to_space():
    your_list.clear()
    global random_alien
    global space_weapon
    random_alien = random.choice(alien_creatures)
    space_weapon = random.choice(space_weapons)
    begin()
    choose_route()
    try_again()


if __name__ == "__main__":
    go_to_space()
# this code was written from scratch using the lessons learned
# in Udacity's program
