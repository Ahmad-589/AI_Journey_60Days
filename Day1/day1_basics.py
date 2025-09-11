# day1_basics.py

name = input("Enter your name: ")
age = int(input("Enter your age: "))

birth_year = 2025 - age
print(f"Hello {name}, you were born around {birth_year}!")

# First NumPy test
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("Sample NumPy Array:", arr)
