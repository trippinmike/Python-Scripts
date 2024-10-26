#author: N3m0m3N
#date: 10/5/2024
#description: String List (Day 6)

# Ask the user for a string and print out whether this string is a palindrome or not.

forward_word = input("Please enter a word:\n")
forward_word = str(forward_word)

reverse_word = forward_word[::-1]

print(reverse_word)

if forward_word == reverse_word:
    print(f"{forward_word} is a palindrome.")
else:
    print(f"{forward_word} is not a palindrome.")