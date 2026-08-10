class BankAccount:
    def __init__(self, account_number: str, account_holder: str, balance: float):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    @property
    def account_holder(self):
        return self.__account_holder

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return self.__balance
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                return self.__balance
            else:
                print("Insufficient funds")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        return self.__balanceÍ