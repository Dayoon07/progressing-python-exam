import random
import string

def password_generator():
    length = int(input("Enter the password length: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generated password: {password}")

password_generator()