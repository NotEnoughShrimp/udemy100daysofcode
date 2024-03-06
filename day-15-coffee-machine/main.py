from coffeemachine import MENU, resources


def main():
    coffee_machine = True
    while coffee_machine:
        pick = input("What would you like to drink? (espresso/latte/cappuccino): ")
        if pick in MENU.keys():
            can_we_make_it = check_stock(pick)
            if can_we_make_it:
                make_order(pick)
                cost = MENU[pick]["cost"]
                print(f"Yeah, sure we can make your {pick}. That'll be ${cost:.2f}")
                
            else:
                print(f"We can't make your {pick}")
        elif pick == "report":
            report()
        elif pick == "off":
            coffee_machine = coffee_machine_off()
        else:
            print("invalid entry")

def coffee_machine_off():
    return False

def report():
    print("Here is what we have.")
    print("Water: {}ml".format(resources["water"]))
    print("Milk: {}ml".format(resources["milk"]))
    print("Coffee: {}g".format(resources["coffee"]))
    print("Balance: ${:.2f}".format(resources["cash"]))

def check_stock(drink_name):
    drink_ingredients = MENU[drink_name]["ingredients"]
    for ingredient, quantity in drink_ingredients.items():
        if resources[ingredient] < quantity:
            print(f"Not enough {ingredient}")
            return False
    return True

def make_order(drink_name):
    drink_ingredients = MENU[drink_name]["ingredients"]
    for ingredient, quantity in drink_ingredients.items():
        resources[ingredient] -= quantity
    resources["cash"] += MENU[drink_name]["cost"]
def currency(*args):
    payment = 0
    for arg in args:
        payment += arg
    return payment
    

main()
