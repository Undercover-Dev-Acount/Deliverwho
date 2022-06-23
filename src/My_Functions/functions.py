import os
import pymysql
from prettytable import from_db_cursor
from dotenv import load_dotenv
import random 
import sys
import hashlib
from getpass import getpass
import json

## DB Declaration
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

connection = pymysql.connect(
                host,
                user,
                password,
                database
        )
cursor = connection.cursor
def get_DB():
        # Try to establish a database connection
        try:
                connection = pymysql.connect(
                        host,
                        user,
                        password,
                        database
                )

                return connection
        except:
                print("Can't connect to database")
                return 0
        
##===========================Connection Close and Commits===========================================
def close_DB(connection):
        connection.close()

def commit_DB(connection):
        connection.commit()

##==========================DB Functions============================================================

## Insert ----------------------
def insert_to_DB(table_name, product_name, price):
        cursor = connection.cursor()

        sql = f"INSERT INTO {table_name} (Product, Price) VALUES (%s, %s)"
        val = (product_name, price)
        cursor.execute(sql, val)

## Delete ----------------------
def delete_from_DB(table_name, product_ID):
        cursor = connection.cursor()

        sql = f"DELETE FROM {table_name} WHERE (Product_ID) = {product_ID}"
        
        cursor.execute(sql)


## Update Price ------------------------
def update_price_DB(table_name, product_ID, price):
        cursor = connection.cursor()

        sql = f"UPDATE {table_name} SET Price = {price} WHERE Product_ID = {product_ID}"
        
        cursor.execute(sql)

## Print ----------------------------------
def print_from_DB(table_name):
        cursor = connection.cursor()
        cursor.execute(f"SELECT Product, Price, Product_ID FROM {table_name}")
        mytable = from_db_cursor(cursor)

        print(mytable)


## Create Order --------------------------
def create_order():
        
        Customer_Name = input("Please enter the Customer's name\n")
        Address = input("Please enter the Customer's address\n")
        Phone_Number = input("Please enter the Customer's Phone Number\n")
        Order_Status = "Placed"
        Courier_ID = random.randint(1,3)
        Order_Placed = getdate()
        Order_Data = [Customer_Name, Address, Phone_Number, Order_Status, Courier_ID, Order_Placed]

        return Order_Data


## Save Order --------------------------        
def save_order(Order_Data, connection):
        cursor = connection.cursor()

        sql = "INSERT INTO Orders (Customer_Name, Address, Phone_Number, Order_Status, Courier_ID, Order_Placed) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (Order_Data)
        cursor.execute(sql, val)
        commit_DB(connection)


## Edit Order -------------------------
def update_order_DB(table_name, connection):
        cursor = connection.cursor()

        print_from_order_DB(table_name, connection)
        
        order_choice = input('Which order number would you like to edit?\n')
        column_choice = input('Which column would you like to update?\n')
        if column_choice == "Order_Placed":
                print('Please choose a different column or enter 9 to exit')
                column_choice = input('Which column would you like to update?\n')
                if column_choice == "9":
                        
                        return
        
        update_value = input('What would you like to set the new value to?\n')

        
        sql = f"UPDATE {table_name} SET {column_choice} = '{update_value}' WHERE Order_Number = {order_choice}"
        
        cursor.execute(sql)
        commit_DB(connection)
        print("You have successfully updated your order")

## Delete Order ----------------------------

def delete_from_order_DB(table_name, connection):
        cursor = connection.cursor()
        
        print_from_order_DB(table_name, connection)
        
        Order_Number = input("Please enter the Order Number you would like to delete\n")
        if Order_Number:
                sql = f"DELETE FROM {table_name} WHERE (Order_Number) = {Order_Number}"
                
                cursor.execute(sql)
                commit_DB(connection)
                print(f"Order Number {Order_Number} deleted")
        
        else:
                print("No order was deleted")




## Print Order List ----------------------------------
def print_from_order_DB(table_name, connection):
        
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        mytable = from_db_cursor(cursor)

        print(mytable)
        


## ========================== Item Options (Add, Edit, Delete) ================================================================================

def item_options(table_name):

    print('Options:\n1) Add \n2) Edit Price \n3) Delete\n4) Return to Main Menu')
    choice = input()
    if choice == '1':
            clear_term()
            print_from_DB(table_name)
            product_name = input('please type the product name you would like to add\n')
            price = float(input('please type the price of the item\n'))
            insert_to_DB(table_name, product_name, price)
            commit_DB(connection)
        
    elif choice == '2':
           
            clear_term()
            print_from_DB(table_name)
            product_ID = int(input('Select a product ID to edit\n'))
            price = input('Please select the new price\n')
            update_price_DB(table_name, product_ID, price)
            commit_DB(connection)
        
    elif choice == '3':
            clear_term()
            print_from_DB(table_name)
            product_ID = input('Select a product ID to delete\n')
            delete_from_DB(table_name, product_ID)
            commit_DB(connection)
     

        
## =========================Terminal Clear =====================================================================================
def clear_term(): 
    os.system('clear')

## =========================Age Check===========================================================================================
def age_check(age, min_age): 
        min_age = 18
        try:
                age = int(input('How old are you?\n'))
        except:
                print('You have not entered an age')
                return False

        if age < min_age: 
                return False
        else: 
                return True
        
##=========================SQL DateTime==========================================================================================
def getdate():
    cursor = connection.cursor()
    
    date = "SELECT SYSDATE() as dt"
    sql = date
    cursor.execute(sql)
    date = cursor.fetchone()
    print('Order placed at:', date[0])
    return date[0]


## ======================== List Print (non-DB)
def print_list(list):
        index = 0
        for x in list:
            print(index, x)
            index += 1

def log_in_check(connection):
       

        name = input('Username:\n')
        password = getpass('Password:\n')

        name = name.encode('utf-8')
        password = password.encode('utf-8')
        
        hash_name = hashlib.sha1(name).hexdigest()
        hash_pass = hashlib.sha1(password).hexdigest()
        

        hashed_db_data = get_hashed_data(connection)

        if hashed_db_data[hash_name]==hash_pass:
                return True
        else:
                return False
        
        

def get_hashed_data(connection):
        cursor = connection.cursor()

        sql1 = f"SELECT User_Name FROM Passwords"
        
        cursor.execute(sql1)
        hash_name_db = []
        for row in cursor:
                hash_name_db.append(row[0])
        
        sql2= f'SELECT Password FROM Passwords'
        cursor.execute(sql2)
        hash_pass_db = []
        for row in cursor:
                hash_pass_db.append(row[0])
        
    
        hashed_db_data = dict(zip(hash_name_db, hash_pass_db))
        return hashed_db_data
