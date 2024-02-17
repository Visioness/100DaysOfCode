from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
def main():
    while True:
        choice = input(f"What would you like? ({menu.get_items()}report): ")
        while choice not in menu.get_items() and choice != "report":
            choice = input(f"What would you like? {menu.get_items()}: ")
        
        if choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost): 
                coffee_maker.make_coffee(drink)

if __name__ == "__main__":
    main()