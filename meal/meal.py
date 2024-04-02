def main():
    # Prompt the user for a time
    time_str = input("Enter the time (in 24-hour format, e.g., 7:30): ")

    # Convert the time to hours as a float
    time = convert(time_str)

    # Determine the meal time and output the result
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")


def convert(time_str):
    # Split the time string into hours and minutes
    hours, minutes = map(int, time_str.split(':'))

    # Convert hours and minutes to a float representing the time in hours
    time_in_hours = hours + minutes / 60.0
    return time_in_hours


if __name__ == "__main__":
    main()
