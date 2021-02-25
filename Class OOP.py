# Python Object-Oriented Programing
# classmethods and staticmethods


class Employee:
    nums_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, second, pay):
        self.first = first
        self.second = second
        self.pay = pay
        self.email = f"{self.first}.{self.second}@company.com"

        Employee.nums_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.second}"

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)


    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first, second, pay = emp_str.split('-')
        return cls(first, second, pay)


emp_str_1 = 'Joana-Santos-50000'
emp_str_2 = 'Joao-Santos-30000'
emp_str_3 = 'Vanessa-Souza-70000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1)

# emp_1 = Employee('Carlos', 'Garcia', 60000)
# emp_2 = Employee('Melannie', 'Perez', 70000)

# Employee.set_raise_amt(1.05)
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

