import os
import products

def print_list(list):
        index = 0
        for x in list:
            print(index, x)
            index += 1

def item_options(list):

    print('Options:\n1) Add \n2) Edit \n3) Delete\n4) Return to Main Menu')
    choice = input()
    if choice == '1':
            new_entry =input('please type the product name you would like to add\n')
            price = float(input('please type the price of the item'))
            list[new_entry] = price
        
    elif choice == '2':
           
            print_list(list)
            edit_entry = int(input('Select an item number to edit\n'))
            
            list[edit_entry] = input("Enter new item here\n")
    elif choice == '3':
            print_list(list)
            del_entry = int(input('Select an item number to delete\n'))
            list.remove(del_entry)

def clear_term(): #clears the terminal
    os.system('clear')

def age_check(age, min_age):
        min_age = 18
        try:
                age = int(input('How old are you?'))
        except:
                print('You have not entered an age')
                return False

        if age < min_age: 
                return False
        else: 
                return True
        