
print("For loop from 1 to 5:")
for i in range(1, 6):
    print(i)

print("\nWhile loop example:")
count = 5
while count > 0:
    print("Count", count)
    count -= 1

print("\nBreak and Continue Example:")
for i in range(10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print("Odd number:", i)
# writting
with open("sample.txt", "w") as f:
    f.write("Hello, this is Day 3!\n")
    f.write("We are learning loops and file handling.\n")

# reading
with open("sample.txt", "r") as f:
    content = f.read()
    print("\nFile Content:")
    print(content)


for i in range(5):
    print("Iteration:", i)

# while loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1
