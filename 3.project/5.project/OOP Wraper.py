class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def display(self):
        print("\nPerson Details:")
        print("Name : ", self.name)
        print("Age : ", self.age)


class Employee(Person):
    def __init__(self, name="", age=0, emp_id="", salary=0):
        super().__init__(name, age)
        self.emp_id = emp_id       # removed __ (private)
        self.salary = salary

    def display(self):
        print("\nEmployee Details : ")
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Employee ID : ", self.emp_id)
        print("Salary : $", self.salary)


class Manager(Employee):
    def __init__(self, name="", age=0, emp_id="", salary=0, department=""):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department : ", self.department)


class Developer(Employee):
    def __init__(self, name="", age=0, emp_id="", salary=0, language=""):
        super().__init__(name, age, emp_id, salary)
        self.language = language

    def display(self):
        super().display()
        print("Programming Language : ", self.language)


def main():
    person = None
    employee = None
    manager = None

    while True:
        print("\n===== Python OOP Project: Employee Management System =====")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Exit")

        choice = input("Enter your choice : ")

        if choice == "1":
            name = input("Enter Name : ")
            age = int(input("Enter Age : "))
            person = Person(name, age)
            print("\nPerson created successfully!")

        elif choice == "2":
            name = input("Enter Name : ")
            age = int(input("Enter Age : "))
            emp_id = input("Enter Employee ID : ")
            salary = float(input("Enter Salary : "))
            employee = Employee(name, age, emp_id, salary)
            print("\nEmployee created successfully!")

        elif choice == "3":
            name = input("Enter Name : ")
            age = int(input("Enter Age : "))
            emp_id = input("Enter Employee ID : ")
            salary = float(input("Enter Salary : "))
            dept = input("Enter Department : ")
            manager = Manager(name, age, emp_id, salary, dept)
            print("\nManager created successfully!")

        elif choice == "4":
            print("\n1. Person\n2. Employee\n3. Manager")
            sub = input("Choose details to show : ")

            if sub == "1" and person:
                person.display()
            elif sub == "2" and employee:
                employee.display()
            elif sub == "3" and manager:
                manager.display()
            else:
                print("No data found!")

        elif choice == "5":
            print("\nExiting the system. Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")


# Run Program
main()
