# Question 1
print("Hello World")

# Question 2
import math
pi = math.pi
print(pi)

# Question 3
def square_root(num):
    if num > 0:
        return math.sqrt(num)
    else:
        print("Error: Cannot compute the square root of a negative number.")

# Question 4
def add_numbers(a, b):
    return a + b

# Question 5
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start(self):
        print(f"{self.year} {self.make} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
print(car1)
