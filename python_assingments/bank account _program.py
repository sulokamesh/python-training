print("==========================")
print("welcome to theresa school")
print("==========================")
customer_master_list= [
    ["STU001","ARJUNKUMAR","savings","25000"],
    ["STU002","PRIYA","current","45000"],
    ["STU003","karthick","savings","35000"],
    ["STU004","divya","current","50000"]
]
while True:
     print("1.create account")
     print("2.deposit account")
     print("3.withdraw account")
     print("4.check balance")
     print("5.delete account")
     print("6.delete Exit")
     choice=int(input("enter your choice:....."))
     if choice == 1:
        print("you selected create account")
        account_no=input("enter the account number:")
        name=input("enter the customer name")
        account_type=input("enter account type")
        balance=int(input("enter balance"))
        customer_list=[account_no,name,account_type,balance]
        customer_master_list.append(customer_list)
        print("student data successfully added")
     elif choice == 2:
         print("you selectedto deposit amount")
         if len(customer_master_list)==0:
             print("the master list empty please add customer details")
             continue
         account_no=input("enter account number:")
         customer_present=False
         for customer in customer_master_list:
             if customer [0]==account_no:
                 customer_present=True
                 print("1.customer name is:",customer[1])
                 print("2.account type:",customer[2])
                 print("3.current balance:",customer[3])
                 deposit_amount=int(input("enter deposit amount:"))
                 customer[3]=int(customer[3])+deposit_amount
                 print("Amount deposited succesfully.")
                 print("updated balance:",customer[3])
                 break
             if customer_present==False:
                 print("the given accont number is not correct")
     elif choice == 3:
         print("you selectedto deposit amount")
         if len(customer_master_list)==0:
             print("the master list empty please add customer details")
             continue
         account_no=input("enter account number:")
         customer_present=False
         for customer in customer_master_list:
             if customer [0]==account_no:
                 customer_present=True
                 print("1.customer name is:",customer[1])
                 print("2.account type:",customer[2])
                 print("3.current balance:",customer[3])
                 print(type(customer[3]))
                 withdraw_amount=int(input("enter withdraw amount:"))
                 if withdraw_amount<=int(customer[3]):
                     customer[3]=int(customer[3])-withdraw_amount
                     print("amount withdrawn succesfully.")
                     print("updated balance:",customer[3])
                 else:
                      print("insufficient balance.")
                 break
         if customer_present==False:
                print("the given accont number is not correct")

     elif choice == 4:
         print("you selectedto check balance")
         if len(customer_master_list)==0:
             print("the master list empty please add customer details")
             continue
         account_no=input("enter account number:")
         customer_present=False
         for customer in customer_master_list:
             if customer [0]==account_no:
                 customer_present=True
                 print("1.customer name is:",customer[1])
                 print("2.account type:",customer[2])
                 print("3.available balance:",customer[3])
                 break
         if customer_present==False:
              print("the given account number is notcorrect.")
     elif choice == 5:
         print("you selectedto delete account")
         if len(customer_master_list)==0:
             print("the master list empty please add customer details")
             continue
         account_no=input("enter account number:")
         customer_present=False
         for customer in customer_master_list:
             if customer [0]==account_no:
                 customer_present=True
                 print("1.customer name is:",customer[1])
                 print("2.account type:",customer[2])
                 print("3.balance:",customer[3])
                 customer_master_list.remove(customer)
                 print("customer account deleted successfully.")
                 break
         if customer_present==False:
              print("the given account number is not correct.")
     elif choice == 6:
          print("thank you for using SBI Bank")
          break
     else:
          print("invalid choice.please try again.")
          
                
                 









                 
                 
