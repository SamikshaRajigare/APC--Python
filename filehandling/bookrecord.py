import csv
file = "books.csv"
def add_book():
    with open(file, "a", newline="") as f:
        w = csv.writer(f)
        id = input("Book ID: ")
        title = input("Title: ")
        author = input("Author: ")
        w.writerow([id, title, author, "Available"])
def search():
    key = input("Enter Book ID or Title: ")
    with open(file) as f:
        for b in csv.reader(f):
            if b[0] == key or b[1].lower() == key.lower():
                print(b)
                return
    print("Book not found")
def issue():
    books = list(csv.reader(open(file)))
    id = input("Book ID: ")

    for b in books:
        if b[0] == id:
            if b[3] == "Available":
                b[3] = "Issued"
                print("Book issued")
            else:
                print("Already issued")
            break

    with open(file, "w", newline="") as f:
        csv.writer(f).writerows(books)
def return_book():
    books = list(csv.reader(open(file)))
    id = input("Book ID: ")

    for b in books:
        if b[0] == id:
            b[3] = "Available"
            print("Book returned")
            break

    with open(file, "w", newline="") as f:
        csv.writer(f).writerows(books)
def display():
    with open(file) as f:
        for b in csv.reader(f):
            if b[3] == "Available":
                print(b)
while True:
    print("\n1.Add  2.Search  3.Issue  4.Return  5.Display  6.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_book()
    elif ch == "2":
        search()
    elif ch == "3":
        issue()
    elif ch == "4":
        return_book()
    elif ch == "5":
        display()
    elif ch == "6":
        break
    else:
        print("Invalid choice")
