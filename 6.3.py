# Define the function to convert gallons to liters
def gallons_to_liters(gallons):
    liters = gallons * 3.78541  # 1 gallon = 3.78541 liters
    return liters



while True:

    gallons = float(input("Enter a volume in gallons (or a negative value to quit): "))


    if gallons <= 0:
        break


    liters = gallons_to_liters(gallons)


    print(f"{gallons} gallons is equal to {liters:.2f} liters")
