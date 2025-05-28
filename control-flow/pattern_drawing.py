# pattern_drawing.py

# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Loop through each row using a while loop
while row < size:
    # Print each asterisk in the row using a for loop
    for _ in range(size):
        print("*", end="")  # Print without newline
    print()  # Print newline after each row
    row += 1  # Move to the next row
