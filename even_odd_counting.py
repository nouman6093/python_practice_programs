# Write a Python program to count the number of even and odd numbers in a series of numbers
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4

even = 0
odd = 0

for i in range(1,10):
    if(i%2==0):
        even = even + 1
    else:
        odd = odd + 1

print(f"number of even numbers are: {even} and number of odd numbers are {odd}")
