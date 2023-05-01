def intro():
    print("Welcome to the Zombie Apocalypse outbreak adventure.")
    print("Here you will play as a survivor in a world filled with zombies.")
    name = input("To begin, please enter your adventurer's name: ")
    return name

def step1():
    print("You wake up in a wrecked car and realize the world has changed.")
    print("Zombies roam the streets. You need to escape and find a safe place to hide.")
    print("What will you do?")
    print("A. Stay in the car, hoping the zombies don't notice you")
    print("B. Leave the car and search for a nearby building for shelter.")
    choise = input("A/B?:> ")
    return choise

def main():
    player_name = intro()
    choise = step1()
    if choise.upper() == "A":
        print("Disaster 1")
    elif choise.upper() == "B":
        print("YOU WILL GO STEP 2 HERE")
    else:
        print("A or B only. Please try again.")

if __name__ == "__main__":
    main()