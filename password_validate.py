from support.validators import (has_underscore,
                                has_required_length,
                                has_capital_letter,
                                has_lower_case_letter,
                                has_number)


def validate_string_with_validators(mystring: str, validators: list[callable] | tuple[callable]) -> bool:
    return False not in [v(mystring) for v in validators]


def validate_password(password):
    validators = [has_underscore, has_required_length, has_capital_letter, has_lower_case_letter, has_number]
    return validate_string_with_validators(password, validators)
