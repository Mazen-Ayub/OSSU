def main():
    # Get user input
    greeting == input("Greeting: ")
    # Store the result of value function
    printed_value = value(greeting)
    print(f'${printed_value}')

def value(greeting):
    # convert greeting in all lower and without whitespaces
    greeting = greeting.lower().strip()
    # check if the answer has 'hello' => return 0
    if 'hello' in greeting:
        return 0
    # check if answer starts with 'h' => return 20
    elif 'h' in greeting[0]:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
