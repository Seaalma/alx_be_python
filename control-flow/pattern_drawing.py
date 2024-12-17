#!/usr/bin/python3

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter for the while loop
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks (*) for each column in the row
    for column in range(size):
        print("*", end="")  # Print asterisk without a newline
    print()  # Print a newline after completing a row
    row += 1  # Increment the row counter
