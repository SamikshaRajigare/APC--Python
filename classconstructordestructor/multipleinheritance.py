class Father:
    def __init__(self, father_name):
        self.father_name = father_name
        print("Father constructor called")
    def display_father(self):
        print("Father Name:", self.father_name)
class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name
        print("Mother constructor called")
    def display_mother(self):
        print("Mother Name:", self.mother_name)
class Child(Father, Mother):
    def __init__(self, father_name, mother_name, child_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.child_name = child_name
        print("Child constructor called")
    def display_child(self):
        self.display_father()
        self.display_mother()
        print("Child Name:", self.child_name)
    def __del__(self):
        print("Child destructor called")
child = Child("Raj", "Priya", "Rahul")
child.display_child()
del child