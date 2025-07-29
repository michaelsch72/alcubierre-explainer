def format_output(text):
    """Format the output text for better readability."""
    return f"*** {text} ***"

def validate_input(user_input, valid_options):
    """Validate user input against a list of valid options."""
    return user_input in valid_options