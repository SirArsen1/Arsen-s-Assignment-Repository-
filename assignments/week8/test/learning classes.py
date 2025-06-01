class employee:

    raise_amount = 1.05
    num_of_emps = 0

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@comail.com'

        employee.num_of_emps += 1

    def full_name(self):
        return '{} {}.'.format(self.first_name, self.last_name)
    def salary(self):
        return '{} makes {}.'.format(self.first_name, self.pay)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        print(f"After a raise, {self.first_name} makes {self.pay}")
    def full_info(self):
        return f'''Name: {self.full_name()}
Email: {self.email}
Salary: {self.pay}'''

emp1 = employee('Jerry', 'Seinfeld', 95000)
emp2 = employee('George', 'Costenza', 0)
emp3 = employee('Elaine', 'Benes', 75000)

print(f"{emp1.full_info()}\n\n{emp2.full_info()}\n\n{emp3.full_info()}")