import re

def check_strength(password):
    score = 0
    feedback = []

    # Checking length of password
    if len(password) > 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Checking Uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Checking Lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Checking Numbers
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Checking Special Characters
    if re.search(r'[\W_]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Checking Uniqueness
    unique_chars = len(set(password))
    if unique_chars >= len(password) / 2:
        score += 1
    else:
        feedback.append("Password should have a higher diversity of characters.")

    # Checking Score of password
    if len(password) >= 8 and score >= 6:
        strength = "Strong"
    elif 5 <= len(password) <= 7 and 3 <= score < 5:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

password = input("Enter your password: ")
strength, feedback = check_strength(password)

print(f"Password Strength: {strength}")
if feedback:
    print("Feedback to improve your password:")
    for suggestion in feedback:
        print(f"- {suggestion}")
