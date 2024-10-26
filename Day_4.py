#author: N3m0m3N
#date: 10/5/2024
#description: Divisors (Day 4)

# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)

