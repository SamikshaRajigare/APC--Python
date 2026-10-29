def total_marks(marks):
    return sum(marks)

def percentage(marks):
    return (sum(marks) / (len(marks) * 100)) * 100

def grade(per):
    if per >= 90:
        return "A+"
    elif per >= 80:
        return "A"
    elif per >= 70:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 40:
        return "D"
    else:
        return "Fail"
if __name__ == "__main__":
    import student

    name = input("Enter student name: ")
    n = int(input("Enter number of subjects: "))

    marks = []
    for i in range(n):
        mark = float(input(f"Enter marks for subject {i + 1} (out of 100): "))
        marks.append(mark)

    total = student.total_marks(marks)
    per = student.percentage(marks)
    g = student.grade(per)

    print("\n--- Student Result ---")
    print("Name:", name)
    print("Total Marks:", total, "/", n * 100)
    print("Percentage:", round(per, 2), "%")
    print("Grade:", g)