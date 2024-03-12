def validate_password(password):
    # Check password length
    if len(password) < 8:
        return False

    # Check for at least one uppercase, one lowercase letter, and one digit
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if not (has_upper and has_lower and has_digit):
        return False

    # Check for spaces in the password
    if ' ' in password:
        return False

    # Password meets all conditions
    return True