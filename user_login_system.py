print("===== USER LOGIN SYSTEM =====")

# Create account
username = input("Enter username: ")
password = input("Enter password: ")

length = len(password)

lower = 0
upper = 0
digit = 0

# Check password characters
for ch in password:

    if ch >= 'a' and ch <= 'z':
        lower = 1

    if ch >= 'A' and ch <= 'Z':
        upper = 1

    if ch >= '0' and ch <= '9':
        digit = 1

# Validate password
if (length >= 6 and length <= 12
        and lower == 1
        and upper == 1
        and digit == 1):

    print("Valid password")
    print("Account created successfully!")

    # Login
    print("\n===== LOGIN =====")

    login_username = input("Enter username: ")
    login_password = input("Enter password: ")

    if login_username == username and login_password == password:
        print("Login successful!")
    else:
        print("Invalid username or password")

else:
    print("Invalid password")
    print("Password must contain:")
    print("- 6 to 12 characters")
    print("- At least one lowercase letter")
    print("- At least one uppercase letter")
    print("- At least one digit")