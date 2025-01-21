#   Utilize while loops and nested for loops to draw a simple text-based pattern.

number = int(input("Enter the size of the pattern: "))

if number <= 0:
    print ("you entred an invalid number")
else:
    
    row = 0    # Initialize row counter

    while row < number:
        # Use a for loop to print asterisks (*) for the current row
        for _ in range(number):
            print("*", end="")  # Print asterisk without moving to the next line
        print()  # Print a newline character after completing the row
        row += 1
    
    