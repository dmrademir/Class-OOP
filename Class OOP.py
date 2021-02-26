# Python Object-Oriented Programing
# Special (Magic/Dunder) Methods

class Employee:
    raise_amount = 1.04

    def __init__(self, first, second, pay):
        self.first = first
        self.second = second
        self.pay = pay
        self.email = f'{self.first}.{self.second}@company.com'

    def fullname(self):
        return f"{self.first} {self.second}"

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    def __repr__(self):
        return f"Employee('{self.first}','{self.second}','{self.pay}')"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Carlos', 'Garcia', 50000 )
emp_2 = Employee('Melannie', 'Perez', 60000)

print(emp_1+emp_2)
print(len(emp_1))
# print(str(emp_1))
# print(repr(emp_1))
