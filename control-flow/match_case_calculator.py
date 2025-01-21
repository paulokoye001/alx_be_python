print("Two numbers will be needed for this arithmetic calculation.")
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

operation = input(
    "+ = Addition\n- = Subtraction\n* = Multiplication\n/ = Division\n"
    "Enter the arithmetic operation you want to carry out: "
).lower()

match operation:
    case "+":
        addition = float(num_1 + num_2)
        print(f"The result is {addition}")
    case "-":
        subtraction = float(num_1 - num_2)
        print(f"The result is {subtraction}")
    case "*":
        multiplication = float(num_1 * num_2)
        print(f"The result is {multiplication}")
    case "/":
        if num_2 != 0:
            division = float(num_1 / num_2)
            print(f"The result is {division}")
        else:
            print("Error! Division by zero is not allowed.")
    case _:
        print("Invalid operation selected.")