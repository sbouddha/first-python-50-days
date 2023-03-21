import os
os.system("cls" if os.name == "nt" else "clear")

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Create objects for all the class
my_menu=Menu()
#my_menu_item=MenuItem()
my_coffee_maker=CoffeeMaker()
my_money_machine=MoneyMachine()

#To implement with OOP, we will use these new objects
is_on=True
while is_on:
    options=my_menu.get_items()
    choice=input(f'What would you like? {options}: ')
    if choice.lower()=='off':
        is_on=False
        print('Machine will be Turned-Off')
    elif choice.lower()=='report':
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        if choice in options:
            drink=my_menu.find_drink(choice)
            if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
                my_coffee_maker.make_coffee(drink)


                    


            


