class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person constructor called")
    def display_person_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
    def __del__(self):
        print("Person destructor called")
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary
        print("Employee constructor called")
    def display_employee_info(self):
        self.display_person_info()
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
    def __del__(self):
        print("Employee destructor called")
class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department, team_size):
        super().__init__(name, age, employee_id, salary)
        self.department = department
        self.team_size = team_size
        print("Manager constructor called")
    def display_manager_info(self):
        print("\n Manager Information")
        self.display_employee_info()
        print("Department:", self.department)
        print("Team Size:", self.team_size)
    def __del__(self):
        print("Manager destructor called")
manager1 = Manager("Rahul", 35, "MGR101", 75000, "IT", 10)
manager1.display_manager_info()
del manager1