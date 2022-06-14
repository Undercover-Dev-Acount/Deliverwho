## Imports
import My_Functions.functions as func
from getpass import getpass
from passwords import User_passwords 
import json
import random 
from dotenv import load_dotenv
import os
import pymysql
from prettytable import from_db_cursor

## DB Declaration
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

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
                connection = func.get_DB()
                
                #Displays the sandwich data, followed by the list of options to add, edit, delete. 
                func.print_from_DB('Sandwiches')
                
                func.item_options('Sandwiches')
                func.close_DB()
            elif menu_choice =='2':
                connection = func.get_DB()
                
                #Displays the soft drink data, followed by the list of options to add, edit, delete. 
                func.print_from_DB('Snacks')
                
                func.item_options('Snacks')
                func.close_DB()
            elif menu_choice == '3':
                connection = func.get_DB()
                
                #Displays the soft drink data, followed by the list of options to add, edit, delete. 
                func.print_from_DB('Soft_Drinks')
                
                func.item_options('Soft_Drinks')
                func.close_DB(connection)

                
            elif menu_choice == '4':
    
                age = int
                age_check = func.age_check(age,18)
                if age_check == True:
                    
                    connection = func.get_DB()
                
                    #Displays the soft drink data, followed by the list of options to add, edit, delete. 
                    func.print_from_DB('Adult_Drinks')
                    
                    func.item_options('Adult_Drinks')
                    func.close_DB(connection)

                
                else:
                    continue
            elif menu_choice == '5':
                connection = func.get_DB()
                
                #Displays the soft drink data, followed by the list of options to add, edit, delete. 
                func.print_from_DB('Confec')
                
                func.item_options('Confec')
                func.close_DB(connection)

                
            elif menu_choice == '0':
                continue
            
        elif menu_choice == '2':
            print('Deliverwho v.0.9.9')
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
       
        


