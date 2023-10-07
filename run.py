''' Needed to obtain random number '''
import random

MAX_GUESS = 3


def get_random_number():
    ''' Generates random number '''
    number = random.randint(1, 10)
    return number