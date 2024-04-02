from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    birth_date = input("Date of Birth: ")
    try:
        year, month, day = check_birthday(birth_date)
    except:
        sys.exit("Invalid Date")

    dato_of_birth = date(int(year), int(month), int(day))
    dato_of_today = date.today()
    difference = dato_of_today -dato_of_birth
    total_min = difference.days * 24 *60
    output = p.number_to_words(total_min, andword="")
    print(output.capitalize() + " minutes")



def check_birthday(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        year, month, day = birth_date.split("-")
        return year, month, day

if __name__ == "__main__":
    main()
