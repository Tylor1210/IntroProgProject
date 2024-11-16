users = {}

def signup():
    print("\n--- Signup ---")
    username = input("Choose a username: ")

    # Check if username already exists
    if username in users:
        print("Username already taken. Try a different one.")
    else:
        password = input("Choose a password: ")
        users[username] = password
        print("Signup successful! You can now log in.")

def login():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if username exists and password matches
    if username in users and users[username] == password:
        print(f"Login successful! Welcome, {username}.")
        quiz_menu()
    else:
        print("Login failed. Incorrect username or password.")

def quiz_menu():
    print("\nWelcome to the Programming Quiz!")
    print("Choose a level:")
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Advanced")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        quiz_beginner()
    elif choice == "2":
        quiz_intermediate()
    elif choice == "3":
        quiz_advanced()
    else:
        print("Invalid choice. Returning to main menu.")
# Put quiz_beginner() here


#Put quiz_intermediate() here


#Put quiz_advanced() here


def main():
    while True:
        print("\n--- Welcome ---")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            signup()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()


