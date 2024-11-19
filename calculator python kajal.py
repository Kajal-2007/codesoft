import random
import string

def generate_password(length=12):
    if length < 6:
        print("Password length should be at least 6 characters.")
        return None

    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    
    all_characters = lowercase + uppercase + digits + special_characters

    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters),
    ]
    
    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)
    
    
    return ''.join(password)

def main():
    print("Password Generator")
    
    
    try:
        length = int(input("Enter the length of the password (minimum 6): "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    
    password = generate_password(length)
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
