import random


def raise_exception():
    chance = 0.7
    if random.random() < chance:
        raise ValueError("Invalid value")


try:
    # this code may* raise an exception
    raise_exception()
    print('No exception')
except ValueError:
    print('Value error handled!')
