
class Employee:

    raise_amt = 1.04 #Class vaiable

    def __init__(self, first, last , pay): ## Instance of class as first argument
        self.first = first
        self.last = last
        self.pay = pay


    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    
    @classmethod ## Class as first argument # Engage directly with class variables
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount 

    @staticmethod  ## Used when we dont use instance or class within function
    def  is_workday(day):
        if day == "Monday":
            return True
        return False

class Developer(Employee):  # Sub class of Employee class # Everything of Employee class can be accesed.
    raise_amt = 1.10
    def __init__(self, first, last , pay, prog_lang):
        super().__init__(first, last , pay)
        self.prog_lang = prog_lang


emp_1 = Employee("Abbad", "Zafar", 100)

Employee.set_raise_amt(1.05)

print(emp_1.raise_amt)

Day = Employee.is_workday("ss")

print(Day)

Dev_1 = Developer("Dev", "loper", 100, "Lina")
print(Dev_1.fullname())
print(Dev_1.pay)
Dev_1.apply_raise() # It will use developer class raise amount # Not Parent Class
print(Dev_1.pay)

emp_2 = Employee("Emp", "loye", 100)
print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)

Dev_2 = Developer("Dev", "loper", 1020, "Lina")
print(Dev_2.fullname())
print(Dev_2.prog_lang)








