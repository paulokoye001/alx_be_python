# multiplication times table
number = int (input ("Enter a number to see its multiplication table: "))

for j in range(1, 11):
    # Inner loop iterates through columns (other factors)
    product = number * j
    print(f"{number} x {j} = {product}", end="\n")  # Print with tabs for better formatting
