def main():
    # Prompting the user for input
    answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")

    # Checking if the input is 42, forty-two, or forty two (case-insensitive)
    if answer.strip().lower() == "42" or answer.strip().lower() == "forty-two" or answer.strip().lower() == "forty two":
        print("Yes")
    else:
        print("No")

main()
