



task = str(input ("Enter your task: ")).lower()
priority = str(input ("Priority (high/medium/low): ")).lower()
time_bound = str(input ("Is it time-bound? (yes/no): ")).lower()

match priority:
    case "high":
        reminder = f"Your task '{task}' is of high priority."
    case "medium":
        reminder = f"Your task '{task}' is of medium priority."
    case "low":
        reminder = f"Your task '{task}' is of low priority."
    case _:
        reminder = f"Your task '{task}' has an undefined priority."
# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " It requires immediate attention today!"

# Print the customized reminder
print("\nReminder:")
print(reminder)