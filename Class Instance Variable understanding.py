class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first.lower() + "." + last.lower() + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(emp_1.first, emp_1.last)
emp_1 = Employee('Moshiur', 'Rahman', 18000)
emp_2 = Employee('Ranti', 'Hasan', 20000)

print(emp_1.email)
print(emp_1.fullname())
print(Employee.fullname(emp_1))


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