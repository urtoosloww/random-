from random import randint
from random import random as r
maxnum = 100
print("give me a number, 1-" + str(maxnum) + "and I'll guess it")
ans = input()
ans = int(ans)
computer_guess = randint(1,maxnum)
lownum = 0
highnum = maxnum
# print(computer_guess)
while 1:
    clue = input("Is this hot or cold " + str(computer_guess) + ": ")
    if computer_guess == ans:
        print("you got it!!!")
        break
    if clue == "hot":
        lownum = computer_guess - 10
        highnum = computer_guess + 10
        #generate a number between computer_guess, and some higher number or something
        computer_guess = randint(lownum, highnum)
    elif clue == "cold":
        lownum += 10
        highnum -= 10
        computer_guess = (randint(lownum, highnum))
        print(computer_guess)


