# Program to check if the entered character is an alphabet or not

# Taking input from the user
char = input("Enter a character: ")

# Checking if the input is a single character
if len(char) == 1:
    # Using comparison operators to check if it's an alphabet
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        print(f"The character '{char}' is an alphabet.")
    else:
        print(f"The character '{char}' is NOT an alphabet.")
else:
    print("Please enter only a single character.")
