#author: N3m0m3N
#date: 10/5/2024
#description: List Overlap (Day 5)

# Take two lists and write a program that returns a list that contains only the elements that are common between
# the lists (without duplicates).
# Make sure your program works on two lists of different sizes
# Randomly generate lists

import random

rand_list_1 = []
rand_list_2 = []
n = 5

for i in range(n):
    rand_list_1.append(random.randint(0, 5))
    rand_list_2.append(random.randint(3, 7))

print(rand_list_1)
print(rand_list_2)


set_1 = set(rand_list_1)
set_2 = set(rand_list_2)

matches = list(set_1.intersection(set_2))
print(matches)
