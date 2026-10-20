"""A simple password strength checker using Python's standard library."""

import string


def assess_password(password):
    """Return a strength label, score, and improvement suggestions."""
    checks = {
        "At least 8 characters": len(password) >= 8,
        "At least 12 characters (recommended)": len(password) >= 12,
        "Contains an uppercase letter": any(ch.isupper() for ch in password),
        "Contains a lowercase letter": any(ch.islower() for ch in password),
        "Contains a number": any(ch.isdigit() for ch in password),
        "Contains a special character": any(ch in string.punctuation for ch in password),
    }

    # The 12-character recommendation is informative and is not required
    # for a password to pass the basic five-point strength score.
    core_checks = [
        checks["At least 8 characters"],
        checks["Contains an uppercase letter"],
        checks["Contains a lowercase letter"],
        checks["Contains a number"],
        checks["Contains a special character"],
    ]
    score = sum(core_checks)

    if score == 5 and len(password) >= 12:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    suggestions = []
    if len(password) < 8:
        suggestions.append("Use at least 8 characters; 12 or more is better.")
    elif len(password) < 12:
        suggestions.append("Consider using 12 or more characters.")
    if not checks["Contains an uppercase letter"]:
        suggestions.append("Add an uppercase letter (A-Z).")
    if not checks["Contains a lowercase letter"]:
        suggestions.append("Add a lowercase letter (a-z).")
    if not checks["Contains a number"]:
        suggestions.append("Add a number (0-9).")
    if not checks["Contains a special character"]:
        suggestions.append("Add a special character, such as !, @, #, or ?.")
    if not suggestions:
        suggestions.append("Good mix of character types. Avoid reused or predictable passwords.")

    return strength, score, checks, suggestions


def main():
    print("=" * 46)
    print("         PASSWORD STRENGTH CHECKER")
    print("=" * 46)
    print("Tip: For privacy, try a sample password rather than a password you actually use.")
    password = input("Enter a sample password to check: ")

    strength, score, checks, suggestions = assess_password(password)
    print(f"\nResult: {strength} ({score}/5 core checks passed)")
    print("\nChecklist:")
    for label, passed in checks.items():
        mark = "PASS" if passed else "NOT MET"
        print(f"- {label}: {mark}")

    print("\nSuggestions:")
    for suggestion in suggestions:
        print(f"- {suggestion}")

    print("\nPrivacy note: This program only checks the text locally and does not save it.")


if __name__ == "__main__":
    main()
