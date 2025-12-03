import re
 
# Data structures to store users and books
library_users = []
library_books = []
 
# Start loop to add a new user
while True:
    print("\n--- Add New Library User ---")
 
    # Presence Check: Name
    user_name = input("Enter user's full name: ").strip()
    if user_name == "":
        print("Name is required.")
        continue
 
    # Length Check: Address
    user_address = input("Enter user's address: ").strip()
    if len(user_address) < 10 or len(user_address) > 100:
        print("Address must be between 10 and 100 characters.")
        continue
 
    # Type Check: Age
    user_age_input = input("Enter age: ")
    try:
        user_age = int(user_age_input)
    except ValueError:
        print("Age must be a number.")
        continue
 
    # Range Check: Age must be between 5 and 120
    if user_age < 5 or user_age > 120:
        print("Age must be between 5 and 120.")
        continue
 
    # Format Check: Postcode
    user_postcode = input("Enter user's UK postcode: ").upper()
    postcode_pattern = r"^[A-Z]{1,2}[0-9][0-9A-Z]? ?[0-9][A-Z]{2}$"
    if not re.match(postcode_pattern, user_postcode):
        print("Invalid UK postcode format.")
        continue
 
    # Check Digit: Library Card Number (10-digit)
    card_number = input("Enter 10-digit library card number: ")
    if len(card_number) == 10 and card_number.isdigit():
        total = sum(int(card_number[i]) * (10 - i) for i in range(10))
        if total % 11 != 0:
            print("Invalid card number (check digit failed).")
            continue
    else:
        print("Card number must be 10 digits.")
        continue

 
    # Store user data
    user_record = {
        "name": user_name,
        "address": user_address,
        "age": user_age,
        "postcode": user_postcode,
        "card_number": card_number,
    }
    library_users.append(user_record)
    print("User added successfully!")
 
    # Ask if another user should be added
    another = input("Add another user? (yes/no): ").lower()
    if another != "yes":
        break
 
# Display all users
print("\n--- All Library Users ---")
for user in library_users:
    print(user)