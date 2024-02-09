import random

def guess_num(correct_num, attempts):

    """Function to guess the secret number."""
    while attempts > 0:
        guess = int(input("Guess how many fingers I'm holding up behind my back (0-10): "))
        if guess == correct_num:
            print("Awesome! You guessed the number {} correct!!".format(correct_num))
            return
        elif guess < correct_num:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
        attempts -= 1

    print("Sorry, the number was {}.".format(correct_num))

def main():
    print("Welcome to the Number Guessing Game!")
    correct_num = random.randint(0, 10)
    attempts = 3
    guess_num(correct_num, attempts)

if __name__ == "__main__":
    main()

