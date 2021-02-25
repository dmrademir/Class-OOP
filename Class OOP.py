# Python Object-Oriented Programing
# Subclasses


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

class Developer(Employee):
    pass

dev_1 = Developer('Carlos', 'Garcia', 60000)
dev_2 = Developer('Melannie', 'Perez', 70000)

print(help(Developer))
