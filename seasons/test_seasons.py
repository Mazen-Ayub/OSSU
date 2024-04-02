from seasons import check_birthday

def main():
    test_check_birthday()

def test_check_birthday():
    assert check_birthday('2001-07-26') == ("2001", "07", "26")
    assert check_birthday('2001-7-6') == None
    assert check_birthday('July 26, 2001') == None

if __name__ == "__main__":
    main()
