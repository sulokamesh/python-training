print("==========================")
print("Welcome to Therasa School")
print("==========================")

student_fields = ("roll_num", "name", "dob", "gender", "dept", "blood_group")

student_master_list = [
    {
        "roll_no": "STU001",
        "name": "Arjun Kumar",
        "dob": "15-01-2004",
        "gender": "Male",
        "department": "Computer Science",
        "blood_group": "O+"
    },
    {
        "roll_no": "STU002",
        "name": "Priya Sharma",
        "dob": "22-03-2005",
        "gender": "Female",
        "department": "Information Technology",
        "blood_group": "A+"
    },
    {
        "roll_no": "STU003",
        "name": "Karthik Raj",
        "dob": "08-07-2004",
        "gender": "Male",
        "department": "Electronics",
        "blood_group": "B+"
    },
    {
        "roll_no": "STU004",
        "name": "Divya Lakshmi",
        "dob": "30-11-2005",
        "gender": "Female",
        "department": "Mechanical",
        "blood_group": "AB+"
    },
    {
        "roll_no": "STU005",
        "name": "Rahul Verma",
        "dob": "12-05-2004",
        "gender": "Male",
        "department": "Civil",
        "blood_group": "O-"
    },
    {
        "roll_no": "STU006",
        "name": "Sneha Reddy",
        "dob": "18-09-2005",
        "gender": "Female",
        "department": "Computer Science",
        "blood_group": "A-"
    },
    {
        "roll_no": "STU007",
        "name": "Vikram Singh",
        "dob": "25-12-2004",
        "gender": "Male",
        "department": "Electrical",
        "blood_group": "B-"
    },
    {
        "roll_no": "STU008",
        "name": "Meena Krishnan",
        "dob": "14-02-2005",
        "gender": "Female",
        "department": "Information Technology",
        "blood_group": "O+"
    },
    {
        "roll_no": "STU009",
        "name": "Suresh Babu",
        "dob": "09-08-2004",
        "gender": "Male",
        "department": "Artificial Intelligence",
        "blood_group": "AB-"
    },
    {
        "roll_no": "STU010",
        "name": "Ananya Nair",
        "dob": "27-06-2005",
        "gender": "Female",
        "department": "Data Science",
        "blood_group": "A+"
    }
]

while True:

    print("1.Add New Student")
    print("2.Display Student Data")
    print("3.Update Student Data")
    print("4.Delete Student Data")
    print("5.Exit this program")

    choice = int(input("Enter your operation....."))

    if choice == 1:
        print("You selected to add student")

        roll_no = input("Enter the student roll number")
        name = input("Enter the student Name")
        dob = input("Enter the student DOB")
        gender = input("Enter the student Gender")
        dept = input("Enter the student Dept")
        blood_group = input("Enter the student Blood Group")

        temp = {}

        temp["roll_no"] = roll_no
        temp["name"] = name
        temp["dob"] = dob
        temp["gender"] = gender
        temp["department"] = dept
        temp["blood_group"] = blood_group

        student_master_list.append(temp)

        print("Student data successfully added")

    elif choice == 2:
        print("You selected to display student")

        if len(student_master_list) == 0:
            print("The master list empty please add few student data to display")
            continue

        roll_num = input("Enter the student roll number to display data")

        student_present = False

        for student in student_master_list:

            if student["roll_no"] == roll_num:
                student_present = True

                print("Student Name is : ", student["name"])
                print("Student DOB is : ", student["dob"])
                print("Student Gender is : ", student["gender"])
                print("Student Dept is : ", student["department"])
                print("Student Blood Group is : ", student["blood_group"])

        if student_present == False:
            print("the given roll number is incorrect")

    elif choice == 3:
        print("You selected to update student")

        if len(student_master_list) == 0:
            print("The master list empty please add few student data to display")
            continue

        roll_num = input("Enter the student roll number to update")

        student_present = False

        for student in student_master_list:

            if student["roll_no"] == roll_num:
                student_present = True

                print("Student Name is : ", student["name"])
                print("Student DOB is : ", student["dob"])
                print("Student Gender is : ", student["gender"])
                print("Student Dept is : ", student["department"])
                print("Student Blood Group is : ", student["blood_group"])

                print("1.Name")
                print("2.DOB")
                print("3.Gender")
                print("4.Department")
                print("5.Blood Group")

                modify_choice = int(
                    input("please enter the number which you want to update")
                )

                col_dict = {
                    1: 'name',
                    2: 'dob',
                    3: 'gender',
                    4: 'department',
                    5: 'blood_group'
                }

                print(
                    "you selected to update this : ",
                    col_dict[modify_choice]
                )

                new_value = input("Enter the new value")

                student[col_dict[modify_choice]] = new_value

                print("Student data updated")

        if student_present == False:
            print("the given roll number is incorrect")

    elif choice == 4:
        print("You selected to delete student")

        if len(student_master_list) == 0:
            print("The master list empty please add few student data to display")
            continue

        roll_num = input("Enter the student roll number to display data")

        student_present = False
        student_list_index = 0

        for student in student_master_list:

            if student["roll_no"] == roll_num:
                student_present = True

                print("Student Name is : ", student["name"])
                print("Student DOB is : ", student["dob"])
                print("Student Gender is : ", student["gender"])
                print("Student Dept is : ", student["department"])
                print("Student Blood Group is : ", student["blood_group"])

                delete_choice = input(
                    "Are you sure you want to delete this student (yes/no)"
                )

                if delete_choice.lower() == "yes":
                    del student_master_list[student_list_index]
                    print("Student record successfully deleted...")
                else:
                    print("Skipping deletion")

            student_list_index += 1

        if student_present == False:
            print("the given roll number is incorrect")

    elif choice == 5:
        print("Exiting")
        break

    else:
        print("Enter the valid input between 1 to 5")