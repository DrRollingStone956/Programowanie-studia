from logic import (
    is_prime
)


# 7. Test dla is_prime
def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(5) is True
    assert is_prime(97) is True
