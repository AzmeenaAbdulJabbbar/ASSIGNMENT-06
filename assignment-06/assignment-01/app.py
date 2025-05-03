class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

# Input from user
n = input("Your name: ")
m = int(input("Marks: "))

# Create object and show detail
s = Student(n, m)
s.display()