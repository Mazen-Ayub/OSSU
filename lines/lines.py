import sys

def main():
    # check the command line arguments
    check_command_line_arg()

    # Try to open the file
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()

    # If can't open this means that the file doesn't exist
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Loop through the lines and check if starts with # or space
    count_lines = 0
    for line in lines:
        if check_line(line) == False:
            count_lines += 1
    print(count_lines)

# Function to check the command line arguments
def check_command_line_arg():
    # Check how many elements in the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Check if it is a python file
    if ".py" not in sys.argv[1]:
        sys.exit("Not a python file")

# Function to check comments and empty lines
def check_line(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False


if __name__ == "__main__":
    main()
