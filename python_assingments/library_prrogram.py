book_master_list=[
    {"book_id": "B101", "book_name": "Python Programming", "author": "Reema Thareja", "price": 550, "status": "Available"},
    {"book_id": "B102", "book_name": "C Programming", "author": "E. Balagurusamy", "price": 450, "status": "Available"},
    {"book_id": "B103", "book_name": "Data Structures", "author": "Seymour Lipschutz", "price": 600, "status": "Available"},
    {"book_id": "B104", "book_name": "Java Programming", "author": "Herbert Schildt", "price": 700, "status": "Available"},
    {"book_id": "B105", "book_name": "Database Management System", "author": "Korth", "price": 650, "status": "Available"}
]
issue_book_list=[]
def add_book():
    book_id=input("enter the book_id")
    name=input("enter the book_name")
    price=int(input("enter the price"))
    author=input("enter the author ")
    status=input("enter the status")
    temp={}
    temp["book_id"]=book_id
    temp["book_name"]=name
    temp["price"]=price
    temp["author"]=author
    temp["status"]=status
    print("book successfully added")
    book_master_list.append(temp)
def display_book():
    if len(book_master_list)==0:
        print("the master list empty please add few book menu to display")
        return False
    book_id=input("enter the book id to display")
    book_present=False
    for book in book_master_list:
       if book["book_id"]==book_id:
            book_present=True
            print("book_name is:",book["book_name"])
            print("book_price is:",book["price"])
            print("book_author is:",book["author"])
            print("book_status:",book["status"])
    if book_present==False:
        print("the given book id is incorrect")
def search_book():
    if len(book_master_list)==0:
        print("the master list empty please add few book to search")
        return False                                                                                                         
    book_id=input("enter the book id to search")
    book_present=False
    for book in book_master_list:
       if book["book_id"]==book_id:
            book_present=True
            print("book_name is:",book["book_name"])
            print("book_price is:",book["price"])
            print("book_author is:",book["author"])
            print("book_status:",book["status"])
    if book_present==False:
          print("the given book id number is incorrect")
def update_book():
    if len(book_master_list)==0:
        print("the master list is empty please add some book details to update")
        return False
    book_id=input("enter the book id ")
    book_present=False
    for book in book_master_list:
        if book["book_id"]==book_id:
            book_present=True
            print("1.book_name is:",book["book_name"])
            print("2.book_price is:",book["price"])
            print("3.book_author is:",book["author"])
            print("4.book_status:",book["status"])
1            modify = int(input("Enter Field Number : "))
            col_dict = {
                    1: "name",
                    2: "price",
                    3: "status"
                }
            new_value = input("Enter New Value : ")
            book[col_dict[modify]] = new_value

    if book_present==False:
          print("the given item id number is incorrect")
def delete_book():
    print("delete book")
    if len(book_master_list)==0:
        print("the master list is empty please add some book details to delete")
        return False
    book_id=input("enter the book id ")
    book_present=False
    for book in book_master_list:
        if book["book_id"]==book_id:
            book_present=True
            print("1.book_name is:",book["book_name"])
            print("2.book_price is:",book["price"])
            print("3.book_author is:",book["author"])
            print("4.book_status:",book["status"])
            confirm=input("are you sure(yes/no):")
            if confirm.lower()=="yes":
                book_master_list.remove(book)
                print("deleted successfully")
    
    if book_present==False:
           print("the given item id number is incorrect")
def issue_book():
    print("issue book")
    if len(book_master_list)==0:
        print("the master list is empty please add some book details to issue")
        return False
    book_id=input("enter the book id ")
    book_present=False
    for book in book_master_list:
        if book["book_id"]==book_id:
            book_present=True
            issue_date=input("enter your date")
            print("1.book_name is:",book["book_name"])
            print("2.book_price is:",book["price"])
            print("3.book_author is:",book["author"])
            print(".book_status:",book["status"])
            print("issue date:",issue_date)
            issue_book_list.append(book)
            
        if book_present==False:
           print("the given item id number is incorrect")
def return_book():
    if len(book_master_list)==0:
        print("the master list is empty please add some book details to return date")
        return False
    book_id=input("enter the book id ")
    book_present=False
    for book in book_master_list:
        if book["book_id"]==book_id:
            book_present=True
            return_date=input("enter the return date")
            print("1.book_name is:",book["book_name"])
            print("2.book_price is:",book["price"])
            print("3.book_author is:",book["author"])
            print(".book_status:",book["status"])
            print("return_date:",return_date)
            
        if book_present==False:
           print("the given item id number is incorrect")

    


    

while True:
    choice=int(input("enter the operation"))
    if choice==1:
        print("you selected to add book")
        add_book()
    elif choice==2:
        print("you selected to display book")
        display_book()
    elif choice==3:
        print("you selected to search book")
        search_book()
    elif choice==4:
        print("you selected to update book")
        update_book()
    elif choice==5:
        print("you selected to delete book")
        delete_book()
    elif choice==6:
        print("you selected to issue book")
        issue_book()
    elif choice==7:
        print("you selected to return book")
        return_book()
    elif choice==8:
        print("exit")
        
    else:
        print("enter the valid input between 1 to 8")
        break
        

        










        












        
