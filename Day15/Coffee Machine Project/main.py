MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

resources["money"] = 0

########################################################################################
# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
#   a. Check the user’s input to decide what to do next.
#   b. The prompt should show every time action has completed.

active = True
while active:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 3. Print report.
    if coffee_type == "report":
        print("Water:", resources["water"], "ml")
        print("Milk:", resources["milk"], "ml")
        print("Coffee:", resources["coffee"], "g")
        print("Money:$", resources["money"])
        continue

    # TODO: 2. Turn off the Coffee Machine by entering “off”.
    if coffee_type == "off":
        active = False
        continue

    # Drink selection
    if coffee_type.startswith("esp"):
        drink = "espresso"
    elif coffee_type.startswith("la"):
        drink = "latte"
    elif coffee_type.startswith("cap"):
        drink = "cappuccino"
    else:
        print("Invalid choice.")
        continue

    # Extract ingredients and cost
    waterqty = MENU[drink]["ingredients"].get("water", 0)
    milkqty = MENU[drink]["ingredients"].get("milk", 0)
    cofeeqty = MENU[drink]["ingredients"].get("coffee", 0)
    cost = MENU[drink]["cost"]

    # print("Drink:", drink)
    # print("Water:", waterqty)
    # print("Milk:", milkqty)
    # print("Coffee:", cofeeqty)
    # print("Cost:", cost)

    ########################################################################################
    # TODO: 4. Check resources sufficient?
    #   a. If not enough ingredients → stop.

    if resources["water"] < waterqty:
        print("Sorry, not enough water.")
        continue

    if resources["milk"] < milkqty:
        print("Sorry, not enough milk.")
        continue

    if resources["coffee"] < cofeeqty:
        print("Sorry, not enough coffee.")
        continue

    ########################################################################################
    # TODO: 5. Process coins.
    #   a. Prompt user to insert coins.
    #   b. Calculate total monetary value.

    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    total_inserted = quarters + dimes + nickels + pennies
    print("You inserted: $", round(total_inserted, 2))

    ########################################################################################
    # TODO: 6. Check transaction successful?
    #   a. If not enough money → refund.
    #   b. If enough → accept and give change.

    if total_inserted < cost:
        print("Sorry, that's not enough money. Money refunded.")
        continue

    change = round(total_inserted - cost, 2)
    if change > 0:
        print("Here is your change: $", change)



    ########################################################################################
    # TODO: 7. Make Coffee.
    #   a. Deduct ingredients.
    #   b. Add money.
    #   c. Serve drink.

    resources["water"] -= waterqty
    resources["milk"] -= milkqty
    resources["coffee"] -= cofeeqty

    resources["money"] += cost

    print(f"Here is your {drink}. Enjoy!")