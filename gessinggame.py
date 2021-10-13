import random
word = random.randint(1,9)
chances=0
while chances<5:
    userword=int(input("Enter your number between 1 to 9"))
    if word == userword:
        print ("thats the word")
        break
    elif word<userword:
        print ("too high")
    else:
        print ("too low")
    chances=chances+1
