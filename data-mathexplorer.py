# Welcome to Python Data & Math explorer!

name = input("Enter your name: ")

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input for age. Please enter a number.")
    age = int(input("Enter your age: "))

try:
    height = float(input("Enter your height in meters: "))
except ValueError:
    print("Invalid input for height. Please enter a decimal number.")
    height = float(input("Enter your height in meters: "))

# Math operations
print("\n--- Math Operations ---")
a = input("Enter first number (a): ")
b = input("Enter second number (b): ")

aFloat= float(a)
bFloat= float(b)

aInt = int(aFloat)
bInt = int(bFloat)

print(f"Addition: a + b = {aFloat + bFloat}")
print(f"Subtraction: a - b = {aFloat - bFloat}")
print(f"Multiplication: a * b = {aFloat * bFloat}")
print(f"Division: a / b = {aFloat / bFloat}")
print(f"Floor Division: a // b = {aFloat // bFloat}")
print(f"Modulus: a % b = {aFloat % bFloat}")
print(f"Exponent: a ** b = {aFloat ** bFloat}")

# List
print("\n--- List Example ---")
hobbies = input("Enter your hobbies separated by commas: ").split(',')
hobbies = [hobby.strip() for hobby in hobbies]
print("Your hobbies are: ", hobbies)

# Tuples
print("\n--- Tuple Example ---")
location = ("Ebbw Vale", "Wales", "UK")
print("Your Location Tuple: ", location)

# Set
print("\n--- Set Example ---")
unique_letters = set(name.lower())
print("Unique letters in your name: ", unique_letters)

# Dictionary
print("\n--- Dictionary Example ---")
profile = {
    "Name": name,
    "Age": age,
    "Height": height,
    "Hobbies": hobbies,
    "Location": location
}
print(f"Your Profile Dictionary: {profile}")#
for key, value in profile.items():
    print(f"{key}: {value}")

# Summary
print("\n--- Summary ---")
print("Thank you for exploring Python today, ", name, "!")
