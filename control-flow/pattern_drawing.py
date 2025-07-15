# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Outer while loop for rows
while row < size:
    # Inner for loop for columns (printing asterisks)
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
