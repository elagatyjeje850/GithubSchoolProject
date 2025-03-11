
import random

def get_random_code(length=8):
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    random_code = ''
    for i in range(length):
        random_code += characters[random.randint(0, len(characters) - 1)]
    return random_code