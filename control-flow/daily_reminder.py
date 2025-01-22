



task = str(input ("Enter your task: ")).lower()
priority = str(input ("Priority (high/medium/low): ")).lower()
time_bound = str(input ("Is it time-bound? (yes/no): ")).lower()

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"Your task '{task}' has an undefined priority."
# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    reminder += " Consider completing it when you have free time."
else:
    print ("invalid data for time_bound. it's either 'yes' or 'no'.")
    exit()

# Print the customized reminder
print(f"Reminder: {reminder}")




# Example Interaction and Output:

# Enter your task: Finish project report
# Priority (high/medium/low): high
# Is it time-bound? (yes/no): yes

# Reminder: 'Finish project report' is a high priority task that requires immediate attention today!
# Or, for a non-time-bound task:

# Enter your task: Read a book
# Priority 
# (high/medium/low): low
# Is it time-bound? (yes/no): no

# Note: 'Read a book' is a low priority task. Consider completing it when you have free time.