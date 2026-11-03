from logic import (
    is_palindrome
)


# 1. Test dla is_palindrome
def test_is_palindrome():
    assert is_palindrome("KajaK") is True
    assert is_palindrome("Kobyła ma mały bok") is True
    assert is_palindrome("python") is False
    assert is_palindrome("") is True
    assert is_palindrome("A") is True
