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


emp_1 = Employee('Carlos', 'Garcia', 60000)
emp_2 = Employee('Melannie', 'Perez', 70000)
emp_3 = Employee('Carla','Martinez', 78000)
emp_2.raise_amount = 1.05
print(emp_2.__dict__)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

print(Employee.nums_of_emps)

# print(Employee.__dict__)
