import pytest
from gradebook import letter_grade, is_passing


# letter_grade testing

def test_letter_grade_A():
    assert letter_grade(95) == "A"

def test_letter_grade_F():
    assert letter_grade(45) == "F"

@pytest.mark.parametrize("score, expected", [
    (95, "A"),
    (45, "F")
])

def test_letter_grade(score, expected):
    assert letter_grade(score) == expected

def test_letter_grade_invalid_type():
    with pytest.raises(TypeError):
        letter_grade("hello")

# is_passing testing

def test_is_passing_true():
    assert is_passing(75) == True