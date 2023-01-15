import pandas as pd
from tabulate import tabulate
import mysql.connector as myc
import matplotlib.pyplot as plt
import os

con = myc.connect(host = "localhost", user = "root", password = "root", database = "inventory")
cursor=con.cursor()

def add_item():
    try:
        item_no       = int(input("\nEnter Item No. : "))
        item_name     = input("Enter Item Name : ")
        purchase_rate = float(input("Enter Purchase Rate : "))
        sale_rate     = float(input("Enter Sale Rate : "))
        qty_on_hand   = int(input("Enter Qty On Hand : "))
        cursor.execute("insert into ITEM values({},'{}',{},{},{});".format(item_no,item_name,purchase_rate,sale_rate,qty_on_hand))
        con.commit()
        print("Item Added successfully")
    except:
        print("Error : Wrong input\nTry again")

def edit_item():
    try:
        item_no = int(input("\nEnter Item No. : "))
        q = "select * from ITEM where Item_no = {};".format(item_no)
        cursor.execute(q)
        if cursor.fetchone():
            item_name = input("Enter New Item Name : ")
            cursor.execute("update ITEM set Item_name = '{}' where Item_no = {};".format(item_name,item_no))
            con.commit()
            print("Item Info Edited Successfully")
        else:
            print("Item Not Found")
    except:
        print("Error : Wrong input\nTry again")

def fix_rate():
    try:
        item_no = int(input("\nEnter Item No. : "))
        q = "select * from ITEM where Item_no = {};".format(item_no)
        cursor.execute(q)
        if cursor.fetchone():
            purchase_rate = int(input("Enter New Purchase Rate : "))
            sale_rate = int(input("Enter New Sale Rate : "))
            cursor.execute("update ITEM set Purchase_rate = {}, Sale_rate = {} where Item_no = {};".format(purchase_rate,sale_rate,item_no))
            con.commit()
            print("New Rate Updated Successfully")
        else:
            print("Item Not Found")
    except:
        print("Error : Wrong input\nTry again")

def search_item():
    try:
        item_no = int(input("\nEnter Item No. : "))
        q = "select * from ITEM where Item_no = {};".format(item_no)
        cursor.execute(q)
        if cursor.fetchone():
            df = pd.read_sql(q,con)
            print(tabulate(df,headers ='key' ,tablefmt = 'psql', showindex = False))
        else:
            print("Item Not Found")
    except:
        print("Error : Wrong input\nTry again")

def delete_item():
    try:
        item_no = int(input("\nEnter Item No. : "))
        cursor.execute("select * from ITEM where Item_no = {};".format(item_no))
        if cursor.fetchone():
            cursor.execute("delete from ITEM where Item_no = {};".format(item_no))
            con.commit()
            print("Item Deleted Successfully")
        else:
            print("Item Not Found")
    except:
        print("Error : Wrong input\nTry again")
