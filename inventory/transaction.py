import pandas as pd
from tabulate import tabulate
import mysql.connector as myc
import matplotlib.pyplot as plt

con = myc.connect(host = "localhost", user = "root", password = "root", database = "inventory")
cursor=con.cursor()

def purchase():
    try:
        purchase_id = 0
        total = 0
        grand = 0
        ch = 'y'
        l = []
        q = "select max(Purchase_id) as largest from PURCHASE_MASTER"
        cursor.execute(q)
        r = cursor.fetchone()[0]
        if r:
            purchase_id = r + 1
        else:
            purchase_id = 1
        purchase_date = input("Enter Purchase Date [yyyy/mm/dd] : ")
        sale_id = int(input("ENter Supplier ID : "))
        cursor.execute("select * from supplier where Supplier_id = {};".format(sale_id))
        if cursor.fetchone():
            print("Item Details")
            df = pd.read_sql("select * from ITEM",con)
            print(tabulate(df ,headers = 'keys', tablefmt = 'psql' , showindex = False))
            while(ch == 'y'):
                item_no = int(input("Enter Item No : "))
                cursor.execute("select * from ITEM where Item_no = {};".format(item_no))
                r1 = cursor.fetchone()
                if r1:
                    qty = int(input("Enter QTY : "))
                    rate = r1[2]
                    total = qty * rate
                    grand = grand + total
                    t = (purchase_id,item_no,qty,rate,total)
                    l.append(t)
                else:
                    print("Item Not Found")
                ch = input("Do you whish to add more items in bucket? (y/n)\nInput : ")
                q1 = "insert into PURCHASE_MASTER values( {}, '{}', {}, {});".format(purchase_id,purchase_date,sale_id,grand)
                cursor.execute(q1)
                con.commit()
                q2 = "insert into PURCHASE_DETAIL values(%s, %s, %s, %s, %s);"
                cursor.executemany(q2,l)
                con.commit()
                cursor.executemany("insert into PURCHASE_TEMP values(%s, %s, %s, %s, %s);",l)
                con.commit()
                q3 = "update ITEM join PURCHASE_TEMP using(Item_no) set Item.Qty_on_hand = Item.Qty_on_hand+PURCHASE_TEMP.Qty"
                cursor.execute(q3)
                con.commit()
                cursor.execute("delete from PURCHASE_TEMP")
                con.commit()
                print("Item Purchases and Added Successfullf")
        else:
            print("Supplier Not Found")
    except:
        print("Error : Wrong input\nTry again")

def sale():
    try:
        sale_id = 0
        total = 0
        grand = 0
        ch = 'y'
        l = []
        q = "select max(Sale_id) as largest from SALE_MASTER"
        cursor.execute(q)
        r = cursor.fetchone()[0]
        if r:
            sale_id = r + 1
        else:
            sale_id = 1
        sale_date = input("Enter Purchase Date [yyyy/mm/dd] : ")
        supplier_id = int(input("Enter Supplier ID : "))
        cursor.execute("select * from supplier where Supplier_id = {};".format(supplier_id))
        if cursor.fetchone():
            print("Item Details")
            df = pd.read_sql("select * from ITEM",con)
            print(tabulate(df ,headers = 'keys', tablefmt = 'psql' , showindex = False))
            while(ch == 'y'):
                item_no = int(input("Enter Item No : "))
                cursor.execute("select * from ITEM where Item_no = {};".format(item_no))
                r1 = cursor.fetchone()
                if r1:
                    qty = int(input("Enter QTY : "))
                    rate = r1[2]
                    total = qty * rate
                    grand = grand + total
                    t = (sale_id,item_no,qty,rate,total)
                    l.append(t)
                else:
                    print("Item Not Found")
                ch = input("Do you whish to add more items in bucket? (y/n)\nInput : ")
                q1 = "insert into SALE_MASTER values( {}, '{}', {}, {});".format(sale_id,sale_date,supplier_id,grand)
                cursor.execute(q1)
                con.commit()
                q2 = "insert into SALE_DETAIL values(%s, %s, %s, %s, %s);"
                cursor.executemany(q2,l)
                con.commit()
                cursor.executemany("insert into SALE_TEMP values(%s, %s, %s, %s, %s);",l)
                con.commit()
                q3 = "update ITEM join SALE_TEMP using(Item_no) set Item.Qty_on_hand = Item.Qty_on_hand-SALE_TEMP.Qty"
                cursor.execute(q3)
                con.commit()
                cursor.execute("delete from SALE_TEMP")
                con.commit()
                print("Item Sold and Subtracted Successfullfy")
        else:
            print("Supplier Not Found")
    except:
        print("Error : Wrong input\nTry again")
