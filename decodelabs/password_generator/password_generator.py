"""
Secure Random Password Generator
--------------------------------
A beginner-friendly Python script that generates a secure, random password.
Features:
- Validates user input (numbers, bounds, types)
- Structured using functions
- Beautiful and professional console styling
- Ensures at least one character from each set (upper, lower, digit, special) if length >= 4
"""

import random
import string


def generate_password(length: int) -> str:
    """
    Generates a secure random password of the specified length.
    
    If length is 4 or more, the function guarantees at least one character from:
    - Lowercase letters
    - Uppercase letters
    - Digits
    - Special characters/punctuation
    """
    # Define the character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Combine all character sets to form a single pool
    all_characters = lower + upper + digits + special

    # If the length is less than 4, we cannot guarantee one of each set.
    # We simply select random characters from the entire pool.
    if length < 4:
        return ''.join(random.choice(all_characters) for _ in range(length))

    # To ensure the password is secure, we pre-populate it with at least
    # one character from each category.
    password_chars = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random characters from the combined pool
    remaining_length = length - 4
    password_chars.extend(random.choice(all_characters) for _ in range(remaining_length))

    # Shuffle the list of characters to randomize the positions of the guaranteed characters
    random.shuffle(password_chars)

    # Join the character list to create the final password string
    return ''.join(password_chars)


def get_valid_length() -> int:
    """
    Prompts the user for a password length and validates the input.
    Continues to prompt until a valid positive integer is entered.
    """
    while True:
        try:
            print("\n" + "-" * 50)
            user_input = input("Enter the desired password length: ").strip()
            
            # Handle empty inputs
            if not user_input:
                print("[ERROR] Input cannot be empty. Please enter a number.")
                continue

            # Convert input to integer
            length = int(user_input)

            # Check if length is greater than 0
            if length <= 0:
                print("[ERROR] Length must be a positive number greater than 0.")
                continue
            
            # Optional warning for weak password length
            if length < 8:
                print("[WARNING] Passwords shorter than 8 characters are easy to crack!")
            
            # Prevent potential memory issues or console flooding for extremely large values
            if length > 2048:
                print("[WARNING] Length is extremely large. For performance, maximum allowed length is 2048.")
                length = 2048

            return length

        except ValueError:
            print("[ERROR] Invalid input. Please enter a valid whole number (integer).")


def main():
    """
    Main function to run the Password Generator CLI application.
    """
    # Print a professional header banner
    print("=" * 50)
    print("         *** SECURE RANDOM PASSWORD GENERATOR ***       ")
    print("=" * 50)
    print("This tool generates highly secure, randomized passwords.")
    print("Includes: Lowercase, Uppercase, Numbers, & Special Symbols.")
    
    # Run the generator in a loop so the user can generate multiple passwords
    while True:
        # Step 1: Get validated length
        length = get_valid_length()
        
        # Step 2: Generate the password
        password = generate_password(length)
        
        # Step 3: Display results nicely
        print("\n" + "=" * 50)
        print("[SUCCESS] Your generated password is:")
        print(f"\n-->  {password}\n")
        print("=" * 50)
        
        # Ask if the user wants to generate another one
        choice = input("Would you like to generate another password? (y/n): ").strip().lower()
        if choice not in ('y', 'yes'):
            print("\nThank you for using the Secure Password Generator. Stay safe online!")
            break


if __name__ == "__main__":
    main()
