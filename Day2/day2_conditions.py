# Day2/practice_problems.py

# 1. Write a program to check if a number is even or odd.
import random
num = 7
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# 2. Function to find the maximum of three numbers


def max_of_three(a, b, c):
    return max(a, b, c)


print("Max of (5, 10, 3):", max_of_three(5, 10, 3))

# 3. Store student data in a dictionary and print name & grade
student = {"name": "Ahmed", "age": 23, "grade": "A"}
print(f"Student {student['name']} has grade {student['grade']}")

# 4. Use a set to remove duplicates from a list
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = set(nums)
print("Unique numbers:", unique_nums)

# 5. Use random to generate 5 random numbers between 1 and 50
print("Random numbers:", [random.randint(1, 50) for _ in range(5)])
