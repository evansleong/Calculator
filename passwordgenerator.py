import random
import string


def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def password_generator():
    num_passwords = int(input("Enter the number of passwords you want to generate: "))
    password_length = int(input("Enter the length of each password: "))

    passwords = [generate_random_password(password_length) for _ in range(num_passwords)]

    print("\nGenerated Passwords:")
    for index, password in enumerate(passwords, start=1):
        print(f"Password {index}: {password}")


if __name__ == "__main__":
    print("Welcome to the Random Password Generator!")
    password_generator()
