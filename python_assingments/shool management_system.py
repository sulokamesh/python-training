print("==================")
print("welcome to school management system")
print("===================")
student_fields=("roll n","name","dob","gender","department","blood_group","phone","email","address","percentage")
student_master_list = [
    {
        "roll_no": "STU001",
        "name": "Arjun Kumar",
        "dob": "15-01-2004",
        "gender": "Male",
        "department": "Computer Science",
        "blood_group": "O+",
        "phone": "9876543210",
        "email": "arjun@gmail.com",
        "address": "Chennai",
        "percentage": 92.5
    },
    {
        "roll_no": "STU002",
        "name": "Priya Sharma",
        "dob": "22-03-2005",
        "gender": "Female",
        "department": "Information Technology",
        "blood_group": "A+",
        "phone": "9876543211",
        "email": "priya@gmail.com",
        "address": "Coimbatore",
        "percentage": 88.0
    },
    {
        "roll_no": "STU003",
        "name": "Karthik Raj",
        "dob": "08-07-2004",
        "gender": "Male",
        "department": "Electronics",
        "blood_group": "B+",
        "phone": "9876543212",
        "email": "karthik@gmail.com",
        "address": "Madurai",
        "percentage": 84.5
    },
    {
        "roll_no": "STU004",
        "name": "Divya Lakshmi",
        "dob": "30-11-2005",
        "gender": "Female",
        "department": "Mechanical",
        "blood_group": "AB+",
        "phone": "9876543213",
        "email": "divya@gmail.com",
        "address": "Salem",
        "percentage": 90.2
    },
]    
while True:
    print("1.add student")
    print("2.search student by roll number")
    print("3.update student details")
    print("4.deletestudent record")
    print("5.display one student")
    print("6.display all student")
    print("7.count total students")
    print("8.search student by department")
    print("9.find topper")
    print("10.sort students by name")
    print("11.sort students by percentage")
    print("12.exit")
    choice=int(input("enter your choice:"))
    if choice == 1:

        print("\nAdd Student")

        roll_no = input("Enter Roll Number : ")

        student_found = False

        for student in student_master_list:
            if student["roll_no"] == roll_no:
                student_found = True
                break

        if student_found:
            print("Roll Number already exists.")
            continue

        name = input("Enter Name : ")
        dob = input("Enter DOB : ")
        gender = input("Enter Gender : ")
        department = input("Enter Department : ")
        blood_group = input("Enter Blood Group : ")
        phone = input("Enter Phone Number : ")
        email = input("Enter Email : ")
        address = input("Enter Address : ")
        percentage = float(input("Enter Percentage : "))

        temp = {}

        temp["roll_no"] = roll_no
        temp["name"] = name
        temp["dob"] = dob
        temp["gender"] = gender
        temp["department"] = department
        temp["blood_group"] = blood_group
        temp["phone"] = phone
        temp["email"] = email
        temp["address"] = address
        temp["percentage"] = percentage

        student_master_list.append(temp)

        print("Student Added Successfully.")

    elif choice == 2:

        print("\nSearch Student")

        if len(student_master_list) == 0:
            print("No Student Records Found.")
            continue

        roll_no = input("Enter Roll Number : ")

        student_found = False

        for student in student_master_list:

            if student["roll_no"] == roll_no:

                student_found = True

                print("\nStudent Details")
                print("Roll No      :", student["roll_no"])
                print("Name         :", student["name"])
                print("DOB          :", student["dob"])
                print("Gender       :", student["gender"])
                print("Department   :", student["department"])
                print("Blood Group  :", student["blood_group"])
                print("Phone        :", student["phone"])
                print("Email        :", student["email"])
                print("Address      :", student["address"])
                print("Percentage   :", student["percentage"])

        if student_found == False:
            print("Student Not Found.")

    elif choice == 3:

        print("\nUpdate Student")

        if len(student_master_list) == 0:
            print("No Student Records Found.")
            continue

        roll_no = input("Enter Roll Number : ")

        student_found = False

        for student in student_master_list:

            if student["roll_no"] == roll_no:

                student_found = True

                print("1.Name")
                print("2.DOB")
                print("3.Gender")
                print("4.Department")
                print("5.Blood Group")
                print("6.Phone")
                print("7.Email")
                print("8.Address")
                print("9.Percentage")

                modify = int(input("Enter Field Number : "))
                col_dict = {
                    1: "name",
                    2: "dob",
                    3: "gender",
                    4: "department",
                    5: "blood_group",
                    6: "phone",
                    7: "email",
                    8: "address",
                    9: "percentage"
                }

                new_value = input("Enter New Value : ")

                if modify == 9:
                    new_value = float(new_value)

                student[col_dict[modify]] = new_value

                print("Student Updated Successfully.")

        if student_found == False:
            print("Student Not Found.")

    elif choice == 4:

        print("\nDelete Student")

        if len(student_master_list) == 0:
            print("No Student Records Found.")
            continue

        roll_no = input("Enter Roll Number : ")

        student_found = False
        index = 0

        for student in student_master_list:

            if student["roll_no"] == roll_no:

                student_found = True

                confirm = input("Are you sure (yes/no) : ")

                if confirm.lower() == "yes":
                    del student_master_list[index]
                    print("Student Deleted Successfully.")
                else:
                    print("Deletion Cancelled.")

                break

            index += 1

        if student_found == False:
            print("Student Not Found.")

    elif choice == 5:

        print("\nDisplay One Student")

        if len(student_master_list) == 0:
            print("No Student Records Found.")
            continue

        roll_no = input("Enter Roll Number : ")

        student_found = False

        for student in student_master_list:

            if student["roll_no"] == roll_no:

                student_found = True

                print("\n========== Student Details ==========")
                print("Roll No      :", student["roll_no"])
                print("Name         :", student["name"])
                print("DOB          :", student["dob"])
                print("Gender       :", student["gender"])
                print("Department   :", student["department"])
                print("Blood Group  :", student["blood_group"])
                print("Phone        :", student["phone"])
                print("Email        :", student["email"])
                print("Address      :", student["address"])
                print("Percentage   :", student["percentage"])

        if student_found == False:
            print("Student Not Found.")

    elif choice == 6:

        print("\nDisplay All Students")

        if len(student_master_list) == 0:
            print("No Student Records Found.")
            continue

        for student in student_master_list:

            print("\n==============================")
            print("Roll No      :", student["roll_no"])
            print("Name         :", student["name"])
            print("DOB          :", student["dob"])
            print("Gender       :", student["gender"])
            print("Department   :", student["department"])
            print("Blood Group  :", student["blood_group"])
            print("Phone        :", student["phone"])
            print("Email        :", student["email"])
            print("Address      :", student["address"])
            print("Percentage   :", student["percentage"])
    elif choice == 7:

        print("\nTotal Students")

        print("Total Number of Students :", len(student_master_list))

    elif choice == 8:

        print("\nSearch Students by Department")

        if len(student_master_list) == 0:
            print("No Student Records Found.")
            continue

        dept = input("Enter Department : ")

        student_found = False

        for student in student_master_list:

            if student["department"].lower() == dept.lower():

                student_found = True

                print("\n--------------------------------")
                print("Roll No    :", student["roll_no"])
                print("Name       :", student["name"])
                print("Department :", student["department"])
                print("Percentage :", student["percentage"])

        if student_found == False:
            print("No Students Found in this Department.")

    elif choice == 9:

        print("\nFind Topper")

        if len(student_master_list) == 0:
            print("No Student Records Found.")
            continue

        topper = student_master_list[0]

        for student in student_master_list:

            if student["percentage"] > topper["percentage"]:
                topper = student

        print("\n===== TOPPER DETAILS =====")
        print("Roll No      :", topper["roll_no"])
        print("Name         :", topper["name"])
        print("Department   :", topper["department"])
        print("Percentage   :", topper["percentage"])

    elif choice == 10:

        print("\nSort Students by Name")

        if len(student_master_list) == 0:
            print("No Student Records Found.")
            continue

        student_master_list.sort(key=lambda student: student["name"])

        print("Students Sorted by Name Successfully.")

        for student in student_master_list:

            print("--------------------------------")
            print("Roll No :", student["roll_no"])
            print("Name    :", student["name"])
            print("Dept    :", student["department"])

    elif choice == 11:

        print("\nSort Students by Percentage")

        if len(student_master_list) == 0:
            print("No Student Records Found.")
            continue

        student_master_list.sort(
            key=lambda student: student["percentage"],
            reverse=True
        )

        print("Students Sorted by Percentage Successfully.")

        for student in student_master_list:

            print("--------------------------------")
            print("Roll No    :", student["roll_no"])
            print("Name       :", student["name"])
            print("Percentage :", student["percentage"])

    elif choice == 12:

        print("Thank You...")
        break

    else:

        print("Please Enter a Valid Choice (1 to 12)")













        
                    
                    
                
