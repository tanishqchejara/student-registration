

import re

def validate_data(name, aicte_id, email, phone, college):
    # Check if all fields are filled
    if not all([name, aicte_id, email, phone, college]):
        return False, "Please fill all fields."

    # Validate email format
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        return False, "Please enter a valid email address."


    return True, None  # Validation succeeded
