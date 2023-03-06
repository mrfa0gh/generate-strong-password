import string, random, pyfiglet
print('')
logo = pyfiglet.figlet_format("My user Mrfa0gh")
print(logo)
count = 0
while True:
    # Prompt the user to enter the desired password length
    print('')
    length = int(input("Enter the desired password length: "))
    print('')
    # Define the character set to use in generating the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a strong password of the desired length
    password = ''.join(random.choice(characters) for i in range(length))
    # Print the generated password
    print("Your strong password is:", password)
    print('')
    # Prompt the user to save password in txt file
    choice = input("Press 'y' to save password or 'Q' to Quit: ")
    if choice.lower() == 'y':
        count += 1
        with open("password.txt", "a") as f:
            f.write(f"[!]New Password Number => {count}: {password}\n")
            print("Password saved to password.txt")
    elif choice.lower() == 'q':
        break
    else:
        print("Invalid choice. Please try again.")
        continue
    # Prompt the user to try again or exit
    print('')
    choice = input("Press 'T' to try again or 'Q' to exit: ")
    if choice.lower() == 't':
        continue
    elif choice.lower() == 'q':
        break
    else:
        print("Invalid choice. Please try again.")
        continue
