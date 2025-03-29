def fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    
    Parameters:
    n (int): The position in the Fibonacci sequence to calculate.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

# Example usage:
print(fibonacci(8))  # Output: 21
