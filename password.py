import random
import string

def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Get user input for password length
while True:
    try:
        length = int(input("Enter the desired length of the password: "))
        break
    except ValueError:
        print("Please enter a valid integer.")

# Generate and display the password
password = generate_password(length)
print("Generated password:", password)
