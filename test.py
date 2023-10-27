class Employee:
    
    progress = 1.3
    
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name.lower() + "." + last_name.lower() + "@gmail.com"
        self.salary = salary
        
        
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    def salary_progress(self):
        self.salary = int(self.progress*self.salary)
        
class Developer(Employee):
    progress = 1.5
    def __init__(self, first_name, last_name, salary, prog_lang):
        super().__init__(first_name, last_name, salary)
        self.prog_lang = prog_lang
        
class Manager(Employee):
    def __init__(self, first_name, last_name, salary, employees=None):
        super().__init__(first_name, last_name, salary)
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
            print("--> ", emp.fullname())
        
emp_1 = Employee("Zhantai", "Isakov", 600)
dev_1 = Developer('Zhyldyzbek', 'Zhalynbekov', 1000, 'Python')
man_1 = Manager("Umut", "Arpidinov", 1200, [emp_1])

# man_1.add_emp(dev_1)
# man_1.remove_emp(emp_1)
# man_1.print_emp()



print(emp_1)
# emp_1.salary_progress()
# print(emp_1.salary)

