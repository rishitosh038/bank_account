# Description: Bank Account simulation using OOP concepts

# Base Class: BankAccount

class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        # Encapsulation: Private attributes
        self.__account_holder = account_holder
        self.__account_number = account_number
        self.__balance = balance

    # Getter methods
    def get_account_holder(self):
        return self.__account_holder
    
    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__balance
    
    # Setter method (controlled access)
    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New Balance: {self.__balance}")
        else: 
            print("Invalid deposited amount")
        
    def withdraw(self, amount):
        if amount <= self.__balance and amount > 0:
            self.__balance -= amount
            print(f"Withdraw {amount}. New Balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount")
    
    def display_details(self):
        print("\n--- Account Details ---")
        print(f"Account Holder : {self.__account_holder}")
        print(f"Account Number : {self.__account_number}")
        print(f"Balance        : {self.__balance}")


# Derived Class: SavingsAccount (Inheritance)

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance=0, interest_rate=0.03):
        super().__init__(account_holder, account_number, balance)
        self.interest_rate = interest_rate

    # Method overriding
    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        print(f"Interest Earned: {interest}")
        return interest
    

# Derived Class: CurrentAccount (Inheritance)

class CurrentAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance=0, overdraft_limit=5000):
        super().__init__(account_holder, account_number, balance)
        self.overdraft_limit = overdraft_limit

    # Method overriding
    def withdraw(self, amount):
        if amount > 0 and amount <= self.get_balance() + self.overdraft_limit:
            new_balance = self.get_balance() - amount
            print(f"Withdrawn {amount}. New Balance: {new_balance}")
        else:
            print("Overdraft limit exceeded")


# Creating Multiple Objects & Simulating Bank Operation

if __name__ == "__main__":
    # Savings Account Object
    
    savings = SavingsAccount("Rishitosh Kumar", "SA12345", 10000)
    savings.display_details()
    savings.deposite(2000)
    savings.withdraw(3000)
    savings.calculate_interest()

    # Current Account Object
    
    current = CurrentAccount("Richa Singh", "CA7890", 5000)
    current.display_details()
    current.deposite(1000)
    current.withdraw(9000)

    print("\n Bank operations completed successfully")