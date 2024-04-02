import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

# check the argv if equal to one
if len(sys.argv) == 1:
    isRandomFont = True
# check the argv if equal to three & argv equal to -f or --font
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandomFont = False
# otherwise exit
else:
    sys.exit("Invalid usage")

# Getting a list of available fonts
figlet.getFonts()

# if isRandomFalse => Setting the font to argv[2]
if isRandomFont == False:
    # try & except to avoid writing wrong fonts
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        sys.exit("Invalid usage")
# otherwise the font is random
else:
    font = random.choice(figlet.getFonts())

# Getting the input from user
msg = input("Input: ")

# render the font and print it
print("Output: ")
print(figlet.renderText(msg))
