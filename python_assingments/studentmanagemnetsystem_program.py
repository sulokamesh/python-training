print("==========================")
print("welcome to theresa school")
print("==========================")
student_master_list= [
    ["STU001","ARJUNKUMAR","15-01-2004","male","CS","o+"],
    ["STU002","PRIYA","15-04-2004","female","ECE","o+"],
    ["STU003","karthick","17-04-2001","male","ECE","B+"],
    ["STU004","divya","17-04-2002","male","EEE","AB+"]
]
while True:
     print("1.add new student")
     print("2.display student data")
     print("3.update student data")
     print("4.delete student data")
     print("5.exit the program")
     choice=int(input("enter your operation....."))
     if choice == 1:
        print("you selectedto add student")
        roll_no=input("enter the student roll number")
        name=input("enter the student name")
        dob=input("enter the student DOB")
        gender=input("enter the student Gender")
        dept=input("enter the student dept")
        blood_group=input("enter the student Blood Group")
        student_list=[roll_no,name,dob,gender,dept,blood_group]
        student_master_list.append(student_list)
        print("student data successfully added")
     elif choice == 2:
         print("you selectedto display student")
         if len(student_master_list)==0:
             print("the master list empty pplease add few student data to display")
             continue
         roll_num=input("enter tge student rool number to display date")
         student_present=False
         for student in student_master_list:
             if student[0]==roll_num:
                 student_present=True
                 print("1.student name is:",student[1])
                 print("2.student DOB is:",student[2])
                 print("3.student Gender is:",student[3])
                 print("4.student dept is:",student[4])
                 print("5.student Blood Group is:",student[5])
         if student_present==False:
                print("the given rool number is incorrect")
     elif choice == 3:
         print("you selectedto update student")
         if len(student_master_list)==0:
             print("the master list empty pplease add few student data to display")
             continue
         roll_num=input("enter tge student rool number to update date")
         student_present=False
         for student in student_master_list:
             if student[0]==roll_num:
                 student_present=True
                 print("1.student name is:",student[1])
                 print("2.student DOB is:",student[2])
                 print("3.student Gender is:",student[3])
                 print("4.student dept is:",student[4])
                 print("5.student Blood Group is:",student[5])
                 modify_choice=int(input("please enter the number which you want to update"))
                 col=['name','DOB', 'Gender', 'Dept','Blood Group']
                 print("you selected to update this:",col[modify_choice-1])
                 new_value=input("enter the new value")
                 student[modify_choice]=new_value
                 print("student data updated")
         if student_present==False:
                print("the given rool number is incorrect")
     elif choice == 4:
         print("you selectedto update student")
         if len(student_master_list)==0:
             print("the master list empty pplease add few student data to display")
             continue
         roll_num=input("enter tge student rool number to update date")
         student_present=False
         student_list_index=0
         for student in student_master_list:
             if student[0]==roll_num:
                 student_present=True
                 print("1.student name is:",student[1])
                 print("2.student DOB is:",student[2])
                 print("3.student Gender is:",student[3])
                 print("4.student dept is:",student[4])
                 print("5.student Blood Group is:",student[5])
                 delete_choice=input("are you sure you want to delete this student(yes/no)")
                 if delete_choice.lower()=="yes":
                     del student_master_list[student_list_index]
                     print("student record sucesfully deleted")
                 else:
                    print("skipping deletion")
             student_list_index+=1
         if student_present==False:
               print("the given roll number is incorrect")
     elif choice == 5:
         print("exiting")
         break
     else:
         print("enter the valid input between 1 to 5")
               
                     
                 
         
                       
                
                
                
                 












                 
         
     
