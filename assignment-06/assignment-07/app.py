class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  # Public variable
        self._salary = salary  # Protected variable
        self.__ssn = ssn  # Private variable

# Employee ka object banate hain
emp = Employee("azmeena", 50000, "123-458-98759")
print(emp.name)        # Public
print(emp._salary)     # Protected
# print(emp.__ssn)     # Will raise AttributeError
