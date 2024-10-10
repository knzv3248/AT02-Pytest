import pytest
from main import count_vowels

def test_count_vowels():
    assert count_vowels("аеёыыыы") == 7

@pytest.mark.parametrize("check_string, expected_count", [
    ("аеёыыыы", 7),
    ("скртч", 0),
    ("hello, world", 3),
    ("мама мыла раму", 6),
    ("Чудо-юдо рыба КИТИК", 8),
    ])
def test_count_vowels_parametrized(check_string, expected_count):
    assert count_vowels(check_string) == expected_count