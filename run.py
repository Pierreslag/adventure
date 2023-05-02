# Welcome message and character name input

def intro():
    print("Welcome to the Zombie Apocalypse outbreak adventure.")
    print("Here you will play as a survivor in a world filled with zombies.")
    name = input("To begin, please enter your adventurer's name: ")
    return name


# Step 1 functions.

def step1():
    print("You wake up in a wrecked car and realize the world has changed.")
    print("Zombies roam the streets. You need to escape and find a safe place to hide.")
    print("What will you do?")
    print("A. Stay in the car, hoping the zombies don't notice you")
    print("B. Leave the car and search for a nearby building for shelter.")
    choice = input("A/B?:> ")
    return choice


# Step 2 functions.

def step2(player_name):
    print(f"{player_name}, you find an apartment building with a barricaded entrance.")
    print("What will you do?")
    print("A. Attempt to break through the barricade")
    print("B. Search for another way inside")
    choice = input("A/B?:> ")
    return choice


# Ste 3 function

def step3(player_name):
    print("Having broken through the barricade, you find yourself in a dimmed lit hallway.")
    print("What will you do?")
    print("A. Proceed down the hallway, searching for a safe room (Leads to Step 4)")
    print("B. Go back outside and look for a different building (Leads to Disaster 3)")
    choice = input("A/B?:> ")
    return choice

# Main game logics

def main():
    player_name = intro()
    choice = step1()
    if choice.upper() == "A":
        print("While you're hiding in the car, the zombies notice you and swarm the vehicle.")
        print("The windows shatter, and they pull you out of the car. Game over.")
    elif choice.upper() == "B":
        choice = step2(player_name)
        if choice.upper() == "A":
            choice = step3(player_name)
        elif choice.upper() == "B":
            print("You find a basement entrance, but it's flooded. A hidden zombie bites you. Game over.")
        else:
            print("A or B only. Please try again.")
    else:
        print("A or B only. Please try again.")

# Checker

if __name__ == "__main__":
    main()