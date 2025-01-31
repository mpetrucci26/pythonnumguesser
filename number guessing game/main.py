import random
num = random.randint(1, 100)
guesses = 0
maxGuesses = 6
while guesses < maxGuesses:
    guess = input("Guess: ")
    if guess.isdecimal():
        if int(guess) >= 1 and int(guess) <= 100:
            guesses += 1
            if num == int(guess):
                print("You won in " + str(guesses) + " guesses!")
                break
            elif num < int(guess):
                print("The number is below " + guess  + " (" + str(int(maxGuesses)-int(guesses)) + " guesses left)")
            elif num > int(guess):
                print("The number is above " + guess  + " (" + str(int(maxGuesses)-int(guesses)) + " guesses left)")
        else:
            print("Please enter a whole number from 1-100")
    else:
        print("Please enter a whole number from 1-100")

if not int(guess) == num:
    print("You ran out of guesses! The number was " + str(num))
