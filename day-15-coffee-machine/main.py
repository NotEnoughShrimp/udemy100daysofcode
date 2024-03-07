from coffeemachine import MENU, resources


def main():
    is_machine_on = True
    while is_machine_on:
        user_input = input("What would you like to drink? (espresso/latte/cappuccino): ")
        if user_input in MENU.keys():
            if resource_sufficient(user_input):
                payment = process_coins()
                confirmation = check_transaction_success(payment, user_input)
                if confirmation:
                    if isinstance(confirmation, bool):  # should be here where I can update and take from resources.
                        print(f"Enjoy your {user_input}.")
                    elif isinstance(confirmation, float):
                        print(f"Enjoy your {user_input}. Here is ${confirmation:.2f} in change")
                else:
                    print(f"Not enough. Refunded ${confirmation:.2f}")    
        elif user_input == "off":
            print("Machine is off")
            is_machine_on = False
        elif user_input == "report":
            report()
        else:
            print("invalid entry")


def report():
    _earning = float(resources['earning'])
    formatted_earning = "{:.2f}".format(_earning)
    print("Current inventory: ")
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"earning: ${formatted_earning}")


def resource_sufficient(drink):
    drink_ingredients = MENU[drink]["ingredients"]  
    # drink_ingredients = MENU['espresso'][ingredients=water:50, coffee:18]
    for ingredient, quantity in drink_ingredients.items():
        # for every key, value in the ingredient's dictionary
        if resources[ingredient]<quantity:
            print(f"Sorry there is not enough {ingredient}")
            return False
        else:
            resources[ingredient] -= quantity
    resources["earning"] += float(MENU[drink]["cost"])
    # if value of key in resources is less than quantity of espresso's 
    return True


def process_coins():
    coin_directory = {
        "quarter": 0.25,
        "dime": 0.10,
        "nickle": 0.05,
        "penny": 0.01
    }
    total = 0
    for k, v in coin_directory.items():
        coin_add = int(input(f"How many {k}s: "))
        total += coin_add * v
    return total


def check_transaction_success(total, drink):
    drink_cost = MENU[drink]["cost"]
    if total < drink_cost:
        return False  # f"Not enough, refunded: ${total:.2f}"
    elif total == drink_cost:
        return True  # f"Enjoy your {drink}"
    elif total > drink_cost:
        new_total = total - drink_cost
        return new_total

main()

