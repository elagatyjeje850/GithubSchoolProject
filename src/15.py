import random

def get_random_python_code():
    # Generate a random number between 1 and 5
    num = random.randint(1, 5)

    # Return a string based on the number generated
    if num == 1:
        return "print('Hello World!')"
    elif num == 2:
        return "x = 5\ny = 10\nprint(x + y)"
    elif num == 3:
        return "fruits = ['apple', 'banana', 'cherry']\nprint(fruits[1])"
    elif num == 4:
        return "for i in range(6):\n\tprint(i)"
    else:
        return "while True:\n\tprint('Hello World!')"