employee_master_list = [
    {"employee_id": "E001", "name": "Arun Kumar", "age": 28, "gender": "Male", "department": "HR", "designation": "HR Executive", "salary": 300000},
    {"employee_id": "E002", "name": "Priya S", "age": 31, "gender": "Female", "department": "Finance", "designation": "Accountant", "salary": 35000},
    {"employee_id": "E003", "name": "Karthik R", "age": 26, "gender": "Male", "department": "IT", "designation": "Software Developer", "salary": 45000},
    {"employee_id": "E004", "name": "Divya M", "age": 29, "gender": "Female", "department": "Sales", "designation": "Sales Executive", "salary": 32000},
    {"employee_id": "E005", "name": "Suresh B", "age": 40, "gender": "Male", "department": "Admin", "designation": "Office Manager", "salary": 50000}
]
def add_employee():
    employee_id=input("enter the employee_id")
    name=input("enter the name")
    age=int(input("enter the age"))
    gender=input("enter the gender ")
    department=input("enter the department")
    designation=input("enter the designation")
    salary=int(input("enter the salary"))
    temp={}
    temp["employee_id"]=employee_id
    temp["name"]=name
    temp["age"]=age
    temp["gender"]=gender
    temp["department"]=department
    temp["designation"]=designation
    temp["salary"]=salary
    print("employee successfully added")
    employee_master_list.append(temp)
def display_employee():
    if len(employee_master_list)==0:
        print("the master list empty please add few employee menu to display")
        return False
    employee_id=input("enter the employee id to display")
    employee_present=False
    for employee in employee_master_list:
        if employee["employee_id"]==employee_id:
            employee_present=True
            print("employee_name is:",employee["name"])
            print("employee_age is:",employee["age"])
            print("employee_gender is:",employee["gender"])
            print("employee_department:",employee["department"])
            print("employee_designation:",employee["designation"])
            print("employee_salary:",employee["salary"])
    if employee_present==False:
        print("the given employee id is incorrect")
def search_employee():
    if len(employee_master_list)==0:
        print("the master list empty please add few employee menu to search")
        return False
    employee_id=input("enter the employee id to search")
    employee_present=False
    for employee in employee_master_list:
       if employee["employee_id"]==employee_id:
            employee_present=True
            print("employee_name is:",employee["name"])
            print("employee_age is:",employee["age"])
            print("employee_gender is:",employee["gender"])
            print("employee_department:",employee["department"])
            print("employee_designation:",employee["designation"])
            print(employee)
    if employee_present==False:
        print("the given employee id is incorrect")

def update_employee():
    if len(employee_master_list)==0:
        print("the master list empty please add few employee menu to display")
        return False
    employee_id=input("enter the employee id to display")
    employee_present=False
    for employee in employee_master_list:
       if employee["employee_id"]==employee_id:
            employee_present=True
            print("employee_name is:",employee["name"])
            print("employee_age is:",employee["age"])
            print("employee_gender is:",employee["gender"])
            print("employee_department:",employee["department"])
            print("employee_designation:",employee["designation"])
            print(employee)
            modify = int(input("Enter Field Number : "))
            col_dict = {
                    1: "name",
                    2: "age",
                    3: "gender",
                    4: "department",
                    5: "designation",
                    6: "salary"
                    
                }
            new_value = input("Enter New Value : ")
            employee[col_dict[modify]] = new_value

    if employee_present==False:
          print("the given item id number is incorrect")
def delete_employee():
    print("delete employee")
    if len(employee_master_list)==0:
        print("the master list empty please add few employee menu to display")
        return False
    employee_id=input("enter the employee id to display")
    employee_present=False
    for employee in employee_master_list:
       if employee["employee_id"]==employee_id:
            employee_present=True
            print("employee_name is:",employee["name"])
            print("employee_age is:",employee["age"])
            print("employee_gender is:",employee["gender"])
            print("employee_department:",employee["department"])
            print("employee_designation:",employee["designation"])
            print("employee_salary:",employee["salary"])
            confirm=input("are you sure(yes/no):")
            if confirm.lower()=="yes":
                employee_master_list.remove(employee)
                print("deleted successfully")
    
    if employee_present==False:
           print("the given item id number is incorrect")
def calculate_net_salary():
    if len(employee_master_list)==0:
        print("the master list empty please add few employee menu to display")
        return False
    employee_id=input("enter the employee id to display")
    employee_present=False
    for employee in employee_master_list:
       if employee["employee_id"]==employee_id:
            employee_present=True
            print("employee_name is:",employee["name"])
            print("employee_age is:",employee["age"])
            print("employee_gender is:",employee["gender"])
            print("employee_department:",employee["department"])
            print("employee_designation:",employee["designation"])
            print(employee)
            print("bonus:",bonus)
            print("net salery:",net_salery)
            salary=int(employee["salary"])
            bonus=10
            if(salary>30000):
               net_salary=salary+bonus
            if(salary<30000):
               break
            
    
while True:
    choice=int(input("enter the operation"))
    if choice==1:
        print("you selected to add employee")
        add_employee()
    elif choice==2:
        print("you selected to display employee")
        display_employee()
    elif choice==3:
        print("you selected to search employee")
        search_employee()
    elif choice==4:
        print("you selected to update employee")
        update_employee()
    elif choice==5:
        print("you selected to delete employee")
        delete_employee()
    elif choice==6:
        print("you selected to calculate salary")
        calculate_net_salary()




