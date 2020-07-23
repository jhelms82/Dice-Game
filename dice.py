import random
import time

#Have each player enter their game at the start of the game
user1 = input("Player 1 please enter your name: ")
print()
user2 = input("Player 2 please enter your name: ")
print()

#Main function starts game with each player starting with 0 points
def main():
    player1 = 0
    player1Wins = 0
    player2 = 0
    player2Wins = 0
    rounds = 1

#While loop going for 7 rounds, input 2 seconds between each player roll, 
    while rounds != 8:
        time.sleep(1)
        print("Round " + str(rounds) + ":")
        print()
        time.sleep(2)
        player1 = dice_roll()
        player2 = dice_roll()
        print(user1 + " Roll: " + str(player1))
        time.sleep(2)
        print(user2 + " Roll: " + str(player2))

#Function for each outcome with a 3 second delay 
        if player1 == player2:
            time.sleep(3)
            print()
            print("Draw!")
            print()
        elif player1 > player2:
            time.sleep(3)
            player1Wins = player1Wins +1
            print()
            print(user2 + " wins!")
            print()
        else:
            time.sleep(3)
            player2Wins = player2Wins +1
            print()
            print(user2 + " wins!")
            print()

        rounds = rounds + 1

 #End of all the rounds with print statement for each scernio    
    if player1Wins == player2Wins:
        time.sleep(2)
        print("This game is a draw!")
        print()
    elif player1 > player2:
        time.sleep(2)
        print(user1 + " wins! Rounds won: " + str(player1Wins))
        print()
    else:
        time.sleep(2)
        print(user2 + " wins! Rounds won: " + str(player2Wins))
        print()

#A while loop if they want to play again or not
    while True:
        retry = input("Would you like to play again? (yes or no) : ")
        if retry.upper() == "YES":
            main()
        if retry.upper() == "NO":
            exit()
        else:
            print("I'm sorry I could not recognize what you entered")

#function to roll the dice with the setup of random number 1 through 6
def dice_roll():
    diceRoll  = random.randint(1,6)
    return diceRoll

main()

