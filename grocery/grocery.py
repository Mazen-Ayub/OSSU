# create empty dic
grocery = {}

while True:
    try:
        # Get user input
        item = input().lower()
        # check if item is already in the dic
        if item in grocery:
            # if it is => add 1 in the count
            grocery[item] += 1
        # otherwise => add the item for the first time
        else:
            grocery[item] = 1
    except EOFError:
        # print all the items in alphabetical order
        for key in sorted(grocery.keys()):
            print(grocery[key], key.upper())
        # stop the while loop
        break
