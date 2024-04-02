def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Removes the leading '$' and converts the string to a float
    return float(d.lstrip('$'))


def percent_to_float(p):
    # Removes the trailing '%' and converts the string to a float
    return float(p.rstrip('%')) / 100


main()
