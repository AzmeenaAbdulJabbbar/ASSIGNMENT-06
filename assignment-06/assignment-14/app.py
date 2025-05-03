class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        return f"Employee Name: {self.name}, Role: {self.role}"

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee 

