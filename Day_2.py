#author: N3m0m3N
#date: 10/4/2024
#description: Odd or Even (Day 2)

# Ask the user for a number.
num_1 = int(input("Enter a number: \n"))

check = int(input("Enter a second number: \n"))

print(f"Does {num_1} divide evenly into {check}?")

# Depending on whether the number is even or odd, print out an appropriate message to the user.

result = num_1 / check

if result % 2 == 0:
    print(f"{num_1} divides into {check}.")
else:
    print(f"{num_1} does nto divides into {check}.")

