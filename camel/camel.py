def main():
    variable_name = input("camalCase: ")
    snake_case = camel_to_snake(variable_name)
    print(f"snake_case: {snake_case}")

def camel_to_snake(variable_name):
    snake_case = ""
    for i in variable_name:
        if i.isupper():
            snake_case = snake_case + "_" + i.lower()
        else:
            snake_case = snake_case + i
    return snake_case.lstrip('_')

if __name__ == "__main__":
    main()
