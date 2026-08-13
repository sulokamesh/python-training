class Student:

    def __init__(self, roll_no, name, age, marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Roll Number :", self.roll_no)
        print("Name        :", self.name)
        print("Age         :", self.age)
        print("Marks       :", self.marks)
        print("Grade       :", self.calculate_grade())

    def calculate_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"


class Faculty:

    def __init__(self, emp_id, name, subject, salary):
        self.emp_id = emp_id
        self.name = name
        self.subject = subject
        self.salary = salary

    def display(self):
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Subject     :", self.subject)
        print("Salary      :", self.salary)


class Department:

    def __init__(self, name, hod):
        self.name = name
        self.hod = hod
        self.students = []
        self.faculties = []

    def add_student(self, student):
        self.students.append(student)

    def add_faculty(self, faculty):
        self.faculties.append(faculty)

    def display_students(self):
        for student in self.students:
            student.display()
            print("--------------------")


class College:

    def __init__(self, name, code, address):
        self.name = name
        self.code = code
        self.address = address
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def display_departments(self):
        for department in self.departments:
            print("Department :", department.name)
            print("HOD        :", department.hod)
            print("--------------------")


# College Object

college = College(
    "ABC Engineering College",
    "C101",
    "Chennai"
)



while True:

    print("========== SMART COLLEGE ERP ==========")
    print("1. Add Department")
    print("2. Add Student")
    print("3. Add Faculty")
    print("4. Search Student")
    print("5. Search Faculty")
    print("6. Display Department")
    print("7. Display All Students")
    print("8. Display All Faculties")
    print("9. Highest Mark Student")
    print("10. Exit")

    choice = input("Enter your choice: ")


    # 1. Add Department

    if choice == "1":

        name = input("Enter department name: ")
        hod = input("Enter HOD name: ")

        department = Department(name, hod)

        college.add_department(department)

        print("Department added successfully")


    # 2. Add Student

    elif choice == "2":

        roll_no = input("Enter roll number: ")
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))

        student = Student(roll_no, name, age, marks)

        department.add_student(student)

        print("Student added successfully")


    # 3. Add Faculty

    elif choice == "3":

        emp_id = input("Enter employee ID: ")
        name = input("Enter faculty name: ")
        subject = input("Enter subject: ")
        salary = float(input("Enter salary: "))

        faculty = Faculty(emp_id, name, subject, salary)

        department.add_faculty(faculty)

        print("Faculty added successfully")


    # 4. Search Student

    elif choice == "4":

        roll_no = input("Enter roll number: ")

        found = False

        for department in college.departments:

            for student in department.students:

                if student.roll_no == roll_no:

                    student.display()

                    print("Department :", department.name)

                    found = True

        if not found:
            print("Student not found")


    # 5. Search Faculty

    elif choice == "5":

        emp_id = input("Enter employee ID: ")

        found = False

        for department in college.departments:

            for faculty in department.faculties:

                if faculty.emp_id == emp_id:

                    faculty.display()

                    print("Department :", department.name)

                    found = True

        if not found:
            print("Faculty not found")


    # 6. Display Department

    elif choice == "6":

        college.display_departments()


    # 7. Display All Students

    elif choice == "7":

        for department in college.departments:

            print("\nDepartment :", department.name)

            department.display_students()


    # 8. Display All Faculties

    elif choice == "8":

        for department in college.departments:

            print("Department :", department.name)

            for faculty in department.faculties:

                faculty.display()



    # 9. Highest Mark Student

    elif choice == "9":

        highest_student = None
        highest_department = None

        for department in college.departments:

            for student in department.students:

                if highest_student is None:

                    highest_student = student
                    highest_department = department

                elif student.marks > highest_student.marks:

                    highest_student = student
                    highest_department = department


        if highest_student is None:

            print("No students available")

        else:

            print("===== HIGHEST MARK STUDENT =====")

            highest_student.display()

            print("Department :", highest_department.name)


    # 10. Exit

    elif choice == "10":

        print("Thank you for using Smart College ERP System")

        break


    else:

        print("Invalid choice")
,   
