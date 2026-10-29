try:
    name = input("Enter Name: ")
    if name.isdigit():
        raise ValueError("Name should be in string format")
    roll_no = input("Enter Roll No.: ")
    if not roll_no.isdigit():
        raise ValueError("Roll No. should be in integer format")
    roll_no = int(roll_no)
    div = input("Enter Division: ")
    if div.isdigit():
        raise ValueError("Division should be in character format")
    print("\nStudent Record")
    print("Name:", name)
    print("Roll No.:", roll_no)
    print("Division:", div)
except ValueError as e:
    print("Exception:", e)
