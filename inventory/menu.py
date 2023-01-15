import item
import customer
import supplier
import transaction
import report
import pandas as pd
from tabulate import tabulate
import mysql.connector as myc
import matplotlib.pyplot as plt

con = myc.connect(host = "localhost", user = "root", password = "root", database = "inventory")
cursor=con.cursor()


while(True):
    print("\nEnter your choice\n1. Items\n2. Customers\
          \n3. Suppliers\n4. Transaction\n5. Report\n6. Exit")
    ch = int(input("Input : "))
    if ch == 1:
        while(True):
            print("\nEnter your choice\n1. Add Items\n2. Edit Item\
                  \n3. Fix Rate\n4. Search Item\n5. Delete Item\n6. Exit/Main Menu")
            ch = int(input("Input : "))
            if ch == 1:
                item.add_item()
            elif ch == 2:
                item.edit_item()
            elif ch == 3:
                item.fix_rate()
            elif ch == 4:
                item.search_item()
            elif ch == 5:
                item.delete_item()
            elif ch == 6:
                break

    elif ch == 2:
        while(True):
            print("\nEnter your choice\n1. Add Customer\n2. Edit Customer\
                  \n3. Search Customer\n4. Delete Customer\n5. Exit/Main Menu")
            ch = int(input("Input : "))
            if ch == 1:
                customer.add_customer()
            elif ch == 2:
                customer.edit_customer()
            elif ch == 3:
                customer.search_customer()
            elif ch == 4:
                customer.delete_customer()
            elif ch == 5:
                break
    
    elif ch == 3:
        while(True):
            print("\nEnter your choice\n1. Add Supplier\n2. Edit Supplier\
                  \n3. Search Supplier\n3. Delete Supplier\n5. Exit/Main Menu")
            ch = int(input("Input : "))
            if ch == 1:
                supplier.add_supplier()
            elif ch == 2:
                supplier.edit_supplier()
            elif ch == 3:
                supplier.search_supplier()
            elif ch == 4:
                supplier.delete_supplier()
            elif ch == 5:
                break
    
    elif ch == 4:
        while(True):
            print("\nEnter your choice\n1. Sale\n2. Purchase\n3. Exit/Main Menu")
            ch = int(input("Input : "))
            if ch == 1:
                transaction.sale()
            elif ch == 2:
                transaction.purchase()
            elif ch == 3:
                break
    
    elif ch == 5:
        while(True):
            print("\nEnter your choice\n1. Item Details\n2. Customer Details\
                  \n3. Supplier Details\n4. Sale Report\n5. Purchase Report\
                  \n6. Best Selling Report\n7. Sales Performance\n8. Exit/Main Menu")
            ch = int(input("Input : "))
            if ch == 1:
                report.show_item()
            elif ch == 2:
                report.show_customer()
            elif ch == 3:
                report.show_supplier()
            elif ch == 4:
                report.show_sale()
            elif ch == 5:
                report.show_purchase()
            elif ch == 6:
                report.best_product()
            elif ch == 7:
                report.sale_performance()
            elif ch == 8:
                break
    
    elif ch == 6:
        break
