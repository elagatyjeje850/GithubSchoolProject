def calculate_area(rectangle):
    """
    Calculate the area of a rectangle.
    
    Args:
        rectangle: A tuple containing the length and width of the rectangle.

    Returns:
        The area of the rectangle as an integer.
    """
    return rectangle[0] * rectangle[1]

# Example usage:
rectangle = (5, 3)
print(f"The area of the rectangle with length {rectangle[0]} and width {rectangle[1]} is: {calculate_area(rectangle)}")
