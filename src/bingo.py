import numpy as np
from random import choice, randint
from numpy.core.fromnumeric import diagonal
import time


def bingo_game():

    c = np.random.randint(1, 76, size=(5, 5))
    c[2, 2] = 0
    print("The Bingo Board ⬇️\n\n")
    print(f"{c}\n\n")

    max_tries = 50
    tries = 0
    out_of_tries = False
    nums = []
    win_con = np.array([0, 0, 0, 0, 0])
    stuffs = [c[0, :], c[1, :], c[2, :], c[3, :], c[4, :],
              c[:, 0], c[:, 1], c[:, 2], c[:, 3], c[:, 4], diagonal(c), diagonal(c[::-1])]
    won = False

    while not(out_of_tries) and not(won):
        if tries < max_tries:
            num = choice([i for i in range(1, 76) if i not in nums])
            nums.append(num)
            if num in c:
                print(f"Rolled: {num}  💮")
            else:
                print(f"Rolled: {num} ")
            tries += 1
            if num in c:
                for i in range(len(c)):
                    for j in range(len(c[i])):
                        if c[i][j] == num:
                            c[i, j] = 0
            time.sleep(0.1)
            for i in stuffs:
                if (i == win_con).all():
                    print("\n\nBingo! 🥳 \n\n")
                    print(c)
                    won = True
                    break

        else:
            out_of_tries = True
            print("Not Bingo... 😔")
            print(c)


bingo_game()
input()
