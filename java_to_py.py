def calculate_room_cost():
    height = float(input("Enter wall height in meters: "))
    length = float(input("Enter wall length in meters: "))

    area = 2 * height * length + 2 * height * length

    print("Choose paint type:\n1. Standard (£1.00 per sq m)\n2. Premium (£1.50 per sq m)\n3. Luxury (£2.00 per sq m)")
    paintchoice = float(input("Enter choice (1/2/3): "))

    paintcostpersqm = 0
    if paintchoice == 1:
        paintcostpersqm = 1.00
    elif paintchoice == 2:
        paintcostpersqm = 1.50
    elif paintchoice == 3:
        paintcostpersqm = 2.00
    else:
        print("Invalid paint choice. defaulting to Standard.")
        paintcostpersqm = 1.00

    undercoat = input("Is undercoat required? (yes/no): ").lower()
    undercoatCost = 0.0
    if undercoat == "yes":
        undercoatCost = 0.50 * area

    paintCost = paintcostpersqm * area
    totalBeforeVat = paintCost + undercoatCost
    vat = totalBeforeVat * 0.20
    totalCost = totalBeforeVat + vat

    print(
        f"Room size: {area:.2f} sq m\n"
        f"Paint cost: £{paintCost:.2f}\n"
        f"Undercoat cost: £{undercoatCost:.2f}\n"
        f"Total before VAT: £{totalBeforeVat:.2f}\n"
        f"Total after VAT: £{totalCost:.2f}"
    )
    return totalBeforeVat

numRooms = int(input("How many rooms to paint: "))
totalBeforeVat = 0.0
for roomNum in range(1, numRooms + 1):
    print(f"\n--- Room {roomNum} ---")
    beforeVat = calculate_room_cost()
    totalBeforeVat += beforeVat

grandVat = totalBeforeVat * 0.20
grandTotal = totalBeforeVat + grandVat
print("\nTotal for all rooms:")
print(f"Total before VAT: £{totalBeforeVat:.2f}")
print(f"Total after VAT: £{grandTotal:.2f}")
