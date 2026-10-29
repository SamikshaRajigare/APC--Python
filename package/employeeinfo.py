class Employee:
    def __init__(self, name, emp_id, department, designation, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.designation = designation
        self.salary = salary

    def display(self):
        print("\n Employee Information")
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Department:", self.department)
        print("Designation:", self.designation)
        print("Salary:", self.salary)

name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
department = input("Enter Department: ")
designation = input("Enter Designation: ")
salary = input("Enter Salary: ")

employee = Employee(
    name, emp_id, department, designation, salary
)
employee.display()
