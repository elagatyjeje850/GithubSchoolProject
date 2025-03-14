import random

def get_random_integer(low, high):
    return random.randint(low, high)

def get_random_string(length):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(alphabet) for i in range(length))

def get_random_boolean():
    return random.choice([True, False])
