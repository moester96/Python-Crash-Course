class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, salary_raise=5000):
        new_salary = str(self.annual_salary + salary_raise)
        print(f'{self.first_name.title()} {self.last_name.title()} previous salary: {self.annual_salary}')
        print(f'{self.first_name.title()} {self.last_name.title()} new salary: {new_salary}')

# Employee1 = Employee('mohammed', 'mubarak', 50000)

# Employee1.give_raise(22500)