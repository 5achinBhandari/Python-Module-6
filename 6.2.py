import random
def roll_dice(num_sides):
    return random.randint(1, num_sides)



max_sides = int(input("Enter the maximum number of sides on the dice: "))


while True:

    result = roll_dice(max_sides)


    print(f"Roll Result: {result}")


    if result == max_sides:
        break
