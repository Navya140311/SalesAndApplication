from tkinter import *
import random
root=Tk()
root.title("Sales Application")
root.geometry("600x600")

month_label = Label(root)
profit_label = Label(root)
max_profit_label = Label(root)
min_profit_label = Label(root)

months=("January","February","March","April","June","July","August","September","October","November","December")
profits=(10000,20000,30000,40000,50000,60000,70000,80000,90000,13000,11000,12000)

month_label["text"]= "Months : January,February,March,April,June,July,August,September,October,November,December"
profit_label["text"]="10000,20000,30000,40000,50000,60000,70000,80000,90000,13000,11000,12000"
def func_profit():

   max_profit= max(profits)
   print(max_profit)

   max_profit_index= profits.index(max_profit)
   print(max_profit_index)

   max_profit_month=months[max_profit_index]

   print("The max profit of "+ str(max_profit)+"   was recorded in the month of: "+ str(max_profit_month))
   max_profit_label["text"]= "The max profit of "+ str(max_profit)+" was recorded in the month of: "+ str(max_profit_month)



   min_profit= min(profits)
   print(min_profit)

   min_profit_index= profits.index(min_profit)
   print(min_profit_index)

   min_profit_month=months[min_profit_index]

   print("The min profit of "+ str(min_profit)+"   was recorded in the month of: "+ str(min_profit_month))
   min_profit_label["text"]= "The min profit of "+ str(min_profit)+" was recorded in the month of: "+ str(min_profit_month)
    
month_label.place(relx=0.5, rely=0.3, anchor=CENTER)
profit_label.place(relx=0.5, rely=0.4, anchor=CENTER)
min_profit_label.place(relx=0.5, rely=0.5, anchor=CENTER)
max_profit_label.place(relx=0.5, rely=0.6, anchor=CENTER)
btn1= Button(root,text="Show max and min profits",command=func_profit)
root.mainloop()