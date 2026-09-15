class Employee:
    """Клас для представлення працівника та відстеження їх загальної кількості."""
    
    total_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_count += 1

    @classmethod
    def display_total_count(cls):
        print(f"Загальна кількість працівників: {cls.total_count}")

    def display_info(self):
        print(f"Працівник: {self.name}, Зарплата: {self.salary}")

emp1 = Employee("Іван", 50000)
emp2 = Employee("Марія", 60000)

emp1.display_info()
emp2.display_info()
Employee.display_total_count()
