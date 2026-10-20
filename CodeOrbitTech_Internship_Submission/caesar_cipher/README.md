# Caesar Cipher Encryption Tool

A Python command-line tool that encrypts and decrypts text using a user-selected integer shift.

## Run
```bash
python caesar_cipher.py
```

## How it works
Each English letter is shifted through the alphabet by the chosen number of positions. Decryption shifts letters in the opposite direction. Uppercase/lowercase is preserved, and spaces, digits, and punctuation remain unchanged.

## Example
- Mode: Encrypt
- Text: `Hello, World!`
- Shift: `3`
- Result: `Khoor, Zruog!`

## Security note
The Caesar cipher is easy to break and must not be used to protect real passwords or confidential information.
