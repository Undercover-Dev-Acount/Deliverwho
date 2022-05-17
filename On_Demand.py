## Functions
import printfunc
from getpass import getpass
from passwords import User_passwords 

## Product names
soft_drinks = ["Lemonade", " Coke", " Orange Juice", " Water", 'Dr Pepper', 'Fanta', 'Lucozade']
adult_drinks = ["Vodka Lemonade", " Rum and Coke", " Pint", " House Red", " House White"]
sandwiches = ['BLT', ' Egg and Cress', ' Chicken and Stuffing', ' Tuna Sweetcorn', ' Ham and Cheese', ' Smoked Salmon and Cream Cheese']
snacks = ['Cheese and Onion Crisps', 'Ready Salted Crisps', 'Prawn Cocktail Crisps', 'McCoys Steak Crisps', 'Sour Cream Pringles']
confec = ['KitKat 4', 'KitKat Chunky', 'Snickers', 'Mars Bar', 'Lion Bar', 'Kinder Bueno', 'Twix', 'Chocolate Chip Cookie', 'Sugared Ring Donut']

## Login Screen

name = input('Username:\n')
password = getpass('Password:\n')

if User_passwords[name]==password:


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

        choice = input()
        if choice == '1':
            print('Please use the terminal to browse the menus:\n'
            '\n''\033[1m'
            '1) Sandwiches \n'
            '2) Snacks\n'
            '3) Soft Drinks\n'
            '4) Alcohol\n'
            '5) Confectionary\n'
            '0) Exit' '\033[0m')
            
            choice =input('Please enter your desired number below \n')
            if choice == '1':
                print(*sandwiches, sep = ',')
                
                printfunc.item_options(sandwiches)
            
            elif choice =='2':
                print(*snacks, sep = ',')

                printfunc.item_options(snacks)
            elif choice == '3':
                print(*soft_drinks, sep = ',')

                printfunc.item_options(soft_drinks)
            elif choice == '4':
                
                age = int(input(f'How old are you?\n'))
                if age < 18:
                    continue
                
                print(*adult_drinks, sep = ',')

                printfunc.item_options(adult_drinks)
            elif choice == '5':
                print(*confec, sep = ',')

                printfunc.item_options(confec)
            elif choice == '0':
                continue
            
        elif choice == '2':
            print('Deliverwho v.0.0.1')
            input('Press enter to return to main menu')
        elif choice == '3':
            print('Welcome to the Deliverwho? ordering system.\n')
            
        elif choice == '0':
            exitloop = True
            exit()
       
        


