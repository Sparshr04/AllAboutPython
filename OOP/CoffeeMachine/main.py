from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import PrettyTable

menu_list = Menu()
# items = MenuItem()
item_report = CoffeeMaker()
profit = MoneyMachine()
table = PrettyTable()

print("Welcome to the Coffee Machine!\n\n")
print(f"Please select from the menu {menu_list.get_items()}\n\n")


is_true= True
while(is_true):

    user_choice = input("Your Choice: ")

    drink = menu_list.find_drink(user_choice)



    if drink is not None:
        print(f"{drink.name} is available\n")
        print(f"Using {drink.ingredients} from the storage.\n")
        if item_report.is_resource_sufficient(drink)==True:
            print(f"Please Pay ${drink.cost}.")
            if profit.make_payment(drink.cost)==True:
                item_report.make_coffee(drink)
                table.add_column("Profit", [str(print(profit.report()))])
                table.add_column("Resource",[str(print(item_report.report()))])
                print(table)


    is_true = bool(input("Want to buy more? [True/False]"))