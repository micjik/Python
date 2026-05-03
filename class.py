class Employee:
    num_of_emps = 0 # class varaible
    raise_amount = 1.04 # class variable

    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName # this is instance variable they are set using self parameter
        self.lastName = lastName # this is instance variable they are set using self parameter
        self.pay = pay # this is instance variable they are set using self parameter
        self.email = firstName + lastName + "@gmail.com"
        
        Employee.num_of_emps += 1

    def fullName(self):
        return f"{self.firstName} {self.lastName}"
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return '{} - {}' .format(self.fullName(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullName())

    @classmethod
    def set_raise_amt(cls, amount):
        cls.amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        firstName, lastName, pay = emp_str.split("-")
        return cls(firstName, lastName, pay)
    
    @staticmethod
    def is_Workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, firstName, lastName, pay, prog_lang):
        super().__init__(firstName, lastName, pay)
        #Employee.__init__(self, firstName, lastName, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, firstName, lastName, pay, employees=None):
        super().__init__(firstName, lastName, pay)
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

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullName())


emp1 = Employee("Ayodele", "Adetayo", 5000)
emp2 = Employee("Bolaji", "Daini", 60000)

print(emp1 + emp2)

dev1 = Developer('Corey', 'Schafer', 50000, 'python')
dev2 = Developer('Test', 'Employee', 60000, 'java')

mgr1 = Manager('Sue', 'Smith', 90000, [dev1])

print(mgr1.email)

mgr1.add_emp(dev2)

print(isinstance(mgr1, Developer))
print(issubclass(Developer, Manager))

#print(dev1.email)
#print(dev2.pay)
#print(help(Developer))

import datetime
my_date = datetime.date(2016, 7, 10)
Employee.set_raise_amt = 1.05


#print(Employee.is_Workday(my_date))

#emp_str1 = 'John-Doe-70000'
#emp_str2 = 'Steve-Smith-30000'
#emp_str3 = 'Jane-Doe-90000'

#new_emp_1 = Employee.from_string(emp_str1)

#print(new_emp_1.pay)
#print(new_emp_1.email)

#print(Employee.raise_amount)
#print(emp1.raise_amount)
#print(emp2.raise_amount)

#print(emp1.fullName()) # Note that the self parameter is an instance of a class
#print (Employee.fullName(emp1)) # Note that the self is an emp1.
#print(Employee.__dict__)
#print(emp1.__dict__)
#print(Employee.num_of_emps)
# class variables & instance variables
# class varaibles are all variables shared among all instances of a class
# while instance variable can be unique for each instance like name, email and pay.
# Note that class variables should be the same for each instance
