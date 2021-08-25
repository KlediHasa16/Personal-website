from random import randint

while True:
    num1 = randint(1, 10)
    print("Welcome to the game where you need to guess a random number from 1 to 10")
    if (num1 % 2) == 0:
        print("The number is even")
    elif (num1 % 2) != 0:
        print("The number is odd")
    guesses = 0
    num2 = ""
    guess_limit = 3
    out_of_guesses = False

    while num2 != num1 and not(out_of_guesses):
        if guesses < guess_limit:
            num2 = input("Enter a number:")
            num2 = int(num2)
            guesses += 1
            if num2 != num1:
                print("Incorrect guess")

        else:
            out_of_guesses = True

    print("The number was " + str(num1) + ".")
    if num2 == num1:
        print("You win!")
        if input("Do you want to play again? Y/N") == "n":
            break
    else:
        print("You lose!")
        if input("Do you want to play again? Y/N") == "n":
            break
