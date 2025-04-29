from auth import authenticate, register

def main():
    print("=== Welcome to AI Mental Health Counseling System ===")
    choice = input("Do you want to (1) Login or (2) Register? ")

    if choice == '1':
        username = input("Username: ")
        password = input("Password: ")
        if authenticate(username, password):
            print("✅ Login successful! Access granted.")
            # Proceed to chatbot, etc.
        else:
            print("❌ Invalid username or password.")

    elif choice == '2':
        username = input("Choose a username: ")
        password = input("Choose a password: ")
        if register(username, password):
            print("✅ Registered successfully. You can now login.")
        else:
            print("⚠️ Username already taken.")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
