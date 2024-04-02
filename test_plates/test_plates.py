from plates import is_valid

def main():
    # call test functions
    test_min_max()
    test_start_letters()
    test_middle_no()
    test_no_0()
    test_panctuation()

# Plates may contain a maximum of 6 charcters (letters & numbers) and a minimum of 2 characters
def test_min_max():
    assert is_valid('AA') == True
    assert is_valid('ABCDEF') == True
    assert is_valid('A') == False
    assert is_valid('ABCDEFGH') == False

# Plates must start with at least two letters
def test_start_letters():
    assert is_valid('AA') == True
    assert is_valid('A2') == False
    assert is_valid('2A') == False
    assert is_valid('22') == False

# Numbers cannot be used in the middle of a plate; the must come at the end
def test_middle_no():
    assert is_valid('AAA222') == True
    assert is_valid('AAA22A') == False

# The first number used cannot be a '0'
def test_no_0():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False

# No periods, spaces, or panctuation marks are allowed
def test_panctuation():
    assert is_valid('PI3.14') == False
    assert is_valid('PI3!14') == False
    assert is_valid('PI 14') == False



if __name__ == "__main__":
    main()
