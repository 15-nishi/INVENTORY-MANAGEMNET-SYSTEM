import pandas as pd
from tabulate import tabulate
import mysql.connector as myc
import matplotlib.pyplot as plt

con = myc.connect(host = "localhost", user = "root", password = "root", database = "inventory")
cursor=con.cursor()

def add_customer():
    try:
        customer_id      = int(input("\nEnter Customer ID : "))
        customer_name    = input("Enter Customer Name : ")
        customer_address = input("Enter Customer Address : ")
        customer_mobile  = int(input("Enter Customer Mobile : "))
        cursor.execute("insert into CUSTOMER values({}, '{}', '{}', '{}');".format(customer_id,customer_name,customer_address,customer_mobile))
        con.commit()
        print("Customer Edited Successfully")
    except:
        print("Error : Wrong input\nTry again")

def edit_customer():
    try:
        customer_id = int(input("\nEnter Customer ID : "))
        cursor.execute("select * from CUSTOMER where Customer_id = {};".format(customer_id))
        if cursor.fetchone():
            customer_address = input("Enter New Address")
            cursor.execute("update CUSTOMER set Customer_address = '{}' where Customer_id = {};".format(customer_address,customer_id))
            con.commit()
            print("Customer Info Edited Sucessfully")
        else:
            print("Customer Not Found")
    except:
        print("Error : Wrong input\nTry again")

def search_customer():
    try:
        while(True):
            try:
                print("\nEnter your choice\n1. Search Customer by ID \n2. Search Customer by Name\n3. Search Customer by Address\n4. Search Customer by Mobile _no.\n5. Exit/Main Menu")
                ch = int(input("Input : "))
                if ch == 1:
                    customer_id = int(input("Enter Customer ID : "))
                    q = "select * from CUSTOMER where Customer_id = {};".format(customer_id)
                    cursor.execute(q)
                    if cursor.fetchall():
                        df=pd.read_sql(q,con)
                        print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))
                    else:
                        print("Customer Not Found")
                elif ch == 2:
                    customer_name = input("Enter Customer Name : ")
                    q = "select * from CUSTOMER where Customer_name like '%{}%';".format(customer_name)
                    cursor.execute(q)
                    if cursor.fetchall():
                        df=pd.read_sql(q,con)
                        print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))
                    else:
                        print("Customer Not Found")
                elif ch == 3:
                    customer_address = input("Enter Customer Address : ")
                    q = "select * from CUSTOMER where Customer_address like '%{}%';".format(customer_address)
                    cursor.execute(q)
                    if cursor.fetchall():
                        df=pd.read_sql(q,con)
                        print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))
                    else:
                        print("Customer Not Found")
                elif ch == 4:
                    customer_mobile = int(input("Enter Customer Mobile_no. : "))
                    q = "select * from CUSTOMER where Customer_mobile = {};".format(customer_mobile)
                    cursor.execute(q)
                    if cursor.fetchall():
                        df=pd.read_sql(q,con)
                        print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))
                    else:
                        print("Customer Not Found")
                elif ch == 5:
                    break
            except:
                print("Error : Wrong input\nTry again")
    except:
        print("Error : Wrong input\nTry again")
        
def delete_customer():
    try:
        customer_id = int(input("Enter Customer ID : "))
        q = "select * from CUSTOMER where Customer_id = {};".format(customer_id)
        cursor.execute(q)
        if cursor.fetchone():
            cursor.execute("delete from CUSTOMER where Customer_id = {};".format(customer_id))
            con.commit()
            print("Customer Deleted Successfully")
        else:
            print("Customer Not Found")
    except:
        print("Error : Wrong input\nTry again")
