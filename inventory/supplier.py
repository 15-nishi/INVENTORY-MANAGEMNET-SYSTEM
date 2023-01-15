import pandas as pd
from tabulate import tabulate
import mysql.connector as myc
import matplotlib.pyplot as plt

con = myc.connect(host = "localhost", user = "root", password = "root", database = "inventory")
cursor=con.cursor()

def add_supplier() :
    try:
        supplier_id      = int(input("\nEnter Supplier ID : "))
        supplier_name    = input("Enter Supplier Name : ")
        supplier_address = input("Enter Supplier Address : ")
        supplier_mobile  = int(input("Enter Supplier Mobile : "))
        cursor.execute("insert into SUPPLIER values({}, '{}', '{}', '{}');".format(supplier_id,supplier_name,supplier_address,supplier_mobile))
        con.commit()
        print("Supplier Edited Successfully")
    except:
        print("Error : Wrong input\nTry again")
 

def edit_supplier():
    try:
        supplier_id = int(input("\nEnter Supplier ID : "))
        cursor.execute("select * from CUSTOMER where Supplier_id = {};".format(supplier_id))
        if cursor.fetchone():
            supplier_address = input("Enter New Address :")
            supplier_name = input("Enter New Supplier Name : ")
            supplier_mobile = int(input("Enter New Mobile no. : "))
            cursor.execute("update SUPPLIER set Supplier_name = '{}' where Supplier_id = {};".format(supplier_name,supplier_id))
            cursor.execute("update SUPPLIER set Supplier_address = '{}' where Supplier_id = {};".format(supplier_address,supplier_id))
            cursor.execute("update SUPPLIER set Supplier_mobile = '{}' where Supplier_id = {};".format(supplier_mobile,supplier_id))
            con.commit()
            print("Supplier Info Edited Sucessfully")
        else:
            print("Supplier Not Found")
    except:
        print("Error : Wrong input\nTry again")
 

def search_supplier():
    try:
        supplier_name = input("Enter Supplier Name : ")
        q = "select * from SUPPLIER where Supplier_name like '%{}%';".format(supplier_name)
        cursor.execute(q)
        if cursor.fetchall():
            df=pd.read_sql(q,con)
            print(tabulate(df, headers = df.columns, tablefmt = 'psql', showindex = False))
        else:
            print("Supplier Not Found")
    except:
        print("Error : Wrong input\nTry again")

def delete_supplier():
    try:
        supplier_id = int(input("Enter Supplier ID : "))
        q = "select * from SUPPLIER where Supplier_id = {};".format(supplier_id)
        cursor.execute(q)
        if cursor.fetchone():
            cursor.execute("delete from SUPPLIER where Supplier_id = {};".format(supplier_id))
            con.commit()
            print("Supplier Deleted Successfully")
        else:
            print("Supplier Not Found")
    except:
        print("Error : Wrong input\nTry again")
