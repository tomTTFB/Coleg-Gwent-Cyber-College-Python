name = input("Enter your name: ")
try:
    amount = int(input("Enter amount of smoothies: "))
except ValueError:
    print("Please enter a valid whole number number.")
    exit()

if amount < 1:
    print("Please enter a number greater than 0.")
    try:
        amount = int(input("Enter amount of smoothies: "))
    except ValueError:
        print("Please enter a valid whole number number.")
        exit()

cost = amount * 3.50

print(name + ", your total is £" + str(cost) + " for " + str(amount) + " smoothies.")