


# class Human:
#     def __init__(self, name):
#         self.name = name

#     def message(self):
#         print(f'Welcome {self.name}')

#     @classmethod
#     def class_info(cls):
#         return 'it is a species of Homosapiens'

#     @staticmethod
#     def static_method():
#         return f'It is static method'

# one = Human('Oleksii')
# one.message()
# print(Human.class_info())
# print(one.static_method())

class Employee:
    employeesCount: int = 0 

    def __init__(self, name, salary = 0):
        self.name = name
        self.salary = salary
        Employee.employeesCount += 1

    def employeeInfo(self):
        print(f'Name: {self.name}')
        print(f'Salary: {self.salary}')

    @classmethod
    def employeesNumber(cls):
        return cls.employeesCount   

emp1 = Employee('Oleksii', 5000)
emp2 = Employee('Petro', 4500)
emp3 = Employee('Oksana', 5000)
emp1.employeeInfo()
print(Employee.employeesNumber())

print("__bases__  :", Employee.__bases__)
print("__dict__   :", Employee.__dict__)
print("__name__   :", Employee.__name__)
print("__module__ :", Employee.__module__)
print("__doc__    :", Employee.__doc__)



        
    