def validate_string_with_validators(mystring: str, validators: list[callable] | tuple[callable]) -> bool:
    return False not in [v(mystring) for v in validators]


def has_underscore(mystring: str) -> bool:
    return "_" in mystring


def has_required_length(mystring: str, minimum: int = 9) -> bool:
    return len(mystring) >= minimum


def has_capital_letter(mystring: str) -> bool:
    return [c for c in mystring if c.isupper()] != []


def has_lower_case_letter(mystring: str) -> bool:
    return [c for c in mystring if c.islower()] != []


def has_number(mystring: str) -> bool:
    return [c for c in mystring if c.isnumeric()] != []


def has_any_string_method_true(mystring: str, str_method: str) -> bool:
    return [c for c in mystring if getattr(c, str_method)()] != []
