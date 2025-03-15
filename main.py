from random import randint
name1= input("Name a cool animal ")
name2= input("name another cool animal ")
name3 = randint(1,999)
points = 0
maxnum = 100
random = randint(1,maxnum)
guesses = randint(1,15)
initialGuesses = guesses
print("hello " + name1 + name2 + str(name3))
print("points: " + str(points))
print("guess a # 1-" + str(maxnum))
print("guesses: " + str(guesses))

while guesses > 0:
    answer = input()

    while not answer.isnumeric():
        print("this isn't a number")
        print("Try a real number")
        answer =input()
        guesses -= 1
    answer = int(answer)

    if answer == random:
        if guesses == initialGuesses:
            points += 3
        print("\x1b[32mYou got it!\x1b[0m")
        points = points + 1
        print("points: " + str(points))
        random = randint(1,10)
        
        guesses = 5
    else:
        guesses -= 1
        print("\x1b[31mtry again!\x1b[0m")
        diff = abs(random - answer)
        if diff < 25:
            print("\x1b[38;2;100;56;9mhot!!🔥\x1b[0m")
        else:
            print("\x1b[36mcold\x1b[0m")
        
    
    print("guesses: " + str(guesses))
print(random)
