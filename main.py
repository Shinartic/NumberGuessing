import random

def Game():
    r_num = int(random.randint(0, 100))
    print("I have a number between 0 and 100, when you guess it you win.")
    print(r_num)
    guess = input("What number do you think that I am thinking of? \n ")
    guess = int(guess)
    if guess ==  r_num:
        print("Good job that was first try!")
    if guess > r_num:
        print("Sorry not yet, try guessing a little lower")
    else:
        print("Sorry not yet, try guessing a little higher")

Game()
