class College:
    def __init__(self, name, code, address, departments=[]):
        self.name = name
        self.code = code
        self.address = address
        self.departments = departments

    def add_departments(self, name, code, hod):
        self.deptObj = Department(name, code, hod)
        self.departments.append(self.deptObj)
        print("Department added successfully")


    def display_departments(self, code):
        for department in self.departments:
            if department.code == code:
                dept_name = department.name
                print("Department Name is : ", dept_name)
                print("Department HOD is : ", department.hod)
                validation = input("do you want to enter into this department (yes/no)")
                if validation.lower() == "yes":
                    print(
                        "Welcome to {dept_name} Department".format(
                            dept_name=dept_name
                        )
                    )
                    print("===========================================")
                    while True:
                        print("1.Add Student...")
                        print("2.Display Student..")
                        print("3.Add Faculty..")
                        print("4.Display Faculty...")
                        print("5. Exit")
                        choice = int(input("Enter your choice"))
                        if choice == 1:
                            print("Enter the below student details..")
                            roll_no = input("Enter the rollno..")
                            name = input("Enter the name")
                            age = input("Enter the age")
                            marks = input("Enter the marks")
                            department.add_student(roll_no, name, age, marks)
                            print("Student added successfully...")
                        elif choice == 2:
                            roll_no = input("enter the roll_no to search")
                            department.display_students(roll_no)
                        else:
                            print("exising..")
                            break


class Department(College):
    def __init__(self, name, code, hod, students=[], faculties=[]):
        self.name = name
        self.code = code
        self.hod = hod
        self.students = students
        self.faculties = faculties

    def add_student(self, roll_no, name, age, marks):
        self.stuObj = Student(roll_no, name, age, marks)
        self.students.append(self.stuObj)
        print("Student added succesfully...")

    def add_faculties(self):
        self.facultObj = Faculty(emp_id, name, subject, salary)
        self.faculties.append(self.facultObj)
        print("Faculty added successfully.....")

    def display_students(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print("Student Name is : ", student.name)
                print("Student  Age is : ", student.age)
                print("Student Marks is : ", student.marks)

    def display_faculty(self, emp_id):
        for faculty in self.faculties:
            if faculty.emp_id == emp_id:
                print("Faculty Name is : ", faculty.name)
                print("Faculty Subject is : ", faculty.subject)
                print("Faculty Salary is : ", faculty.salary)


class Student:
    def __init__(self, roll_no, name, age, marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.marks = marks

    # def display(self):
    #     pass
    # def calculate_grade(self):
    #     pass


class Faculty:
    def __init__(self, emp_id, name, subject, salary):
        self.emp_id = emp_id
        self.name = name
        self.subject = subject
        self.salary = salary


clgObj = College("Anna University", 102, "Chennai")
print("Welcome to College ERP system....")
print("================================")
while True:
    print("1. Add Department ")
    print("2. Display Department")
    print("3. Exit")
    dept_choice = int(input("Enter your choice.."))
    if dept_choice == 1:
        print("you are selected to add department")
        dept_name = input("Enter the dept name...")
        dept_code = input("Enter the department code")
        dept_hod = input("Enter the HOD Name")
        clgObj.add_departments(dept_name, dept_code, dept_hod)
    elif dept_choice == 2:
        print("you are selected to display department...")
        dept_code = input("Enter the dept code to fetch...")
        clgObj.display_departments(dept_code)

    elif dept_choice == 3:
        print("Exiting.....")
        print("thanks for using......")
        break
    else:
        print("please select the choice between 1 and 3")
         