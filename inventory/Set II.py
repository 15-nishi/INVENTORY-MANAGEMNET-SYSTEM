import pandas as pd
import matplotlib.pyplot as plt
d={'cname':['Shruti','Tushar','Jay','Sameer','Mayank','Meena','Dhairya'],
   'city':['Ahmedabad','Baroda','Surat','Ahmedabad','Surat','Baroda','Ahmedabad'],
   'billamt':[9500,5300,4550,4000,8500,4300,3000],
   'tran_date':['2010-10-01','2010-01-04','2009-03-01','2009-04-01','2008-08-05','2008-08-06','2009-10-10']
  }
s=[1001,1002,1003,1004,1005,1006,1007]
customer=pd.DataFrame(d,index=s)
print(customer)

#Answer 1
customer['discount']=customer['billamt']*0.10
print(customer)

#Answer 2
customer.loc[1008]=['Rohan','Bharuch',6000,'2011-04-01',600]
print(customer)

#Answer 3
plt.bar(customer['cname'],customer['billamt'],color=['r','g','b','c','m','y','k'])
plt.title("Report",color='Red')
plt.xlabel("Customer Names",color='Blue')
plt.ylabel("Bill Amount",color='Magenta')
plt.show()
