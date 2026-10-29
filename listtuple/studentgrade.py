student_names = []
student_grades = []
def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    student_names.append(name)
    student_grades.append(grade)
    print("Student added successfully")
def update_grade():
    name = input("Enter student name to update grade: ")

    if name in student_names:
        index = student_names.index(name)
        new_grade = float(input("Enter new grade: "))

        student_grades[index] = new_grade
        print("Grade updated successfully!")
    else:
        print("Student not found.")
def remove_student():
    name = input("Enter student name to remove: ")

    if name in student_names:
        index = student_names.index(name)

        student_names.pop(index)
        student_grades.pop(index)

        print("Student removed successfully!")
    else:
        print("Student not found.")
def calculate_average():
    if len(student_grades) == 0:
        print("No grades available.")
    else:
        average = sum(student_grades) / len(student_grades)
        print("Average grade of the class:", average)
def extreme_grades():
    if len(student_grades) == 0:
        print("No grades available.")
    else:
        highest = max(student_grades)
        lowest = min(student_grades)

        highest_index = student_grades.index(highest)
        lowest_index = student_grades.index(lowest)

        print("Highest grade:", highest,
              "-", student_names[highest_index])

        print("Lowest grade:", lowest,
              "-", student_names[lowest_index])
def display_students():
    if len(student_names) == 0:
        print("No students in the list.")
    else:
        print("\nStudent List:")
        for i in range(len(student_names)):
            print(student_names[i], ":", student_grades[i])
while True:
    print("\n Student Grade Management System")
    print("1. Add new student")
    print("2. Update grade")
    print("3. Remove student")
    print("4. Calculate average grade")
    print("5. Display highest and lowest grade")
    print("6. Display all students")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        update_grade()

    elif choice == "3":
        remove_student()

    elif choice == "4":
        calculate_average()

    elif choice == "5":
        extreme_grades()

    elif choice == "6":
        display_students()

    elif choice == "7":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")