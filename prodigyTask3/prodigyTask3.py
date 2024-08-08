import re

def evaluate_password_strength(pwd):
    # Define criteria for password strength
    min_length = len(pwd) >= 8
    has_uppercase = bool(re.search(r'[A-Z]', pwd))
    has_lowercase = bool(re.search(r'[a-z]', pwd))
    has_digit = bool(re.search(r'\d', pwd))
    has_special_char = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', pwd))

    # Assess the strength of the password based on criteria
    if min_length and has_uppercase and has_lowercase and has_digit and has_special_char:
        return "Strong password! 👍"
    else:
        feedback = "Weak password. Consider the following improvements:\n"
        if not min_length:
            feedback += "- Ensure the password is at least 8 characters long\n"
        if not has_uppercase:
            feedback += "- Include at least one uppercase letter\n"
        if not has_lowercase:
            feedback += "- Include at least one lowercase letter\n"
        if not has_digit:
            feedback += "- Include at least one digit\n"
        if not has_special_char:
            feedback += "- Include at least one special character (!@#$%^&*(),.?\":{}|<>)\n"

        return feedback

def main():
    print("Password Strength Checker")

    # Get user input for the password
    user_password = input("Enter your password: ")

    # Check and provide feedback on the password complexity
    result = evaluate_password_strength(user_password)
    print(result)

if __name__ == "__main__":
    main()