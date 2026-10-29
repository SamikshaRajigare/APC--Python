import csv
n = int(input("Enter number of students: "))
with open("attendance.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["RollNo", "Name", "TotalClasses", "PresentClasses"])
    for i in range(n):
        print("\nEnter details of student", i + 1)
        roll_no = input("Enter Roll No: ")
        name = input("Enter Name: ")
        total_classes = int(input("Enter Total Classes: "))
        present_classes = int(input("Enter Present Classes: "))
        writer.writerow([
            roll_no,
            name,
            total_classes,
            present_classes
        ])
def read_attendance():
    with open("attendance.csv", "r") as file:
        reader = csv.DictReader(file)
        return list(reader)
def attendance_percentage():
    students = read_attendance()
    print("\nAttendance Percentage:")
    for student in students:
        total = int(student["TotalClasses"])
        present = int(student["PresentClasses"])
        percentage = (present / total) * 100
        print(
            student["RollNo"],
            student["Name"],
            ":", round(percentage, 2), "%"
        )
def below_75():
    students = read_attendance()
    print("\nStudents having attendance below 75%:")
    for student in students:
        total = int(student["TotalClasses"])
        present = int(student["PresentClasses"])
        percentage = (present / total) * 100
        if percentage < 75:
            print(
                student["RollNo"],
                student["Name"],
                ":", round(percentage, 2), "%"
            )
attendance_percentage()
below_75()
