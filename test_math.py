from math import sqrt

def check_prime_number(x):
    if x < 2:
        return False
    for i in range(2, x, 1):
        if x % i == 0:
            return False
    return True

def check_square_number(x):
    y = int(sqrt(x))
    if y**2 == x:
        return True
    return False

def test_prime_number():
    assert check_prime_number(5) == True

def test_square_number():
    assert check_square_number(9) == True