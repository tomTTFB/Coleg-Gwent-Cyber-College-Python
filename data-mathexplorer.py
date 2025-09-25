# Welcome to Python Data & Math explorer!

name = input("Enter your name: ")
age = int(input("Enter your age: "))
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