# Python Object-Oriented Programing

class Empregado:
    def __init__(self, primeiro, segundo, pay):
        self.primeiro = primeiro
        self.segundo = segundo
        self.pay = pay
        self.email = f"{primeiro}.{segundo}@company.com"

    def fullname(self):
        return f"{self.primeiro} {self.segundo}"


emp_1 = Empregado('Carlos', 'Garcia', 60000)
emp_2 = Empregado('Melannie', 'Perez', 40000)

print(emp_1.email)
print(emp_1.fullname())
print(Empregado.fullname(emp_1))