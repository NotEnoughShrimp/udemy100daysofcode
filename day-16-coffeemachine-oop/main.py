from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_machine_on = True

while is_machine_on:
    user_input = input(f'What would you like? ({menu.get_items()}): ').lower()
    if user_input == 'off':
        print('Coffee Machine is off.')
        is_machine_on = False
    elif user_input == 'report':
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(user_input):
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
