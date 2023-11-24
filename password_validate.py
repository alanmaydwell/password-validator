from support.validators import validate_string_with_validators
from support.validators import (has_underscore,
                                has_required_length,
                                has_capital_letter,
                                has_lower_case_letter,
                                has_number)


def validate_password(password: str) -> bool:
    validators = [has_underscore, has_required_length, has_capital_letter, has_lower_case_letter, has_number]
    return validate_string_with_validators(password, validators)
