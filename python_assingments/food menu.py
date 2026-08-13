food_master_list=[]
order_list=[]
def add_food_item():
    item_id=input("enter the food item id")
    name=input("enter the food name")
    price=int(input("enter the food price"))
    category=input("enter the food category")
    temp={}
    temp["item_id"]=item_id
    temp["name"]=name
    temp["price"]=price
    temp["category"]=category
    print("food item successfully added")
    food_master_list.append(temp)
def display_food_item():
    if len(food_master_list)==0:
        print("the master list empty please add few food menu to diplay")
        return False
    item_id=input("enter the food item id to display")
    food_present=False
    for food in food_master_list:
       if food["item_id"]==item_id:
            food_present=True
            print("food name is:",food["name"])
            print("food price is:",food["price"])
            print("food category is:",food["category"])
       if food_present==False:
          print("the given item id number is incorrect")
def search_food_item():
    if len(food_master_list)==0:
        print("the master list empty please add few food menu to diplay")
        return False                                                                                                         
    item_id=input("enter the food item id to search")
    food_present=False
    for food in food_master_list:
       if food["item_id"]==item_id:
            food_present=True
            print("food name is:",food["name"])
            print("food price is:",food["price"])
            print("food category is:",food["category"])
       if food_present==False:
          print("the given item id number is incorrect")
def update_food_item():
    if len(food_master_list)==0:
        print("the master list empty please add few food menu to dislay")
        return False
    item_id=input("enter the food item id to update food price")
    food_present=False
    for food in food_master_list:
       if food["item_id"]==item_id:
            food_present=True
            print("food name is:",food["name"])
            print("food price is:",food["price"])
            print("food category is:",food["category"])
            modify = int(input("Enter Field Number : "))
            col_dict = {
                    1: "name",
                    2: "price",
                    3: "category"
                }
            new_value = input("Enter New Value : ")

            if modify == 9:
                    new_value = float(new_value)

            food[col_dict[modify]] = new_value

       if food_present==False:
          print("the given item id number is incorrect")
def delete_food_item():
    print("Delete food")

    if len(food_master_list) == 0:
          print("No food Records Found.")
          return

    item_id = input("Enter item_id : ")

    food_found = False
    index = 0

    for food in food_master_list:

        if food["item_id"] == item_id:

            food_found = True

            confirm = input("Are you sure (yes/no) : ")

            if confirm.lower() == "yes":
                    del food_master_list[index]
                    print("food Deleted Successfully.")
            else:
                    print("Deletion Cancelled.")

            break

            index += 1

        if food_found == False:
            print("food Not Found.")
def place_customer_order():
    if len(food_master_list)==0:
        print("the master list empty please add few food menu to dislay")
        return False
    item_id=input("enter the food item id to update food price")
    food_present=False
    for food in food_master_list:
       if food["item_id"]==item_id:
            food_present=True
            print("food name is:",food["name"])
            print("food price is:",food["price"])
            print("food category is:",food["category"])
            quantity=int(input("enter your quantity"))
            print("order placed successfully")
            order_list.append(food)
       else:
            print("food not available")
def display_customer_order():
    if len(food_master_list)==0:
        print("the master list empty please add few food menu to dislay")
        return False
    item_id=input("enter the food item id to display customer order")
    food_present=False
    for food in food_master_list:
       if food["item_id"]==item_id:
            food_present=True
            print("food name is:",food["name"])
            print("food price is:",food["price"])
            print("food category is:",food["category"])
            print("order displayed successfully")
def calculate_total_bill():
    if len(food_master_list)==0:
        print("the master list empty please add few food menu to dislay")
        return False
    item_id=input("enter the food item id to calculate total bill")
    food_present=False
    for food in food_master_list:
       if food["item_id"]==item_id:
            food_present=True
            quantity=int(input("enter your quantity"))
            total=food["price"]*quantity
            print("food name is:",food["name"])
            print("food price is:",food["price"])
            print("food category is:",food["category"])
            print("food quantity is:",quantity)
            print("total bill is:",total)
            print("thank you visit again")
def display_food_categories():
    food_categories = ("veg", "non-veg", "snacks", "dessert")

    print("Food Categories:")
    for category in food_categories:
        print(category)

    if len(food_master_list) == 0:
        print("The master list is empty. Please add a few food items to display.")
        return False

    item_id = input("Enter the Food catagories: ")

    print("\nShow Food Details:")

    food_present = False

    for food in food_master_list:
        if food["item_id"] == item_id:
            food_present = True

            quantity = int(input("Enter your quantity: "))
            total = food["price"] * quantity

            print("Food Name      :", food["name"])
            print("Food Price     :", food["price"])
            print("Food Category  :", food["category"])
            print("Quantity       :", quantity)
            print("Total Price    :", total)

            break

    if not food_present:
        print("Food Item ID not found.")
def payment_method():
    payment_method = ("cash", "upi", "card", "net banking")

    print("payment method:")
    for payment in payment_method:
        print(payment)

    if len(food_master_list) == 0:
        print("The master list is empty. Please add a few food items to display.")
        return False

    item_id =(input("Enter the payment: "))

    food_present = False

    for food in order_list:
        food_present = True

        quantity = int(input("Enter your quantity: "))
        total = food["price"] * quantity

        print("Food Name      :", food["name"])
        print("Food Price     :", food["price"])
        print("Food Category  :", food["category"])
        print("Quantity       :", quantity)
        print("Total Price    :", total)
        print("payment received successfuly")
    
while True:
     choice=int(input("enter the operation"))
     if choice==1:
        print("you selected to add food item")
        add_food_item()
        
     elif choice==2:
        print("you selected to display food item")
        display_food_item()

     elif choice==3:
        print("you selected to search food item")
        search_food_item()
     elif choice==4:
        print("you selected to updte food price item")
        update_food_item()
     elif choice==5:
        print("you selected to delete food item")
        delete_food_item()
     elif choice==6:
        print("you selected to place order food item")
        place_customer_order()
     elif choice==7:
        print("you selected to display customer order food item")
        display_customer_order()
     elif choice==8:
        print("you selected to total bill")
        calculate_total_bill()
     elif choice==9:
        print("you selected to display food categories")
        display_food_categories()
     elif choice==10:
        print("you selected to payment method")
        payment_method()






        
