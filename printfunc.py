import os

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
            list.append(new_entry)
        
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
