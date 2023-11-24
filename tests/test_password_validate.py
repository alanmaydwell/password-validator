import pytest
from password_validate import validate_password


@pytest.mark.parametrize("password", ["Ab1_zzzzy", "1Aa_12345", "A_1b     "])
def test_password_validate_gives_true_when_password_good(password):
    assert validate_password(password) is True


@pytest.mark.parametrize("password", ["", " ", "password", "P_", "LETMEIN123_", "correcthorsebatterystaple"])
def test_password_validate_gives_false_when_password_bad(password):
    assert validate_password(password) is False
