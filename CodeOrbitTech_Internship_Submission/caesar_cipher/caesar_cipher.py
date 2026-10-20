"""Caesar cipher demonstration: encrypt or decrypt text with a shift key."""


def transform_text(text, shift):
    """Shift English letters while preserving case and non-letter characters."""
    result = []
    shift %= 26

    for char in text:
        if "A" <= char <= "Z":
            result.append(chr((ord(char) - ord("A") + shift) % 26 + ord("A")))
        elif "a" <= char <= "z":
            result.append(chr((ord(char) - ord("a") + shift) % 26 + ord("a")))
        else:
            result.append(char)

    return "".join(result)


def read_shift():
    while True:
        raw = input("Enter the shift value (integer): ").strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter a whole number, such as 3 or -2.")


def main():
    print("=" * 46)
    print("        CAESAR CIPHER ENCRYPTION TOOL")
    print("=" * 46)
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Choose 1 or 2: ").strip()

    if choice not in {"1", "2"}:
        print("Invalid choice. Please run the program again and choose 1 or 2.")
        return

    message = input("Enter the text: ")
    shift = read_shift()
    effective_shift = shift if choice == "1" else -shift
    output = transform_text(message, effective_shift)

    print("\nOriginal text :", message)
    print("Shift key     :", shift)
    print("Result        :", output)
    print("\nReminder: Caesar cipher is for learning only, not for securing sensitive data.")


if __name__ == "__main__":
    main()
