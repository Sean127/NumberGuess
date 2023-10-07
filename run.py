''' Needed to obtain random number '''
import random

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
    while no_of_guesses < 3:
        print(number)
        guess = int(input("Enter your guess:"))
        no_of_guesses += 1
        if guess == number:
            print("Congrats you guessed correctly")
        elif guess < number:
            print('Your guess is too low.')
        elif guess > number:
            print('Your guess is too high.')
        else:
            print("Sorry, your out of attempts. The correct answer was", number)


def main():
    game()


main()