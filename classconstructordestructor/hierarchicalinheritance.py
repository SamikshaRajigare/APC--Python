class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor called")
    def display_person(self):
        print("Name:", self.name)
    def __del__(self):
        print("Person destructor called")
class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
        print("Employee constructor called")
    def display_employee(self):
        self.display_person()
        print("Salary:", self.salary)
    def __del__(self):
        print("Employee destructor called")
class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course
        print("Student constructor called")
    def display_student(self):
        self.display_person()
        print("Course:", self.course)
    def __del__(self):
        print("Student destructor called")
emp = Employee("Rahul", 50000)
print("\nEmployee Details:")
emp.display_employee()
student = Student("Priya", "Python")
print("\nStudent Details:")
student.display_student()
del emp
del student