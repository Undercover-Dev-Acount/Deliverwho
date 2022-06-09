import os
import products
import pymysql
from prettytable import from_db_cursor
from dotenv import load_dotenv

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
        cursor = connection.cursor

def close_DB(connection):
        connection.close()

def commit_DB(connection):
        connection.commit()


def insert_to_DB(table_name, product_name, price):
        cursor = connection.cursor()

        sql = f"INSERT INTO {table_name} (Product, Price) VALUES (%s, %s)"
        val = (product_name, price)
        cursor.execute(sql, val)

def delete_from_DB(table_name, product_ID):
        cursor = connection.cursor()

        sql = f"DELETE FROM {table_name} WHERE (Product_ID) = {product_ID}"
        
        cursor.execute(sql)

def update_price_DB(table_name, product_ID, price):
        cursor = connection.cursor()

        sql = f"UPDATE {table_name} SET Price = {price} WHERE Product_ID = {product_ID}"
        
        cursor.execute(sql)

def print_from_DB(table_name):
        cursor = connection.cursor()
        cursor.execute(f"SELECT Product, Price, Product_ID FROM {table_name}")
        mytable = from_db_cursor(cursor)

        print(mytable)

def print_list(list):
        index = 0
        for x in list:
            print(index, x)
            index += 1

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
        