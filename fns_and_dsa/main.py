

from arithmetic_operations import perform_operation

def main():
    
    print("Arithmetic Operations")
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()




# from arithmetic_operations import perform_operation

# # Example usage
# num1 = 10.5
# num2 = 2.5
# operation = 'multiply'  # You can also use 'add', 'subtract', or 'divide'

# result = perform_operation(num1, num2, operation)
# print(f"Result: {result}")