# Basic input and output

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello " + name + ", you are " + age + " years old")

# Lists
# -------------------------

fruit = ["Apple", "Banana", "Cherry"]

print(f"The first fruit is: {fruit[0]}")

fruit.append("Orange")
print(f"Updated fruit list: {fruit}")

for fruit in fruit:
    print(f"I like {fruit}")