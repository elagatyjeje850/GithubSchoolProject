import math
from typing import List

def calculate_factorials(numbers: List[int]) -> int:
    result = 1
    for number in numbers:
        result *= (number + 1)
    return result
