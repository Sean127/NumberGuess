''' Needed to obtain random number '''
import random
import sys

MAX_GUESS = 3


def get_random_number():
    ''' Generates random number '''
    number = random.randint(1, 10)
    return number


def game():
    number = get_random_number()
    print("Welcome to the game")
    print("The game is simple. Pick a number between 1 and 10")
    print("You will have 3 attempts")
    no_of_guesses = 0
    correct = False
    while no_of_guesses < 3:
        print(number)
        try:
            input_guess = input("Enter your guess:")
            guess = int(input_guess)
            no_of_guesses += 1
            if guess == number:
                print("Congrats you guessed correctly")
                correct = True
                no_of_guesses = 3
            elif guess < 1 or guess > 10:
                print("Please enter a number between 1-10")
            elif guess < number:
                print('Your guess is too low.')
            elif guess > number:
                print('Your guess is too high.')
        except ValueError:
            print("Not a valid number")
            no_of_guesses += 1

    if no_of_guesses == 3:
        if correct is False:
            print("Sorry, your out of attempts. The correct answer was", number)

    again = input("Would you like to play again?[Y/N]").lower()
    if again == 'y':
        game()
    elif again == 'n':
        print("Thanks for playing!")
        sys.exit()


def main():
    game()


main()