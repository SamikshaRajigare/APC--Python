project1 = set(input("Enter employees in Project 1: ").split())
project2 = set(input("Enter employees in Project 2: ").split())

both = project1.intersection(project2)

only_project1 = project1.difference(project2)

only_project2 = project2.difference(project1)

total = project1.union(project2)

print("\nEmployees in both projects:", both)
print("Employees only in Project 1:", only_project1)
print("Employees only in Project 2:", only_project2)
print("Total unique employees:", total)