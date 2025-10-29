import coffee_maker
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



coffe_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_om=True

while is_om:
    options =menu.get_items()
    choice=input(f"Which coffee would you like? {options}")
    if choice == "off":
        is_om=False
    elif choice == "water":
        coffe_maker.report()
    else:
        drink= menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink) and  money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)
