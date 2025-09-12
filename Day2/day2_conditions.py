
fruits = ["apple", "banana", "cherry"]   
coordinates = (10, 20)                  
person = {"name": "Ahmed", "age": 23}   
unique_numbers = {1, 2, 3, 3, 2, 1} 

print("List:", fruits)
print("Tuple:", coordinates)
print("Dictionary:", person)
print("Set:", unique_numbers)

age = 23
if age >= 18:
    print("You are an adult ✅")
else:
    print("You are a minor ❌")

def greet(name):
    return f"Hello, {name}! 👋"

print(greet("Ahmed"))

def add_numbers(a, b):
    return a + b

print("Sum:", add_numbers(5, 7))

import math
import random

print("Square root of 16:", math.sqrt(16))
print("Random number (1–10):", random.randint(1, 10))
def even_or_odd(num: int) -> str:
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(10))  
print(even_or_odd(12))  

