"""
Zombie Apocalypse outbreak game
"""


class Player:
    """
    Player class score and name register
    """
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_points(self, points):
        """
        Adds the points to the player score
        """
        self.score += points

    def get_score(self):
        """
        Return player score or not if score is zero.
        """
        if self.score > 0:
            return self.score
        else:
            return None


# Welcome message and adventure name input.

def intro():
    """
    Welcomes the player and asks for the adventurers name
    """
    print("Welcome to the Zombie Apocalypse outbreak adventure.")
    print("Here you will play as a survivor in a world filled with zombies.")
    name = input("To begin, please enter your adventurer's name: ")
    return Player(name)


# Step 1 functions.

def step1(player):
    """
    First scenario presented here.
    """
    print("You wake up in a wrecked car and realize the world has changed.")
    print("Zombies roam the streets.")
    print("You need to escape and find a safe place to hide.")
    print("What will you do?")
    print("A. Stay in the car, hoping the zombies don't notice you")
    print("B. Leave the car and search for a nearby building for shelter.")
    while True:
        choice = input("A/B?:> ")
        if choice.upper() in ["A", "B"]:
            if choice.upper() == "B":
                player.add_points(10)
            return choice
        else:
            print("A or B only. Please try again.")


# Step 2 functions.

def step2(player):
    """
    Second scenario presented here.
    """
    print(f"{player.name}, you find an building with a barricaded entrance.")
    print("What will you do?")
    print("A. Attempt to break through the barricade")
    print("B. Search for another way inside")
    while True:
        choice = input("A/B?:> ")
        if choice.upper() in ["A", "B"]:
            if choice.upper() == "A":
                player.add_points(10)
            return choice
        else:
            print("A or B only. Please try again.")


# Step 3 functions.

def step3(player):
    """
    Third scenario presented here.
    """
    print("Having broken through the barricade, \n"
          "you find yourself in a dimmed lit hallway.")
    print(f"What will you do {player.name} ?")
    print("A. Proceed down the hallway, searching for a safe room")
    print("B. Go back outside and look for a different building")
    while True:
        choice = input("A/B?:> ")
        if choice.upper() in ["A", "B"]:
            if choice.upper() == "A":
                player.add_points(10)
            return choice
        else:
            print("A or B only. Please try again.")


# Step 4 functions.

def step4(player):
    """
    Fourth scenario presented here.
    """
    print(f"{player.name}, you discover an empty apartment with a \n"
          "reinforced door.")
    print("You lock yourself inside.")
    print("Exploring the apartment, \n"
          "you find a well-stocked pantry and medical supplies.")
    print("What will you do?")
    print("A. Remain in the apartment and utilize the supplies")
    print("B. Leave the apartment to search for more resources")
    while True:
        choice = input("A/B?:> ")
        if choice.upper() in ["A", "B"]:
            if choice.upper() == "A":
                player.add_points(10)
            return choice
        else:
            print("A or B only. Please try again.")


# Step 5 functions

def step5(player):
    """
    Fifth scenario presented here.
    """
    print("You decide to stay and take advantage of the supplies.")
    print("While resting, a faint knock on the door catches your attention.")
    print("Cautiously, you open it to find a small group of survivors \n"
          "seeking refuge.")
    print(f"What will you do {player.name} ?")
    print("A. Invite the survivors in and join forces")
    print("B. Turn the survivors away, fearing they may pose a threat")
    while True:
        choice = input("A/B?:> ")
        if choice.upper() in ["A", "B"]:
            if choice.upper() == "A":
                player.add_points(10)
            return choice
        else:
            print("A or B only. Please try again.")


# Step 6 winstage

def step6(player):
    """
    Winstage scenario presented here.
    """
    print("Congratulations!")
    print("You have successfully completed the game and found a safe place.")
    print("And formed a team of survivors.")
    print("Together, you are now prepared to face the challenges of \n"
          "the Zombie Apocalypse.")
    print("And work towards rebuilding society.")

    score = player.get_score()
    if score is not None:
        print(f"Final score: {score}")


# Replay function

def replay():
    """
    This function asks for replay if adventurer dies or complete.
    """
    choice = input("Replay? (Y/N)> ")
    return choice.upper() == "Y"


# Lose function
def lose(message):
    """
    Function for print message game over if player lose.
    """
    print(message)
    print("Game over.")


# Main gamelogics

def main():
    """
    This is the main function and logics for the game.
    """
    while True:
        player = intro()
        choice = step1(player)
        if choice.upper() == "A":
            lose("While hiding in the car, zombies notice you, \n"
                 "swarm the vehicle, and pull you out.")
        elif choice.upper() == "B":
            choice = step2(player)
            if choice.upper() == "A":
                choice = step3(player)
                if choice.upper() == "A":
                    choice = step4(player)
                    if choice.upper() == "A":
                        choice = step5(player)
                        if choice.upper() == "A":
                            step6(player)
                        elif choice.upper() == "B":
                            lose("After turning the survivors away, \n"
                                 "they target you for retribution.")
                    elif choice.upper() == "B":
                        lose("As you leave, bandits take your supplies, \n"
                             "leaving you helpless.")
                    else:
                        print("A or B only. Please try again.")
                elif choice.upper() == "B":
                    lose("As you search, a horde of zombies surrounds you.")
                else:
                    print("A or B only. Please try again.")
            elif choice.upper() == "B":
                lose("You find a flooded basement entrance \n"
                     "and get bitten by a hidden zombie.")
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
