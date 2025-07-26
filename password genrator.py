import random
import string

def generate_password(length: int, complexity: int):
    """Generate a random password based on specified length and complexity."""
    
    # Define character sets
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    
    # Determine which characters to include based on complexity
    char_set = lower_case
    if complexity >= 2:
        char_set += upper_case
    if complexity >= 3:
        char_set += digits
    if complexity == 4:
        char_set += special_chars
    
    # Generate the password by randomly choosing characters
    password = ''.join(random.choice(char_set) for _ in range(length))
    
    return password

def main():
    try:
        # Prompt user for password length and complexity level
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be a positive integer.")
            return

        print("Password Complexity Levels:")
        print("1: Lowercase letters only")
        print("2: Lowercase + Uppercase letters")
        print("3: Lowercase + Uppercase + Digits")
        print("4: Lowercase + Uppercase + Digits + Special Characters")

        complexity = int(input("Enter the complexity level (1-4): "))

        # Check for valid complexity input
        if complexity not in [1, 2, 3, 4]:
            print("Invalid complexity level. Please enter a number between 1 and 4.")
            return

        # Generate the password
        password = generate_password(length, complexity)
        
        # Display the generated password
        print(f"Generated password: {password}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
