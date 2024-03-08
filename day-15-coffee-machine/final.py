from coffeemachine import MENU, resources


revenue = 0


def main():
    is_machine_on = True
    while is_machine_on:
        customer_order = input("What would you like to drink? (espresso/latte/cappuccino): ").lower()
        if customer_order == "off":
            is_machine_on = False
        elif customer_order == "report":
            report()
        elif customer_order in MENU.keys():
            if can_we_make_it(customer_order):
                payment = process_payment()
                if is_transaction_successful(payment, MENU[customer_order]["cost"]):
                    make_coffee(customer_order, MENU[customer_order]["ingredients"])
        else:
            print("invalid entry.")


def report():
    """Generates a report of resources dict formatted."""
    format_revenue = "{:.2f}".format(revenue)
    print("Current inventory")
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['water']}g")
    print(f"profit: ${format_revenue}")


def can_we_make_it(menu_ingredients):
    """checks menu_ingredients to resources dict to determine whether drink can be made."""
    drink_ingredients = MENU[menu_ingredients]["ingredients"]
    for ingredient, quantity in drink_ingredients.items():
        if resources[ingredient] < quantity:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


def process_payment():
    """prompts user to select how many coins they want with a dict for values and adding them to the total."""
    coins = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    total = 0
    for c, v in coins.items():
        entered_coins = int(input(f"how many {c}: "))
        total += (entered_coins * v)
    return total


def is_transaction_successful(payment, drink_cost):
    """takes the payment & drink_cost and compares. If equal it returns True. If more than equal it returns the
    excess of their payment as well as True. Otherwise, it will return False and perform print("Refunded")."""
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        format_change = "{:.2f}".format(change)
        print(f"Your change is: ${format_change}.")
        global revenue
        revenue += drink_cost
        return True
    else:
        print("Refunded")
        return False


def make_coffee(drink_name, order_requirements):
    """takes the order's name and ingredient and subtracts from the resources."""
    for ingredient in order_requirements:
        resources[ingredient] -= order_requirements[ingredient]
    print(f"Enjoy your {drink_name}. Enjoy.")


main()
