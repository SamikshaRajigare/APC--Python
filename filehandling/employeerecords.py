import csv
n = int(input("Enter number of employees: "))
with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["EmployeeID", "Name", "Department", "Salary"])
    for i in range(n):
        print("\nEnter details of employee", i + 1)
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))
        writer.writerow([emp_id, name, department, salary])
def read_employees():
    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)
        return list(reader)
def display_all():
    employees = read_employees()
    print("\nAll Employees:")
    for emp in employees:
        print(emp["EmployeeID"], emp["Name"],
              emp["Department"], emp["Salary"])
def highest_paid():
    employees = read_employees()
    employee = max(employees, key=lambda x: float(x["Salary"]))
    print("\nHighest-Paid Employee:")
    print("Employee ID:", employee["EmployeeID"])
    print("Name:", employee["Name"])
    print("Department:", employee["Department"])
    print("Salary:", employee["Salary"])
def average_salary():
    employees = read_employees()
    total = sum(float(emp["Salary"]) for emp in employees)
    average = total / len(employees)
    print("\nAverage Salary:", average)
def above_salary(amount):
    employees = read_employees()
    print("\nEmployees earning above", amount, ":")
    for emp in employees:
        if float(emp["Salary"]) > amount:
            print(emp["EmployeeID"], emp["Name"],
                  emp["Department"], emp["Salary"])
display_all()
highest_paid()
average_salary()

salary_limit = float(input("\nEnter salary limit: "))
above_salary(salary_limit)
