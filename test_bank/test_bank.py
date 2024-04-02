from bank import value

def main():
    # Call test functions
    test_zero()
    test_twenty()
    test_hunderd()

# Test return 0
def test_zero():
    assert value('hello gi') == 0
    assert value('Hello') == 0
    assert value('HeLlo Gi') == 0

# Test return 20
def test_twenty():
    assert value('Hi') == 20
    assert value('hey') == 20

# Test return 100
def test_hunderd():
    assert value("What's up?") == 100
    assert value('good morning') == 100


if __name__ == "__main__":
    main()
