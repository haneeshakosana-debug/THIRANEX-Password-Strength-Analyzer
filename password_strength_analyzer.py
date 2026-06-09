import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add special characters.")

    # Strength Rating
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, suggestions


password = input("Enter Password: ")

strength, suggestions = check_password_strength(password)

print("\nPassword Strength :", strength)

if suggestions:
    print("\nSuggestions to Improve Password:")
    for s in suggestions:
        print("-", s)

if strength != "Strong":
    print("\nSuggested Strong Password:")
    print(password + "@123Aa")
