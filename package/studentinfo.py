class EngineeringStudent:
    def __init__(self, name, roll_no, div, branch, sem1, sem2, sem3, sem4):
        self.name = name
        self.roll_no = roll_no
        self.div = div
        self.branch = branch
        self.sem1 = sem1
        self.sem2 = sem2
        self.sem3 = sem3
        self.sem4 = sem4
    def display(self):
        print("\nStudent Information")
        print("Name     :", self.name)
        print("Roll No. :", self.roll_no)
        print("Division :", self.div)
        print("Branch   :", self.branch)

        print("\nStudent Result")
        print("First Semester  :", self.sem1)
        print("Second Semester :", self.sem2)
        print("Third Semester  :", self.sem3)
        print("Fourth Semester :", self.sem4)

name = input("Enter Student Name: ")
roll_no = input("Enter Roll No.: ")
div = input("Enter Division: ")
branch = input("Enter Branch: ")
sem1 = input("Enter First Semester Result: ")
sem2 = input("Enter Second Semester Result: ")
sem3 = input("Enter Third Semester Result: ")
sem4 = input("Enter Fourth Semester Result: ")

student = EngineeringStudent(
    name, roll_no, div, branch, sem1, sem2, sem3, sem4
)
student.display()
