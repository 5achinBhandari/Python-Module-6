import math
def calculate_unit_price(diameter_cm, price_eur):

    radius_m = diameter_cm / 100  # Convert centimeters to meters


    area_sqm = math.pi * (radius_m**2)


    unit_price_per_sqm = price_eur / area_sqm

    return unit_price_per_sqm

# Main program
if __name__ == "__main__":

    diameter1 = float(input("Enter the diameter of the first pizza (in cm): "))
    price1 = float(input("Enter the price of the first pizza (in euros): "))


    diameter2 = float(input("Enter the diameter of the second pizza (in cm): "))
    price2 = float(input("Enter the price of the second pizza (in euros): "))


    unit_price1 = calculate_unit_price(diameter1, price1)
    unit_price2 = calculate_unit_price(diameter2, price2)


    if unit_price1 < unit_price2:
        print("The first pizza provides better value for money.")
    elif unit_price2 < unit_price1:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas have the same unit price.")

