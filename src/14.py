import random
def generate_random_python_code(lines=5):
    """Generate a random Python code with a specified number of lines."""
    # Initialize an empty list to store the code lines
    code = []
    # Generate the number of lines requested
    for i in range(lines):
        # Add a new line to the code
        code.append("print('Hello, world!')")
    return "\n".join(code)