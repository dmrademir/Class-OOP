# Python Object-Oriented Programing

class Employee:
    def __init__(self, first, second, pay):
        self.first = first
        self.second = second
        self.pay = pay
        self.email = f"{self.first}.{self.second}@company.com"

    def fullname(self):
        return f"{self.first} {self.second}"


emp_1 = Employee('Carlos', 'Garcia', 60000)
emp_2 = Employee('Melannie', 'Perez', 40000)

print(emp_1.email)
print(emp_1.fullname())
print(Empregado.fullname(emp_1))