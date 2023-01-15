import pandas as pd
from tabulate import tabulate
import mysql.connector as myc
import matplotlib.pyplot as plt

con = myc.connect(host = "localhost", user = "root", password = "root", database = "inventory")
cursor=con.cursor()

def show_item():
    try:
        df = pd.read_sql("select * from ITEM",con)
        print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))
    except:
        print("Error : Wrong input\nTry again")

def show_customer():
    try:
        df = pd.read_sql("select * from CUSTOMER",con)
        print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))
    except:
        print("Error : Wrong input\nTry again")

def show_supplier():
    try:
        df = pd.read_sql("select * from SUPPLIER",con)
        print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))
    except:
        print("Error : Wrong input\nTry again")

def show_sale():
    try:
        starting_date = input("Enter Starting Date (yyyy/mm/dd) : ")
        ending_date = input("Enter Ending Date (yyyy/mm/dd) : ")
        df = pd.read_sql("select * from SALE_MASTER where Sale_date between '{}' and '{}';".format(starting_date,ending_date),con)
        print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))
    except:
        print("Error : Wrong input\nTry again")

def show_purchase():
    try:
        starting_date = input("Enter Starting Date (yyyy/mm/dd) : ")
        ending_date = input("Enter Ending Date (yyyy/mm/dd) : ")
        df = pd.read_sql("select * from PURCHASE_MASTER where Purchase_date between '{}' and '{}';".format(starting_date,ending_date),con)
        print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))
    except:
        print("Error : Wrong input\nTry again")

def best_product():
    try:
        starting_date = input("Enter Starting Date (yyyy/mm/dd) : ")
        ending_date = input("Enter Ending Date (yyyy/mm/dd) : ")
        q = "select s2.Item_no, sum(s2.Qty) as total from SALE_MASTER s1, SALE_DETAIL s2 \
            where s1.Sale_id = s2.Sale_id and s1.Sale_date between '{}' and '{}' \
            group by s2.Item_no;".format(starting_date,ending_date)
        df = pd.read_sql(q,con)
        print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))
        plt.bar(df.Item_no,df.total)
        plt.xlabel("Item Number")
        plt.ylabel("Qty")
        plt.title("Best Selling Product")
        plt.xticks(df.Item_no)
        plt.show()
    except:
        print("Error : Wrong input\nTry again")

def sale_performance():
    try:
        y = input("Enter Year : ")
        q = "select month(Sale_date) as month, sum(Total) \
            as total from SALE_MASTER where year(Sale_date) = '{}' \
            group by month(Sale_date);".format(y)
        df = pd.read_sql(q,con)
        print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))
        plt.plot(df.month,df.total)
        plt.xlabel("Month")
        plt.ylabel("Total Sale")
        plt.xticks(df.month)
        plt.show()
    except:
        print("Error : Wrong input\nTry again")
