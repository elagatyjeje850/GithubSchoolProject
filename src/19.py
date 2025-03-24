import math

def calculate_factorial(n):
    """
    Calculate the factorial of a given number n.
    
    Args:
        n (int): A positive integer.
        
    Returns:
        int: The factorial of n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        result = n * calculate_factorial(n - 1)
        return result

# Example usage
number = 5
factorial = calculate_factorial(number)
print(f"The factorial of {number} is {factorial}")
