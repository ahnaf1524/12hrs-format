def convert_to_12_hour_format(time24):
    # Split the time string into hours and minutes
    hours, minutes = map(int, time24.split(':'))

    # Determine if it's AM or PM
    period = 'PM' if hours >= 12 else 'AM'

    # Convert hours to 12-hour format
    hours = hours % 12 or 12  # Handle 0 as 12 for midnight

    # Return the formatted time
    return f"{hours}:{minutes:02d} {period}"

# Take input from the user
time24 = input("Enter time in 24-hour format (HH:MM): ")

try:
    # Validate and convert the time
    time12 = convert_to_12_hour_format(time24)
    print(f"The 12-hour format of {time24} is {time12}")
except ValueError:
    print("Invalid time format! Please enter in HH:MM format.")
