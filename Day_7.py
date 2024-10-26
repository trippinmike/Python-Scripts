#author: N3m0m3N
#date: 10/5/2024
#description: List Comprehensions (Day 7)

# Let’s say I give you a list saved in a variable
# Write one line of Python that takes this list a and makes a new list that has
# only the even elements of this list in it.

birth_year = [1984, 2002, 2010, 1975, 1999, 2000, 1991]

age = []

for year in birth_year:
    age.append(2024 - year)

for num in age:
    if num < 20:
        print(f"You're {num}.  Sorry, this is too young.")
    else:
        print(f"You're {num}.  You're old enough.")
