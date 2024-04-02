def main():
    text = input("Input: ")
    print(shorten(text))

def shorten(text):
    output= ''
    for char in text:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            output += char
    return output

if __name__ == "__main__":
    main()
