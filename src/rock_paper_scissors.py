from random import randint
print("Welcome to the game of Rock/Paper/Scissors!")


def game():

    n2 = input("Rock,Paper or Scissors:")
    print("You : " + n2)
    possible_picks = ["rock", "paper", "scissors"]
    n1 = randint(1, 3)
    if n1 == 1:
        print("Enemy : Rock")
        n1 = "Rock"
    elif n1 == 2:
        print("Enemy : Paper")
        n1 = "Paper"
    else:
        print("Enemy : Scissors")
        n1 = "Scissors"

    if n2.lower() in possible_picks:
        if n2.lower() == "rock" and n1.lower() == "rock":
            print("Tie.")
        elif n2.lower() == "rock" and n1.lower() == "scissors":
            print("You win!")
        elif n2.lower() == "rock" and n1.lower() == "paper":
            print("You lose!")
        if n2.lower() == "paper" and n1.lower() == "paper":
            print("Tie.")
        elif n2.lower() == "paper" and n1.lower() == "rock":
            print("You win!")
        elif n2.lower() == "paper" and n1.lower() == "scissors":
            print("You lose!")
        if n2.lower() == "scissors" and n1.lower() == "scissors":
            print("Tie.")
        elif n2.lower() == "scissors" and n1.lower() == "paper":
            win = "true"
            print("You win!")
        elif n2.lower() == "scissors" and n1.lower() == "rock":
            print("You lose!")


game()

while True:
    a = input("Do you want to play again? (Y/N):")
    if a.lower() == "y":
        game()
    elif a.lower() == "n":
        print("Bye!")
        break
