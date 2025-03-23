from random import randint
from random import random as r

maxnum = 100
print("Give me a number, 1-" + str(maxnum) + " and I'll guess it")
ans = input()
ans = int(ans)
computer_guess = randint(1, maxnum)
lownum = 1
highnum = maxnum

while True:
    clue = input("Is this hot or cold " + str(computer_guess) + ": ")
    if clue == ans:
        print("You got it!!!")
        break
    if clue == "hot":
        lownum = max(1, computer_guess - 10)  # Ensure lownum is at least 1
        highnum = min(maxnum, computer_guess + 10)  # Ensure highnum doesn't exceed maxnum
        computer_guess = randint(lownum, highnum)
    elif clue == "cold":
        lownum = min(maxnum, lownum + 10)  # Ensure lownum doesn't exceed maxnum
        highnum = max(1, highnum - 10)  # Ensure highnum is at least 1
        computer_guess = randint(lownum, highnum)
