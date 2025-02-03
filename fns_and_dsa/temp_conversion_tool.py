# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """Prompt the user for a temperature and convert accordingly."""
    try:
        # Get user input
        temp_value = float(input("Enter the temperature value: "))
        unit = input("Is this in (C)elsius or (F)ahrenheit? ").strip().lower()

        # Perform conversion based on the unit
        if unit == 'c':
            converted_temp = celsius_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is equal to {converted_temp:.2f}°F")
        elif unit == 'f':
            converted_temp = fahrenheit_to_celsius(temp_value)
            print(f"{temp_value}°F is equal to {converted_temp:.2f}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()


# def main():
#     """Main function to provide a temperature conversion tool."""
#     while True:
#         print("\nTemperature Conversion Tool")
#         print("1. Convert Celsius to Fahrenheit")
#         print("2. Convert Fahrenheit to Celsius")
#         print("3. Exit")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             try:
#                 celsius = float(input("Enter the temperature to convert:: "))
#                 fahrenheit = celsius_to_fahrenheit(celsius)
#                 print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
#             except ValueError:
#                 print("Invalid input! Please enter a valid number.")

#         elif choice == '2':
#             try:
#                 fahrenheit = float(input("Enter temperature in Fahrenheit: "))
#                 celsius = fahrenheit_to_celsius(fahrenheit)
#                 print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
#             except ValueError:
#                 print("Invalid input! Please enter a valid number.")

#         elif choice == '3':
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice! Please select 1, 2, or 3.")

# if __name__ == "__main__":
#     main()