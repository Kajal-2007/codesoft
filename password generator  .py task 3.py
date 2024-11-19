import string
import secrets

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    
    return password

password = generate_password(12) 
print("Generated Password:", password)
