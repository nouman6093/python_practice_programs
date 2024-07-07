# Write a Python program that accepts a word from the user and reverses it.

word = input("enter a word: ").title()
reverse = ""

for i in word[::-1]:
    reverse += i

print(reverse)
