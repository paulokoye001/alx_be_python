# multiplication times table

number = int(input("Enter a number to see its multiplication table: "))

# Loop to generate the multiplication table
for j in range(1, 11):  # Multiplication factors from 1 to 10
    product = number * j
    print(f"{number} x {j} = {product}")