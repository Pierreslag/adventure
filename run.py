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
    choise = input("A/B?:> ")
    return choise


# Step 2 functions.

def step2(player_name):
    print(f"{player_name}, you find an apartment building with a barricaded entrance.")
    print("What will you do?")
    print("A. Attempt to break through the barricade (Leads to step 3)")
    print("B. Search for another way inside (Leads to Disaster 2)")
    choise = input("A/B?:> ")
    return choise


# Main game logics

def main():
    player_name = intro()
    choise = step1()
    if choise.upper() == "A":
        print("While you're hiding in the car, the zombies notice you and swarm the vehicle.")
        print("The windows shatter, and they pull you out of the car. Game over.")
    elif choise.upper() == "B":
        choice = step2(player_name)
        if choice.upper() == "A":
            print("STEP 3")
        elif choice.upper() == "B":
            print("You find a basement entrance, but it's flooded. A hidden zombie bites you. Game over.")
        else:
            print("A or B only. Please try again.")
    else:
        print("A or B only. Please try again.")

# Checker

if __name__ == "__main__":
    main()