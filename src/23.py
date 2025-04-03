def square_and_sum(numbers):
    """
    This function takes a list of numbers and returns their squares plus the sum of the numbers.
    
    Example usage:
    >>> square_and_sum([1, 2, 3])
    (1+2+3) * 4 = 10
    
    Args:
        numbers (list): A list of numbers.
        
    Returns:
        int: The result of squaring and summing the given list of numbers.
    """
    return sum(map(lambda x: x ** 2, numbers)) + sum(numbers)
