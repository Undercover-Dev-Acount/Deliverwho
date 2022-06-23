## Imports
from time import sleep
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


## ===================================Login Screen=====================================================================

connection = func.get_DB()

try:
    login = func.log_in_check(connection)
except:
    print('Unrecognised Username or Password: Exiting app') 
    sleep(3)
    func.clear_term()
    exit()

if login == False:
    print("Unrecognised Username or Password: Exiting app")
    sleep(3)
    func.clear_term()
    exit()
elif login == True:
    func.clear_term()
    
##=====================================Main Menu=====================================================================
    print('Welcome to \033[1m Deliverwho? \033[0m')
    print('Please use the terminal to select an option below:\n')

    exitloop = False
    while exitloop == False:
        
##===============================Main Menu Options===================================================================
        print('\n''\033[1m'
        '1) Inventory Management \n'
        '2) Version Information\n'
        '3) Ordering\n'
        '0) Exit' '\033[0m')

        menu_choice = input()
        func.clear_term()
        
##============================Inventory Management Options===========================================================
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
            
            ## ------------------------Sandwiches ------------------------

            if menu_choice == '1':
                connection = func.get_DB()
                
                #Displays the sandwich data, followed by the list of options to add, edit, delete. 
                func.print_from_DB('Sandwiches')
                
                func.item_options('Sandwiches')
                func.close_DB(connection)
            
            ## ------------------------Snacks-----------------------------
            
            elif menu_choice =='2':
                connection = func.get_DB()
                
                #Displays the snack drink data, followed by the list of options to add, edit, delete. 
                func.print_from_DB('Snacks')
                
                func.item_options('Snacks')
                func.close_DB(connection)
            
            ## -----------------------Soft Drinks--------------------------
            
            elif menu_choice == '3':
                connection = func.get_DB()
                
                #Displays the soft drink data, followed by the list of options to add, edit, delete. 
                func.print_from_DB('Soft_Drinks')
                
                func.item_options('Soft_Drinks')
                func.close_DB(connection)

            ## ---------------------Adult Drinks-------------------------------

            elif menu_choice == '4':
    
                age = int
                age_check = func.age_check(age,18)
                if age_check == True:
                    
                    connection = func.get_DB()
                
                    #Displays the adult drink data, followed by the list of options to add, edit, delete. 
                    func.print_from_DB('Adult_Drinks')
                    
                    func.item_options('Adult_Drinks')
                    func.close_DB(connection)

                
                else:
                    continue
            
            ## --------------------Confec----------------------------------------
            
            elif menu_choice == '5':
                connection = func.get_DB()
                
                #Displays the confec data, followed by the list of options to add, edit, delete. 
                func.print_from_DB('Confec')
                
                func.item_options('Confec')
                func.close_DB(connection)

##==================================EXIT============================================================================   
            elif menu_choice == '0':
                continue
            
        elif menu_choice == '2':
            print('Deliverwho v.1.0.0')
            input('Press enter to return to main menu')
        elif menu_choice == '3':
            
##===============================Ordering Menus============================================================================================
            print('Welcome to the Deliverwho? ordering system.\n')
            
            ord_choice = input('1) Create Order\n2) Edit Order\n3) Delete Order\n4) Return to Main Menu\n')
            
#===============================Create Order Menu =============================================================================
            if ord_choice == '1':           
                connection = func.get_DB()
                try:
                    Order_Data = func.create_order()
                
                    func.save_order(Order_Data, connection)
                    func.commit_DB(connection)
                    func.close_DB(connection)
                except Exception as e:
                    print("I'm sorry, you have encountered an error. Please ensure all values were input correctly and try again")
                    print(e) 
                    func.close_DB(connection)
                    sleep(2)     
                         
##=============================Edit Order Menu=============================================================================================================
            
            if ord_choice == '2':
                
                try:
                    connection = func.get_DB()
                    table_name = "Orders"
                    func.update_order_DB(table_name, connection)
                    func.commit_DB(connection)
                    func.close_DB(connection)
                        

                        
                    
                except Exception as e:
                    print("You have encountered an error, please ensure all values were input correctly and try again")
                    print(e)
                    func.close_DB(connection)
                    sleep(2)
                
                
##=========================Delete Order==========================================================================================================
            if ord_choice == '3':
                connection = func.get_DB()
                table_name = "Orders"
                
                try:
                    func.delete_from_order_DB(table_name, connection)
                    func.commit_DB(connection)
                    func.close_DB(connection)
                except Exception as e:
                    print("You have encountered and error, please try again")
                    print(e)
                    func.close_DB(connection)
                    sleep(2)
                
                    
                        
##=====================Exit======================================================================================================================      
        
        elif menu_choice == '0':
            exitloop = True
            exit()

        


