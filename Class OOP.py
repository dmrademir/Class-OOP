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
    raise_amt = 1.10

    def __init__(self, first, second, pay, prog_lang):
        super().__init__(first, second, pay)
        self.prog_lang = prog_lang


dev_1 = Developer('Carlos', 'Garcia', 50000, 'Python')
dev_2 = Developer('Melannie', 'Perez', 60000, 'Java')

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)


