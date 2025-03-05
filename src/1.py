import random

def get_random_code():
    """Returns a randomly generated code"""
    # Generate a random string of length 12 using the ascii_letters and digits string constants
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))