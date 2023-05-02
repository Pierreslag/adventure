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


# Step 3 functions.

def step3(player_name):
    print("Having broken through the barricade, you find yourself in a dimmed lit hallway.")
    print(f"What will you do {player_name} ?")
    print("A. Proceed down the hallway, searching for a safe room")
    print("B. Go back outside and look for a different building")
    choice = input("A/B?:> ")
    return choice


# Step 4 functions.

def step4(player_name):
    print(f"{player_name}, you discover an empty apartment with a reinforced door and lock yourself inside.")
    print("Exploring the apartment, you find a well-stocked pantry and medical supplies.")
    print("What will you do?")
    print("A. Remain in the apartment and utilize the supplies")
    print("B. Leave the apartment to search for more resources")
    choice = input("A/B?:> ")
    return choice


# Step 5 functions

def step5(player_name):
    print("You decide to stay and take advantage of the supplies.")
    print("While resting, a faint knock on the door catches your attention.")
    print("Cautiously, you open it to find a small group of survivors seeking refuge.")
    print(f"What will you do {player_name} ?")
    print("A. Invite the survivors in and join forces (Leads to step 6)")
    print("B. Turn the survivors away, fearing they may pose a threat (Leads to Disaster 5)")
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
            if choice.upper() == "A":
                choice = step4(player_name)
                if choice.upper() == "A":
                    print("STEP 5")
                elif choice.upper() == "B":
                    print("As you leave the apartment, you stumble upon a group of bandits.")
                    print("They take all your supplies!")
                    print("Leaving you injured and defenseless against the encroaching zombies. Game over.")
                else:
                    print("A or B only. Please try again.")
            elif choice.upper() == "B":
                print("As you search for another building, a horde of zombies spots you.")
                print("With no place to hide, the zombies quickly surround you. Game over.")
            else:
                print("A or B only. Please try again.")
        elif choice.upper() == "B":
            print("You find a basement entrance, but it's flooded.")
            print("A hidden zombie bites you. Game over.")
        else:
            print("A or B only. Please try again.")
    else:
        print("A or B only. Please try again.")


# Checker

if __name__ == "__main__":
    main()