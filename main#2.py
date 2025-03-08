from random import randint
print("give me a number and I'll guess it")
random = input()
computer_guess = randint(1,100)
# print(computer_guess)
clue = input("Is this hot or cold, " + str(computer_guess) + ": ")
if clue == "hot":
    #generate a number between computer_guess, and some higher number or something
    print(randint(computer_guess))
