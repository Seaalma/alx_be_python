from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Print the formatted date and time
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    # Calculate the future date
    future_date = current_date + timedelta(days=days_to_add)
    # Format the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    # Print the future date
    print(f"Future date: {formatted_future_date}")
    return future_date

def main():
    # Part 1: Display the current date and time
    current_date = display_current_datetime()
    
    # Part 2: Calculate a future date
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: ").strip())
        calculate_future_date(current_date, days_to_add)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
