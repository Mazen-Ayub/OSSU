import random

# Get level
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass

# Set a random number
random_no = random.randint(1, level)

# Get guess and check
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < random_no:
                print("Too small!")
            elif guess > random_no:
                print("Too large!")
            else:
                print("Just right!")
                break
    except:
        pass
