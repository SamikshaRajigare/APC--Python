import csv
n = int(input("Enter number of students: "))
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["RollNo", "Name", "Marks"])
    for i in range(n):
        print("\nEnter details of student", i + 1)
        roll_no = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        writer.writerow([roll_no, name, marks])
def read_students():
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)
        return list(reader)
def display_all():
    students = read_students()
    print("\nAll Student Records:")
    for student in students:
        print(student["RollNo"], student["Name"], student["Marks"])
def highest_marks():
    students = read_students()
    student = max(students, key=lambda x: float(x["Marks"]))
    print("\nStudent with Highest Marks:")
    print("Roll No:", student["RollNo"])
    print("Name:", student["Name"])
    print("Marks:", student["Marks"])
def average_marks():
    students = read_students()
    total = sum(float(student["Marks"]) for student in students)
    average = total / len(students)
    print("\nAverage Marks:", average)
def above_marks(marks_limit):
    students = read_students()
    print("\nStudents who scored more than", marks_limit, ":")
    for student in students:
        if float(student["Marks"]) > marks_limit:
            print(student["RollNo"], student["Name"], student["Marks"])
display_all()
highest_marks()
average_marks()
marks_limit = float(input("\nEnter marks limit: "))
above_marks(marks_limit)
