# Python Object-Oriented Programing
# Inheritance - Creating Subclasses


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
    raise_amt = 1.10

    def __init__(self, first, second, pay, prog_lang):
        super().__init__(first, second, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, second, pay, employees=None):
        super().__init__(first, second, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print(f'--> {emp.fullname()}')


dev_1 = Developer('Carlos', 'Garcia', 50000, 'Python')
dev_2 = Developer('Melannie', 'Perez', 60000, 'Java')

mng_1 = Manager('Suzie', 'Guttierez', 120000, [dev_1])
print(mng_1.email)

mng_1.add_emp(dev_2)
mng_1.remove_emp(dev_1)

mng_1.print_emp()

print(isinstance(mng_1, Developer))
print(issubclass(Developer, Employee))
# print(dev_2.email)
# print(dev_2.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
