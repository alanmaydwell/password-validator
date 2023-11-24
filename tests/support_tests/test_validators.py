import pytest
from support import validators


def test_has_underscore_gives_true_when_string_is_underscore():
    assert validators.has_underscore("_") is True


def test_has_underscore_gives_false_when_string_is_empty():
    assert validators.has_underscore("") is False


@pytest.mark.parametrize("test_string_with_underscore", ["_", "1_1", "_1", "1_"])
def test_has_underscore_gives_true_when_underscore_present(test_string_with_underscore):
    assert validators.has_underscore(test_string_with_underscore) is True


@pytest.mark.parametrize("test_string_without_underscore", ["", "1", "111", "1111"])
def test_has_underscore_gives_false_when_underscore_absent(test_string_without_underscore):
    assert validators.has_underscore(test_string_without_underscore) is False


@pytest.mark.parametrize("test_string,expected_result", [("", False), ("1", False),
                                                         ("1234567", False),
                                                         ("12345678", True),
                                                         ("123456789", True)])
def test_string_length_validation(test_string, expected_result):
    assert validators.has_required_length(test_string) == expected_result


@pytest.mark.parametrize("test_string_with_capital", ["A", "bA", "bAb", "Ab", "SHOUT!", "Alan"])
def test_has_capital_letter_gives_true_when_capital_present(test_string_with_capital):
    assert validators.has_capital_letter(test_string_with_capital) is True


@pytest.mark.parametrize("test_string_without_capital", ["", "a", "!", "abcde 123"])
def test_has_capital_letter_gives_false_when_capital_absent(test_string_without_capital):
    assert validators.has_capital_letter(test_string_without_capital) is False


@pytest.mark.parametrize("test_string_with_lower_case", ["a", " a ", "Ba", "BaD", "zzz"])
def test_has_lower_case_letter_gives_true_when_lower_case_present(test_string_with_lower_case):
    assert validators.has_lower_case_letter(test_string_with_lower_case) is True


@pytest.mark.parametrize("test_string_without_lower_case", ["", " ", "123", "HELLO!!!", "!£$^&* ) (_+=)"])
def test_has_lower_case_letter_gives_false_when_lower_case_absent(test_string_without_lower_case):
    assert validators.has_lower_case_letter(test_string_without_lower_case) is False


@pytest.mark.parametrize("test_string_with_number", ["1", "a1", " 2", " 2 ", "2783783"])
def test_has_number_gives_true_when_number_present(test_string_with_number):
    assert validators.has_number(test_string_with_number) is True


@pytest.mark.parametrize("test_string_without_number", ["", "a", "A", " A ", "One", "£&*"])
def test_has_number_gives_false_when_number_absent(test_string_without_number):
    assert validators.has_number(test_string_without_number) is False


@pytest.mark.parametrize("test_string", [" ", "a ", " A", " A ", "    "])
def test_has_any_string_method_true_with_pass(test_string):
    assert validators.has_any_string_method_true(test_string, "isspace") is True


@pytest.mark.parametrize("test_string", ["", "a", "A", "abcdefg"])
def test_has_any_string_method_true_with_fail(test_string):
    assert validators.has_any_string_method_true(test_string, "isspace") is False


def test_validate_string_with_validators_upper_and_lower():
    v = validators  # just to reduce line length below
    assert v.validate_string_with_validators("Ab", (v.has_capital_letter, v.has_lower_case_letter)) is True


def test_validate_string_with_validators_underscore_and_number():
    v = validators  # just to reduce line length below
    assert v.validate_string_with_validators("Ab", (v.has_underscore, v.has_number)) is False
