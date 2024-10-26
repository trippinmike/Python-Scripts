#author: N3m0m3N
#date: 10/4/2024
#description: Print List (Day 3)

#Take a list and write a program that prints out all the elements of the list that are less than 5.

a_list = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

add_to_list = int(input("Add a number to the list: \n"))
a_list.sort()
a_list.append(add_to_list)
print(a_list)

for i in a_list:
    if i < 10:
        print(i)


