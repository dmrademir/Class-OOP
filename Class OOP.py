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

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Carlos', 'Garcia', 60000)
emp_2 = Employee('Melannie', 'Perez', 70000)

import datetime
my_date = datetime.date(2021,2,25)

print(emp_1.is_workday(my_date))
