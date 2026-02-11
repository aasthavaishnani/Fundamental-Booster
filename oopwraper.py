class Employee : 
    def __init__(self, empid, name, age, salary):
        self.__empid = empid
        self.name = name
        self.age = age
        self.__salary = salary

    def __del__(self):
        print(f"Employee {self.name} with ID {self.__empid} is being deleted successfully.")

    def get_empid(self):
        return self.__empid
    
    def set_empid(self, empid):
        self.__empid = empid

    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        self.__salary = salary
   
    def display_info(self):
        print(f"Employee ID: {self.__empid}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.__salary}")

class Manager(Employee):
    def __init__(self, empid, name, age, salary, department):
        super().__init__(empid, name, age, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

class Developer(Employee):
    def __init__(self, empid, name, age, salary, programming_language):
        super().__init__(empid, name, age, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

employee = []
empid = 1

while True:
    print("\n--- EMPLOYEE MANAGEMENT SYSTEM ---")
    print("1. Create Employee")
    print("2. Create Manager")
    print("3. Create Developer")
    print("4. Display Employee Details")
    print("5. Update Salary")
    print("6. Check Position (Employee/Manager/Developer)")
    print("7. Exit")

    ch = int(input("Enter your choice: "))
    print()

    if ch == 1:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))

        employee.append(Employee(empid, name, age, salary))
        empid += 1
        print("Employee added successfully :)")
        print()

    if ch == 2:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")

        employee.append(Manager(empid, name, age, salary, department))
        empid += 1
        print("Manager added successfully :)")
        print()

    elif ch == 3:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))
        programming_language = input("Enter Programming Language: ")

        employee.append(Developer(empid, name, age, salary, programming_language))
        empid += 1
        print("Developer added successfully :)")
        print()

    elif ch == 4:
        if not employee:
            print("No employees to display.\n")
        else:
            print("1. Display Employees")
            print("2. Display Managers")
            print("3. Display Developers")
            print("4. Display All")

            chh = int(input("Enter your choice: "))
            print()

            if chh == 1:
                print("1. Display Employees by ID: ")
                print("2. Display all employees: ")

                sub_ch = int(input("Enter your choice: "))
                print()

                if sub_ch == 1:
                    emp_id = int(input("Enter Employee ID: "))
                    print()
                    found = False
                    for emp in employee:
                        if isinstance(emp, Employee) and emp.get_empid() == emp_id:
                            emp.display_info()
                            print()
                            found = True
                            break
                    if not found:
                        print("Employee not found.")
                        print()

                elif sub_ch == 2:
                    for emp in employee:
                        emp.display_info()
                        print()

            elif chh == 2:
                print("1. Display Manager by ID: ")
                print("2. Display all Managers: ")

                sub_ch = int(input("Enter your choice: "))
                print()

                if sub_ch == 1:
                    emp_id = int(input("Enter Manager ID: "))
                    print()
                    found = False
                    for emp in employee:
                        if isinstance(emp, Manager) and emp.get_empid() == emp_id:
                            emp.display_info()
                            print()
                            found = True
                            break
                    if not found:
                        print("Manager not found.")
                        print()
                        
                elif sub_ch == 2:
                    for emp in employee:
                        if isinstance(emp, Manager):
                            emp.display_info()
                            print()

            elif chh == 3:
                print("1. Display Developer by ID: ")
                print("2. Display all Developers: ")

                sub_ch = int(input("Enter your choice: "))
                print()

                if sub_ch == 1:
                    emp_id = int(input("Enter Developer ID: "))
                    print()
                    found = False
                    for emp in employee:
                        if isinstance(emp, Developer) and emp.get_empid() == emp_id:
                            emp.display_info()
                            print()
                            found = True
                            break
                    if not found:
                        print("Developer not found.")
                        print()
                        
                elif sub_ch == 2:
                    for emp in employee:
                        if isinstance(emp, Developer):
                            emp.display_info()
                            print()

            elif chh == 4:
                for emp in employee:
                    emp.display_info()
                    print()

    elif ch == 5:
        if not employee:
            print("No employees to display.\n")
        else:
            empid = int(input("Enter Employee ID to update salary: "))
            new_salary = float(input("Enter new salary: "))
            print()
            found = False

            for emp in employee:
                if emp.get_empid() == empid:
                    emp.set_salary(new_salary)
                    print("Salary updated successfully :)\n")
                    found = True
                    break
            
            if not found:
                print("Employee not found.")
                print()

    elif ch == 6:
        if not employee:
            print("No employees to display.\n")
        else:
            empid = int(input("Enter Employee ID to check subclass: "))
            print()
            found = False

            for emp in employee:
                if emp.get_empid() == empid:
                    if isinstance(emp, Manager):
                        print("This employee is a Manager.")
                    elif isinstance(emp, Developer):
                        print("This employee is a Developer.")
                    else:
                        print("This employee is an Employee.")
                    found = True
                    break
            
            if not found:
                print("Employee not found.")
                print()

    elif ch == 7:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.\n")