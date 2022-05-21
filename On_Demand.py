## Functions
import printfunc
from getpass import getpass
from passwords import User_passwords 
import json
import random 
## Product names
soft_drinks = ["Lemonade", " Coke", " Orange Juice", " Water", 'Dr Pepper', 'Fanta', 'Lucozade']
adult_drinks = ["Vodka Lemonade", " Rum and Coke", " Pint", " House Red", " House White"]
sandwiches = ['BLT', ' Egg and Cress', ' Chicken and Stuffing', ' Tuna Sweetcorn', ' Ham and Cheese', ' Smoked Salmon and Cream Cheese']
snacks = ['Cheese and Onion Crisps', 'Ready Salted Crisps', 'Prawn Cocktail Crisps', 'McCoys Steak Crisps', 'Sour Cream Pringles']
confec = ['KitKat 4', 'KitKat Chunky', 'Snickers', 'Mars Bar', 'Lion Bar', 'Kinder Bueno', 'Twix', 'Chocolate Chip Cookie', 'Sugared Ring Donut']

## Order Dictionary

Order = {
    'customer name' : 'customer name',
    'address' : 'address',
    'phone number' : 'phone number',
    'order status' : 'Pending',
    'courier' : 'none',
}

## Login Screen
name = input('Username:\n')
password = getpass('Password:\n')

if User_passwords[name]==password:
    printfunc.clear_term()

    ## Main Menu
    print('Welcome to \033[1m Deliverwho? \033[0m')
    print('Please use the terminal to select an option below:\n')

    exitloop = False
    while exitloop == False:
        print('\n''\033[1m'
        '1) Inventory Management \n'
        '2) Version Information\n'
        '3) Ordering\n'
        '0) Exit' '\033[0m')

        menu_choice = input()
        printfunc.clear_term()
        if menu_choice == '1':
            print('Please use the terminal to browse the menus:\n'
            '\n''\033[1m'
            '1) Sandwiches \n'
            '2) Snacks\n'
            '3) Soft Drinks\n'
            '4) Alcohol\n'
            '5) Confectionary\n'
            '0) Exit' '\033[0m')
            
            menu_choice =input('Please enter your desired number below \n')
            printfunc.clear_term()
            if menu_choice == '1':
                print(*sandwiches, sep = ',')
                
                printfunc.item_options(sandwiches)
            
            elif menu_choice =='2':
                print(*snacks, sep = ',')

                printfunc.item_options(snacks)
            elif menu_choice == '3':
                print(*soft_drinks, sep = ',')

                printfunc.item_options(soft_drinks)
            elif menu_choice == '4':
                
                age = int(input(f'How old are you?\n'))
                printfunc.clear_term()
                if age < 18:
                    continue
                
                print(*adult_drinks, sep = ',')

                printfunc.item_options(adult_drinks)
            elif menu_choice == '5':
                print(*confec, sep = ',')

                printfunc.item_options(confec)
            elif menu_choice == '0':
                continue
            
        elif menu_choice == '2':
            print('Deliverwho v.0.0.1')
            input('Press enter to return to main menu')
        elif menu_choice == '3':
            order_list = {}
            list_name = 'orders.json'

            with open(list_name) as file:

                order_list = json.load(file)
            
            courier_list = 'couriers.json'

            with open(courier_list) as file:

                courier_list = json.load(file)
                courier_list2 = courier_list['Couriers']
            for key in courier_list2.keys():
                courier_list = [key]




            rcourier = random.choice(courier_list)
            
            print('Welcome to the Deliverwho? ordering system.\n')
            
            for key in Order.keys():
                
                if key == 'order status'or key == 'courier':
                    Order['order status'] = 'Placed' 
                    Order['courier'] = rcourier
                    break
                Order[key] = input(f'please enter user {key}\n')
            order_list['orders'].append(Order)
            print('Order placed!')
            
            orders_ext = 'orders.json'
            with open(orders_ext) as file:
                data = json.load(file)
            

            export = 'orders.json'
            with open(export,'w') as file:
                new = json.dumps(order_list, indent='   ')
                file.write(new)
        

        elif menu_choice == '0':
            exitloop = True
            exit()
       
        


