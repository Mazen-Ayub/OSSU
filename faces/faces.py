def main():
    user_input = input("Please Enter the Data ? ")
    convert(user_input)

def convert(user_input):
    converted_str = user_input.replace(':)', '🙂').replace(':(', '🙁')
    print(converted_str)

main()
