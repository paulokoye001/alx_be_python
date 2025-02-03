import datetime

# def display_current_datetime():
#     current_date = datetime.datetime.now()
#     print(f"Current Date and Time: {current_date}")

# def format_date():
#     now = datetime.datetime.now()

#     print(f"ISO Format: {now.isoformat()}")  


# display_current_datetime()


def display_current_datetime():
    """Display the current date and time in a readable format."""
    current_date = datetime.datetime.now()  # Get the current date and time
    formatted_date = current_date.isoformat()          # ("%Y-%m-%d %H:%M:%S")  # Format as YYYY-MM-DD HH:MM:SS
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date():
    """Calculate and display a future date based on user input."""
    try:
        days_to_add = int(input("Enter the number of days to add: "))  # Get user input
        current_date = datetime.date.today()  # Get today's date
        future_date = current_date + datetime.timedelta(days=days_to_add)  # Add days
        print(f"Future Date (after {days_to_add} days): {future_date}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()

    




