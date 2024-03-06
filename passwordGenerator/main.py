import string
import random

print('''Select type password : 
1. Digits
2. Letters
3. Special characters
''')

option = int(input("Select option: "))

if option == 1:
    password_length = int(input("Enter the length of the password: "))

    password = ''.join(random.choice(string.digits) for _ in range(password_length))
    print("Generated Password:", password)

elif option == 2:
    password_length = int(input("Enter the length of the password: "))

    password = ''.join(random.choice(string.ascii_letters) for _ in range(password_length))
    print("Generated Password:", password)

elif option == 3:
    password_length = int(input("Enter the length of the password: "))

    password = ''.join(random.choice(string.digits + string.digits + string.punctuation) for _ in range(password_length))
    print("Generated Password:", password)

else:
    print("Operation invalid")