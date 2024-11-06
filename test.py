from src import is_polindrome


def test_is_polindrom_1():
    assert is_polindrome('12321') == True

def test_is_polindrom_2():
    assert is_polindrome('12345') == False

def test_is_polindrom_3():
    assert is_polindrome('123321') == True

def test_is_polindrom_4():
    assert is_polindrome('123456') == False