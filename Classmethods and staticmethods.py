class Employee:
    num_of_emps = 0     # this is the class variable
    raise_amount = 1.04 # this is the class variable

    def __init__(self, first, last, pay):
        self.first = first # this is the instance/object variable
        self.last = last
        self.email = first.lower() + "." + last.lower() + '@gmail.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(self.pay * 1.05)
        # return int(self.pay * 1.05)
        return int(float(self.pay) * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        str_1 = 'Given date is a holiday. Day is:'
        str_2 = 'Given date is a workday. Day is:'
        weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
        if day.weekday() == 4 or day.weekday() == 5:
            return str_1, weekDays[day.weekday()]
        return str_2, weekDays[day.weekday()]
emp_1 = Employee('Moshiur', 'Milton', 18000)    # this is the first instance/object in Employee class
emp_2 = Employee('Ranti', 'Hasan', 20000)       # this is second instance

import datetime
date_entry = input('Enter a date in YYYY-MM-DD format')
year, month, day = map(int, date_entry.split('-'))
my_date = datetime.date(year, month, day)
# my_date = datetime.date(2020, 7, 10)
print(Employee.is_workday(my_date))

# emp_str_1 = 'Moshiur-Milton- 20000'
# emp_str_2 = 'Ranti-Hasan-18000'
#
#
# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.first)
# print(new_emp_1.email)
# print(new_emp_1.fullname())
# Employee.set_raise_amt(1.05)
#
# print(Employee.raise_amount)
# print(new_emp_1.pay)
# print(new_emp_1.raise_amount)
# print(new_emp_1.apply_raise()) # this line will not work if we dont make self.pay float in apply_raise()

# Employee.set_raise_amt(1.08)
# print(emp_1.raise_amount)
# print(emp_1.apply_raise())

# # We will create a blank class
# class Employee:
#     pass
#
# emp_1 = Employee()
# emp_2 = Employee()
#
# print(emp_1)
# print(emp_2)
#
# emp_1.first = 'Moshiur'
# emp_1.last = 'Rahman'
# emp_1.email = 'moshiur.rahman@company.com'
# emp_1.pay = 18000
#
# emp_2.first = 'Ranti'
# emp_2.last = 'Hasan'
# emp_2.email = 'ranti.hasan@company.com'
# emp_2.pay = 20000
#
# print(emp_1.email)
# print(emp_2.email)



# class Employee:
# 
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay
# 
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
# 
# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Test', 'Employee', 60000)