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
        print("\n Employee Information")
        self.display_person_info()
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
    def __del__(self):
        print("Employee destructor called")
employee1 = Employee("Rahul", 25, "EMP101", 50000)
employee1.display_employee_info()
del employee1

