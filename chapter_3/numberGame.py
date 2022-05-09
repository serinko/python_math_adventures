from random import randrange

def numberGame():
    # Choose a random number
    # between 1 and 100
    number = randrange(1,100)

    print("\nI am thinking about a number between 1 and 100, try to guess.")
    guess = int(input("\nWhat is your guess?\t"))

    while guess:
        if guess == number:
            print(f"Yes! That is correct. The number was {number}.")
            break
        elif number > guess:
            print("Nope, higher!")
        else:
            print("Nope, lower!")

        guess = int(input("\nWhat is your guess?\t"))

numberGame()
