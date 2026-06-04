# Python Random Password Generator

A clean, secure, and beginner-friendly Command Line Interface (CLI) random password generator written in Python. It prompts users for their desired password length, validates the input, and constructs a robust, complex password containing uppercase letters, lowercase letters, numbers, and punctuation.

## Features

- **Robust Input Validation:** Gracefully handles invalid inputs (non-integers, negative numbers, decimals, empty submissions).
- **Security-focused Logic:** If length is `4` or more, it guarantees at least one uppercase letter, one lowercase letter, one numeric digit, and one special character.
- **Repeatable Loop:** Allows generating multiple passwords in a single run without having to restart the script.
- **Modern CLI Design:** Output is neatly framed with emojis and clear status messages.

## Prerequisites

- Python 3.x installed on your machine.
- No external packages required (uses standard library `random` and `string` modules).

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd c:/Users/ATUL/Desktop/decodelabs/password_generator
   ```
3. Run the script:
   ```bash
   python password_generator.py
   ```

---

## Sample Inputs and Outputs

Here is a collection of sample runs demonstrating successful generations and error-handling capabilities.

### 1. Successful Generation (Length: 16)
```text
==================================================
         🔒 SECURE RANDOM PASSWORD GENERATOR 🔒         
==================================================
This tool generates highly secure, randomized passwords.
Includes: Lowercase, Uppercase, Numbers, & Special Symbols.

--------------------------------------------------
Enter the desired password length: 16

==================================================
🎉 SUCCESS! Your generated password is:

👉  q6$G+H2.wA[r_L}*

==================================================
Would you like to generate another password? (y/n): n

Thank you for using the Secure Password Generator. Stay safe online! 👋
```

### 2. Handling Weak Length Warning (Length: 5)
```text
--------------------------------------------------
Enter the desired password length: 5
⚠️  Warning: Passwords shorter than 8 characters are easy to crack!

==================================================
🎉 SUCCESS! Your generated password is:

👉  6z#L_

==================================================
```

### 3. Handling Invalid Integer (Length: 0 or Negative)
```text
--------------------------------------------------
Enter the desired password length: 0
❌ Error: Length must be a positive number greater than 0.

--------------------------------------------------
Enter the desired password length: -10
❌ Error: Length must be a positive number greater than 0.
```

### 4. Handling Non-Integer Characters
```text
--------------------------------------------------
Enter the desired password length: abc
❌ Error: Invalid input. Please enter a valid whole number (integer).

--------------------------------------------------
Enter the desired password length: 12.5
❌ Error: Invalid input. Please enter a valid whole number (integer).

--------------------------------------------------
Enter the desired password length: 
❌ Error: Input cannot be empty. Please enter a number.
```

---

## File Structure

- [password_generator.py](file:///c:/Users/ATUL/Desktop/decodelabs/password_generator/password_generator.py) — Core script containing logical functions, input validation, and CLI formatting.
- [README.md](file:///c:/Users/ATUL/Desktop/decodelabs/password_generator/README.md) — Documentation, usage guides, and samples.
