number = [10, 20, 30, 40, 50]

print("First element:", number[0])

number.append(60)
print("After appending 60:", number)

number.remove(30)
print("After removing 30:", number)

for num in number:
    print(num)