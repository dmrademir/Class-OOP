# Python Object-Oriented Programing
# Property Decorators - Getters, Setters, and Deleters

class Employee:
    def __init__(self, first, second, pay) -> object:
        self.first = first
        self.second = second
        self.pay = pay

    @property
    def email(self):
        return f'{self.first}.{self.second}@company.com'

    @property
    def fullname(self):
        return f"{self.first} {self.second}"

    @fullname.setter
    def fullname(self, name):
        first, second = name.split(' ')
        self.first = first
        self.second = second

    @fullname.deleter
    def fullname(self):
        print('Delete Name')
        self.first = None
        self.second = None


emp_1 = Employee('Carlos', 'Garcia', 50000)
emp_1.first = 'Carlitos'
emp_1.fullname = 'Mayko Jackson'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
del emp_1.fullname
