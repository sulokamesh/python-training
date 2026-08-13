patient_master_list = [
    {"patient_id": "P001", "name": "Ravi Kumar", "age": 35, "gender": "Male", "disease": "Fever", "doctor": "Dr. Priya","phone": "9876543210"},
    {"patient_id": "P002", "name": "Anitha S", "age": 28, "gender": "Female", "disease": "Dengue", "doctor": "Dr. Rajesh","phone": "9123456780"},
    {"patient_id": "P003", "name": "Karthik M", "age": 42, "gender": "Male", "disease": "Diabetes", "doctor": "Dr. Meena", "phone": "9345678901"},
    {"patient_id": "P004", "name": "Divya R", "age": 19, "gender": "Female", "disease": "Typhoid", "doctor": "Dr. Arun","phone": "9567890123"},
    {"patient_id": "P005", "name": "Suresh B", "age": 50, "gender": "Male", "disease": "Heart Disease", "doctor": "Dr. Kumar","phone": "9789012345"}
]
patient_list=[]
def add_patient():
    patient_id=input("enter the patient_id")
    name=input("enter the patient_name")
    age=int(input("enter the age"))
    gender=input("enter the gender ")
    disease=input("enter the disease")
    doctor=input("enter the doctor")
    phone=input("enter the phone ")
    temp={}
    temp["patient_id"]=patient_id
    temp["patient_name"]=name
    temp["age"]=age
    temp["gender"]=gender
    temp["disease"]=disease
    temp["doctor"]=doctor
    temp["phone"]=phone

    print("patient successfully added")
    patient_master_list.append(temp)
def display_patient():
    if len(patient_master_list)==0:
        print("the master list empty please add few patient menu to display")
        return False
    try:
       patient_id=int(input("enter the patient id to display"))
       patient_present=False
       for patient in patient_master_list:
          if patient["patient_id"]==patient_id:
               patient_present=True
               print("patient_name is:",patient["name"])
               print("patient_age is:",patient["age"])
               print("patient_gender is:",patient["gender"])
               print("patient_disease:",patient["disease"])
               print("patient_doctor:",patient["doctor"])
               print("patient_phone:",patient["phone"])
    
       if patient_present==False:
           print("the given patient id is incorrect")
    Error:
        print("not found")
def search_patient():
    if len(patient_master_list)==0:
        print("the master list empty please add few patient to search")
        return False                                                                                                         
    patient_id=input("enter the patient id to search")
    patient_present=False
    for patient in patient_master_list:
       if patient["patient_id"]==patient_id:
            patient_present=True
            print("patient_name is:",patient["name"])
            print("patient_age is:",patient["age"])
            print("patient_gender is:",patient["gender"])
            print("patient_disease:",patient["disease"])
            print("patient_doctor:",patient["doctor"])
            print("patient_phone:",patient["phone"])
    if patient_present==False:
          print("the given patient id number is incorrect")
def update_patient():
    if len(patient_master_list)==0:
        print("the master list is empty please add some patient details to update")
        return False
    patient_id=input("enter the patient id ")
    patient_present=False
    for patient in patient_master_list:
        if patient["patient_id"]==patient_id:
            patient_present=True
            print("1.patient_name is:",patient["name"])
            print("2.patient_age is:",patient["age"])
            print("3.patient_gender is:",patient["gender"])
            print("4.patient_disease:",patient["disease"])
            print("patient_doctor:",patient["doctor"])
            print("patient_phone:",patient["phone"])
            modify = int(input("Enter Field Number : "))
            col_dict = {
                    1: "name",
                    2: "age",
                    3: "disease"
                }
            new_value = input("Enter New Value : ")
            patient[col_dict[modify]] = new_value

    if patient_present==False:
          print("the given item id number is incorrect")
def delete_patient():
    print("delete patient")
    if len(patient_master_list)==0:
        print("the master list is empty please add some patient details to delete")
        return False
    patient_id=input("enter the patient id ")
    patient_present=False
    for patient in patient_master_list:
        if patient["patient_id"]==patient_id:
            patient_present=True
            print("1.patient_name is:",patient["name"])
            print("2.patient_age is:",patient["age"])
            print("3.patient_gender is:",patient["gender"])
            print("4.patient_disease:",patient["disease"])
            print("5.patient_doctor:",patient["doctor"])
            print("6.patient_phone:",patient["phone"])
            confirm=input("are you sure(yes/no):")
            if confirm.lower()=="yes":
               patient_master_list.remove(patient)
               print("deleted successfully")
    
    if patient_present==False:
           print("the given item id number is incorrect")


    


    

while True:
    choice=int(input("enter the operation"))
    if choice==1:
        print("you selected to add patient")
        add_patient()
    elif choice==2:
        print("you selected to display patient")
        display_patient()
    elif choice==3:
        print("you selected to search patient")
        search_patient()
    elif choice==4:
        print("you selected to update patient")
        update_patient()
    elif choice==5:
        print("you selected to delete patient")
        delete_patient()

    
    elif choice==8:
        print("exit")
        
    else:
        print("enter the valid input")
        break
        

        










        












        
