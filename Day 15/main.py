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

on = True


# TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”

# TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.

# TODO: 3. Print report.
def print_report():
    for resource in resources:
        if resource == "coffee":
            print((f"{resource.title()}: {resources[resource]}g"))
        else:
            print(f"{resource.title()}: {resources[resource]}ml")


# print_report()


# TODO: 4. Check resources sufficient?
# def res_sufficient(coffee):
#     water_needed = MENU[coffee]["ingredients"]["water"]
#     coffee_needed = MENU[coffee]["ingredients"]["coffee"]
#     if coffee == "espresso":
#         milk_needed = 0
#     else:
#         milk_needed = MENU[coffee]["ingredients"]["milk"]
#
#     water_avail = resources["water"]
#     milk_avail = resources["milk"]
#     coffee_avail = resources["coffee"]
#
#     if water_avail >= water_needed and milk_avail >= milk_needed and coffee_avail > coffee_needed:
#         resources["water"] -= water_needed
#         resources["milk"] -= milk_needed
#         resources["coffee"] -= coffee_needed
#         return True
#     else:
#         return False

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO: 5. Process coins.

def coin_total(quarter, dime, nickle, penny):
    """ calculates the total amount """
    return quarter * 0.25 + dime * 0.1 + nickle * 0.05 + penny * 0.01

def make_coffee(coffee, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {coffee} ☕️. Enjoy!")

# TODO: 6. Check transaction successful?
def trans_successful(coffee, total):
    cost = MENU[coffee]["cost"]

    if total >= cost:
        if total > cost:
            change = total - cost
            print(f"Here is ${change:2,.2f} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO: 7. Make a coffee.
while on:
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        print("Powering down...")
        on = False
    elif choice == "report":
        print_report()
    else:
        if is_resource_sufficient(MENU[choice]["ingredients"]):
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total = coin_total(quarters, dimes, nickles, pennies)
            print(f"Money: ${total:2,.2f}")
            trans_successful(choice, total)
            make_coffee(choice, MENU[choice]["ingredients"])
