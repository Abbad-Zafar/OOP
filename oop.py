
class Employee:

    raise_amt = 1.04 #Class vaiable

    def __init__(self, first, last , pay): ## Instance of class as first argument
        self.first = first
        self.last = last
        self.pay = pay


    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @classmethod ## Class as first argument # Engage directly with class variables
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount 

    @staticmethod  ## Used when we dont use instance or class within function
    def  is_workday(day):
        if day == "Monday":
            return True
        return False




emp_1 = Employee("Abbad", "Zafar", 100)

Employee.set_raise_amt(1.05)

print(emp_1.raise_amt)

Day = Employee.is_workday("ss")

print(Day)

