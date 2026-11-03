from logic import (
    word_frequencies
)


# 6. Test dla word_frequencies
def test_word_frequencies():
    text = "To be or not to be"
    expected = {"to": 2, "be": 2, "or": 1, "not": 1}
    assert word_frequencies(text) == expected
    text = "Hello, hello!"
    expected = {"hello": 2}
    assert word_frequencies(text) == expected
    text = ""
    expected = {}
    assert word_frequencies(text) == expected
    text = "Python Python python"
    expected = {"python": 3}
    assert word_frequencies(text) == expected
    text = "Ala ma kota, a kot ma Ale."
    expected = {
        "ala": 2,
        "ma": 2,
        "kota": 1,
        "a": 1,
        "kot": 1
    }
    assert word_frequencies(text) == expected
