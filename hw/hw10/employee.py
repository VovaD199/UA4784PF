#10.3.3
from hooman import Hooman
class Employee(Hooman):
    """
    Employee class
    Works only for chocolates)
    """
    employee_count = 0
    def __init__(self,name:str="Abra Cadabra",salary:float=42):
        super().__init__(name)
        assert salary>0,"Salary should be positive (at least, IMP)"
        self.name = name
        self.salary = salary
        Employee.employee_count+=1
        self.employee_id = Employee.employee_count

    @staticmethod
    def GetEmployeeCount():
        return Employee.employee_count

    def PrintEmployeeInfo(self):                                                                                    #yes, i copied π only for this
        print(f"Employee #{self.employee_id} is {self.name} and has a salary of {self.salary:.2f} pieces of chocolate per π days")
        
    
if __name__ == "__main__":
    emp = Employee("Jack",12)
    emp.Greet()
    print(emp.GetEmployeeCount()) #1
    emp.PrintEmployeeInfo() #Employee #1 is Jack and has a salary of 12.00 pieces of chocolate per π days

    emp42 = Employee("Raiden",21)
    print(emp42.GetEmployeeCount()) #2
    emp42.PrintEmployeeInfo() #Employee #2 is Raiden and has a salary of 21.00 pieces of chocolate per π days

    #emp_error = Employee("Error",-42) #Salary assertion error
    print(Employee.__doc__)                                                                                                         #will print __main__ as this block even in __main__ module
    print(f"{Employee.__name__} is derived from {Employee.__base__.__name__}\nhas a namespace {Employee.__dict__}\nand is located in {Employee.__module__} module")
