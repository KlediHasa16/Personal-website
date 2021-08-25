from random import randint


def dicer():

    while True:

        dicu = randint(1, 6)
        dice2 = randint(1, 6)
        win = 25
        move = dicu + dice2
        print(dicu)
        print(dice2)

        print("You moved " + str(move) + " squares.")
        c = move
        b = input("Press Enter to roll the dices again")

        if b == "":
            dicu = randint(1, 6)
            dice2 = randint(1, 6)
            print(dicu)
            print(dice2)
            move = dicu + dice2
            print("You moved " + str(move) + " squares.")
            g = c + move
            print("You are at square " + str(g) + " . ")
            d = input("Press Enter to roll the dices again")

            if d == "":
                dicu = randint(1, 6)
                dice2 = randint(1, 6)
                print(dicu)
                print(dice2)
                move = dicu + dice2
                print("You moved " + str(move) + " squares.")
                z = g + move
                print("You are at square " + str(z) + " . ")

                if z == 36:
                    print("You got the highest possible number, SHEEESH.")
                    break
                elif z >= win:
                    print("GG BRO! You won the game!!")
                    break
                else:
                    print("You didnt arrive at the finish. You Lost!!")
                    break

            else:
                print("Invalid output")
                break

        else:
            print("Invalid output")
            break


b = input("Press Enter to start the game and roll the dices :)")
if b == "":
    dicer()
else:
    print("Invalid input")

while True:
    a = input("Would you like to play again? (Y/N):")
    if a.lower() == "n":
        print("Ok,cool :C")
        break
    elif a.lower() == "y":
        dicer
