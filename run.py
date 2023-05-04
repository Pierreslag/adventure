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
    while True:    
        choice = input("A/B?:> ")
        if choice.upper() in ["A", "B"]:
            return choice
        else:
            print("A or B only. Please try again.")


# Step 2 functions.

def step2(player_name):
    print(f"{player_name}, you find an apartment building with a barricaded entrance.")
    print("What will you do?")
    print("A. Attempt to break through the barricade")
    print("B. Search for another way inside")
    while True:    
        choice = input("A/B?:> ")
        if choice.upper() in ["A", "B"]:
            return choice
        else:
            print("A or B only. Please try again.")


# Step 3 functions.

def step3(player_name):
    print("Having broken through the barricade, you find yourself in a dimmed lit hallway.")
    print(f"What will you do {player_name} ?")
    print("A. Proceed down the hallway, searching for a safe room")
    print("B. Go back outside and look for a different building")
    while True:    
        choice = input("A/B?:> ")
        if choice.upper() in ["A", "B"]:
            return choice
        else:
            print("A or B only. Please try again.")


# Step 4 functions.

def step4(player_name):
    print(f"{player_name}, you discover an empty apartment with a reinforced door.")
    print("You lock yourself inside.")
    print("Exploring the apartment, you find a well-stocked pantry and medical supplies.")
    print("What will you do?")
    print("A. Remain in the apartment and utilize the supplies")
    print("B. Leave the apartment to search for more resources")
    while True:    
        choice = input("A/B?:> ")
        if choice.upper() in ["A", "B"]:
            return choice
        else:
            print("A or B only. Please try again.")


# Step 5 functions

def step5(player_name):
    print("You decide to stay and take advantage of the supplies.")
    print("While resting, a faint knock on the door catches your attention.")
    print("Cautiously, you open it to find a small group of survivors seeking refuge.")
    print(f"What will you do {player_name} ?")
    print("A. Invite the survivors in and join forces")
    print("B. Turn the survivors away, fearing they may pose a threat")
    while True:    
        choice = input("A/B?:> ")
        if choice.upper() in ["A", "B"]:
            return choice
        else:
            print("A or B only. Please try again.")


# Step 6 winstage

def step6():
    print("Congratulations!")
    print("You have successfully completed the game and found a safe place.")
    print("And formed a team of survivors.")
    print("Together, you are now prepared to face the challenges of the Zombie Apocalypse.")
    print("And work towards rebuilding society.")


# Replay function

def replay():
    choice = input("Replay? (Y/N)> ")
    return choice.upper() == "Y"


# Lose function
def lose(message):
    print(message)
    print("Game over.")



# Main game logics

def main():
    while True:
        player_name = intro()
        choice = step1()
        if choice.upper() == "A":
            lose("While hiding in the car, zombies notice you, swarm the vehicle, and pull you out.")
        elif choice.upper() == "B":
            choice = step2(player_name)
            if choice.upper() == "A":
                choice = step3(player_name)
                if choice.upper() == "A":
                    choice = step4(player_name)
                    if choice.upper() == "A":
                        choice = step5(player_name)
                        if choice.upper() == "A":
                            step6()
                            if not replay():
                                print("Thanks for playing!.")
                                break
                        elif choice.upper() == "B":
                            lose("After turning the survivors away, they target you for retribution.")
                    elif choice.upper() == "B":
                        lose("As you leave, bandits take your supplies, leaving you helpless.")
                    else:
                        print("A or B only. Please try again.")
                elif choice.upper() == "B":
                    lose("As you search, a horde of zombies spots and surrounds you.")
                else:
                    print("A or B only. Please try again.")
            elif choice.upper() == "B":
                lose("You find a flooded basement entrance and get bitten by a hidden zombie.")
            else:
                print("A or B only. Please try again.")
        else:
            print("A or B only. Please try again.")

        if not replay():
            print("Thanks for playing! Bye!")
            break

# Checker

if __name__ == "__main__":
    main()
