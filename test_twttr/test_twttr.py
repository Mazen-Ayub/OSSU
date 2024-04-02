from twttr import shorten

def main():
    # call test function
    test_upper_lower()
    test_numbers()
    test_punctuation()

# Test letters upper and lower cases
def test_upper_lower():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('TwItTeR') == 'TwtTR'

# Test numbers
def test_numbers():
    assert shorten('1234') == '1234'

# Test punctuation
def test_punctuation():
    assert shorten('!?.,') == '!?.,'


if __name__ == "__main__":
    main()
