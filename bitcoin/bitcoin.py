import sys
import requests

# Get value from command line
if len(sys.argv) == 2:
    try:
        # change value to float
        value = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

# Get current price of Bitcoin as a float e print with the value of the command line
try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    # json() change the response to dictionary
    response = r.json()
    bitcoin = response['bpi']['USD']['rate_float']
    total = bitcoin * value
    print(f"${total:,.4f}")
    # except that if the link is deleted or edited
except requests.RequestException:
    print("Request Exception")
    sys.exit(1)
