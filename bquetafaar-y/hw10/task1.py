class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number
        self.__balance = balance
        self._account_holder = account_holder
    @property
    def account_holder(self):
        return self._account_holder
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if self.__balance < amount:
            return "Insufficient funds"
        else:
            self.__balance -= amount
    def check_balance(self):
        return self.__balance

my_account = BankAccount("123456789", "John Doe", 1000.0)
print(my_account._account_holder)
print(my_account.check_balance())

my_account.deposit(500)
print(my_account.check_balance())

my_account.withdraw(200)
print(my_account.check_balance())

print(my_account.withdraw(2000))