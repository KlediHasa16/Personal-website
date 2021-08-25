from random import randint


def game():
    scenario1 = "tails"
    scenario2 = "head"
    n = randint(1, 2)

    placeholder1 = input("Choose Head/Tails:")

    if n == 1:
        print(f"You: {placeholder1}\nCoin: {scenario1}")
        if scenario1 == placeholder1.lower():
            print("You won!")
        elif scenario2 == placeholder1.lower():
            print("You Lose!")
        else:
            print("Invalid Input, Try again.")
            game()
    else:
        print(f"You: {placeholder1}\n Coin: {scenario2}")
        if scenario2 == placeholder1.lower():
            print("You won!")
        elif scenario1 == placeholder1.lower():
            print("You Lose!")
        else:
            print("Invalid Input!")
            game()


game()

while True:
    a = input("Play again Y/N?:")
    if a.lower() == "n":
        print("Ok,cool :C")
        break
    elif a.lower() == "y":
        game()
