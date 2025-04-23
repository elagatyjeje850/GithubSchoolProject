import random
import time

def create_random_code():
    while True:
        code = f"#!/bin/bash\n"
        random_code = "random_text"
        if random.random() < 0.5: 
            code += "\n# Debugging: Add some comments to make it easier to understand."
            random_code += " # Random text added for debugging purposes.\n"
        
        code += f"echo -e '{code}' >> .env\n"
        time.sleep(random.uniform(1, 2))
        if not (random.random() > 0.9):
            break
    with open(".env", "a") as file:
        file.write(f"{random_code}\n")

create_random_code()
