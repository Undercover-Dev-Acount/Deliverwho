## Imports
import My_Functions.functions as func
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
    'order number' : 0
}

## Login Screen
name = input('Username:\n')
password = getpass('Password:\n')

## Compares name key and password value to external dictionary to grant access
if User_passwords[name]==password: 
    func.clear_term()

    ## Main Menu
    print('Welcome to \033[1m Deliverwho? \033[0m')
    print('Please use the terminal to select an option below:\n')

    exitloop = False
    while exitloop == False:
        
        ## Importing Inventory files, converting to lists. 
    #     sanwiches_dict = {}
    #     sandwiches = 'Data/sandwiches.json'

    #     with open(sandwiches) as file:

    #         sandwiches_dict = json.load(file)
        
    # #------------------------------------------------------------------#

    #     snacks_dict = {}
    #     snacks = 'Data/snacks.json'

    #     with open(snacks) as file:

    #         snacks_dict = json.load(file)

    # #------------------------------------------------------------------#

    #     confec_dict = {}
    #     confec = 'Data/confec.json'

    #     with open(confec) as file:

    #         confec_dict = json.load(file)
        
    # #------------------------------------------------------------------#

    #     soft_drinks_dict = {}
    #     soft_drinks = 'Data/soft-drinks.json'

    #     with open(soft_drinks) as file:

    #         soft_drinks_dict = json.load(file)

    # #------------------------------------------------------------------#

    #     adult_drinks_dict = {}
    #     adult_drinks = 'Data/adult-drinks.json'

    #     with open(adult_drinks) as file:

    #         adult_drinks_dict = json.load(file)

    #------------------------------------------------------------------#        

        print('\n''\033[1m'
        '1) Inventory Management \n'
        '2) Version Information\n'
        '3) Ordering\n'
        '0) Exit' '\033[0m')

        menu_choice = input()
        func.clear_term()
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
            func.clear_term()
            if menu_choice == '1':
                print(*sandwiches, sep = ',')
                
                func.item_options(sandwiches)
            
            elif menu_choice =='2':
                print(*snacks, sep = ',')

                func.item_options(snacks)
            elif menu_choice == '3':
                print(*soft_drinks, sep = ',')

                func.item_options(soft_drinks)
            elif menu_choice == '4':
    
                age = int
                age_check = func.age_check(age,18)
                if age_check == True:
                    
                    print(*adult_drinks, sep = ',')

                    func.item_options(adult_drinks)
                else:
                    continue
            elif menu_choice == '5':
                print(*confec, sep = ',')

                func.item_options(confec)
            elif menu_choice == '0':
                continue
            
        elif menu_choice == '2':
            print('Deliverwho v.0.0.1')
            input('Press enter to return to main menu')
        elif menu_choice == '3':
            order_list = {}
            list_name = 'Data/orders.json'

            with open(list_name) as file:

                order_list = json.load(file)
            
            courier_list = 'Data/couriers.json'

            with open(courier_list) as file:
                courier_list3 = []
                courier_list = json.load(file)
                courier_list2 = courier_list['Couriers']
               
            for key in courier_list2.keys():
                courier_list3.append(key)
            
            rcourier = random.choice(courier_list3)
            
            print('Welcome to the Deliverwho? ordering system.\n')
            
            ord_choice = input('1) Create Order\n2) Edit Order\n3) Delete Order\n')

            if ord_choice == '1':           
                for key in Order.keys():
                    
                    if key == 'order status'or key == 'courier':
                        Order['order status'] = 'Placed' 
                        Order['courier'] = rcourier
                        Order['order number'] = random.randint(1, 1000)
                        break
                    Order[key] = input(f'please enter user {key}\n')
                order_list['orders'].append(Order)
                
                
                orders_ext = 'Data/orders.json'
                with open(orders_ext) as file:
                    data = json.load(file)
                

                export = 'Data/orders.json'
                with open(export,'w') as file:
                    new = json.dumps(order_list, indent='   ')
                    file.write(new)
            if ord_choice == '2':
                
                order_list = {}
                list_name = 'Data/orders.json'

                with open(list_name) as file:

                    order_list = json.load(file)
                for key in order_list['orders']:
                    index = order_list['orders'].index(key)
                    print(index, sep= ',')
                edit_choice = int(input('Choose an order number to edit'))
                if edit_choice < len(order_list['orders']):
                    for key2 in order_list['orders'][index]:
                    
                        if key2 == 'order status'or key2 == 'courier'or key2 == 'order number':
                            continue
                                
                        order_list['orders'][index][key2] = input(f'please enter user {key2}\n')
                export = 'Data/orders.json'
                with open(export,'w') as file:
                    new = json.dumps(order_list, indent='   ')
                    file.write(new)


            if ord_choice == '3':

                order_list = {}
                list_name = 'Data/orders.json'

                with open(list_name) as file:

                    order_list = json.load(file)
                for key in order_list['orders']:
                    index = order_list['orders'].index(key)
                    print(index, sep= ',')
                try:
                    del_choice = int(input('Choose an order index to delete or press enter to return to main menu'))
                except:
                    continue
                if del_choice < len(order_list['orders']):
                    order_list['orders'].pop(del_choice)
                
                export = 'Data/orders.json'
                with open(export,'w') as file:
                    new = json.dumps(order_list, indent='   ')
                    file.write(new)

                       
                        
        
        
        elif menu_choice == '0':
            exitloop = True
            exit()
       
        


