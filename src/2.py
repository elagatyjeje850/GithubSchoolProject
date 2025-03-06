import random
def generate_random_code(n):
    """Generate a random code of length n."""
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(n))