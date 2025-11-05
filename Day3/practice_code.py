print("Practicing loops")

# for loop
num = int(input("Enter Number: "))
print(f"Multiplication of (num): ")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
# while loop
nums = int(input("Enter Number: "))
while nums > 0:
    print(nums)
    nums -= 1
    print("Time up")
for a in range(21):
    if a % 2 != 0:
        print(a)
sum = 0
while True:
    count = int(input("Enter Number: "))
    if count == 0:
        break
    sum += count
print("sum=", sum)

for c in range(22):
    if c % 2 == 0:
        print("Numbers", c)
