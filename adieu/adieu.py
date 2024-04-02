import inflect
p = inflect.engine()

# create a list to keep names
names = []

# loop forever
while True:
    try:
        # Getting user input
        name = input("Name: ")
        names.append(name)
    except EOFError:
        # Create new line and stop the loop
        print()
        break

# Printing using inflect module
# join => is to put , between the names and (and) before the last name
output = p.join(names)
print(f"Adieu, adieu, to {output}")
