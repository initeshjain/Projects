# This is Stone Paper Scissor Game made in Python.
# Using Only Random Module.
# GUI version Releasing Soon.


import random

def wrong_input():
    print("Oops Wrong Input - Try Again.")
    
def rOre():
    replay = input("\n\nPress R for Replay and \n E for Exit: ").lower()
    if replay == 'r':
        operation()
    elif replay == 'e':
        exit()
    else:
        wrong_input()
        rOre()
        
def operation():
    global i, chances, computer_points, player_points
    while(i < chances):
        print("--------------------------------------------------------------------")
        raw_input = input("\nEnter a Choice: ").lower()
        if raw_input == 's':
            player_input = "stone"
        elif raw_input == 'p':
            player_input = "paper"
        elif raw_input == 'r':
            player_input = "scissor"
        else:
            rOre()     

        computer_guess = (random.choice(list))

        if player_input == 'stone' and  computer_guess == 'paper':
            print("\nComputer Chooses = ", computer_guess)
            print("You Chooses = ", player_input)
            print("\nComputer Wins")
            computer_points = computer_points + 1 
            print("Your Points = ", player_points)
            print("Computer chooses = ", computer_points)

        elif player_input == 'paper' and  computer_guess == 'stone':
            print("\nComputer Chooses = ", computer_guess)
            print("You Chooses = ", player_input)
            print("\nYou Wins")
            player_points = player_points + 1 
            print("Your Points = ", player_points)
            print("Computer chooses = ", computer_points)
            
        elif player_input == 'scissor' and  computer_guess == 'paper':
            print("\nComputer Chooses = ", computer_guess)
            print("You Chooses = ", player_input)
            print("\nYou Wins")
            player_points = player_points + 1 
            print("Your Points = ", player_points)
            print("Computer chooses = ", computer_points)

        elif player_input == 'paper' and  computer_guess == 'scissor':
            print("\nComputer Chooses = ", computer_guess)
            print("You Chooses = ", player_input)
            print("\nComputer Wins")
            computer_points = computer_points + 1 
            print("Your Points = ", player_points)
            print("Computer chooses = ", computer_points)

        elif player_input == 'stone' and  computer_guess == 'scissor':
            print("\nComputer Chooses = ", computer_guess)
            print("You Chooses = ", player_input)
            print("\nYou Wins")
            player_points = player_points + 1 
            print("Your Points = ", player_points)
            print("Computer chooses = ", computer_points)

        elif player_input == 'scissor' and  computer_guess == 'stone':
            print("\nComputer Chooses = ", computer_guess)
            print("You Chooses = ", player_input)
            print("\nComputer Wins")
            computer_points = computer_points + 1 
            print("Your Points = ", player_points)
            print("Computer chooses = ", computer_points)

        elif player_input == computer_guess:
            print("\nComputer Chooses = ", computer_guess)
            print("You Chooses = ", player_input)
            print("\nChance DRAW \n Both Chooses Same.\n")
            print("Your Points = ", player_points)
            print("Computer chooses = ", computer_points)

        else:
            print(" Please Replay the game - Something Went Wrong.")
            break
        
        i = i + 1

    if computer_points > player_points:
        print("\n Sorry Better Luck Next Time")
        print("Computer Wins the Game")
        print("You Loose")

    elif computer_points == player_points:
        print("\nMatch Draw.")

    else:
        print("\n You Got it My Boi.")
        print("You Wins the Game")
        print("Computer Loose")
        
def spsgame():
    print("The Stone, Paper, Scissor Game\n")
    print("Read This\n")
    print("You got", chances, "chances so make choice as: \nStone = s \nPaper = p \nScissor = r\n")
    operation()

list=["paper","stone","scissor","paper","stone","scissor","paper","stone","scissor"]
chances = 10
i = 0
computer_points = 0
player_points = 0  
spsgame()
rOre()
a = input()
     
# End
