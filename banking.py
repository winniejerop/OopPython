from abc import ABCMeta, abstractmethod
from random import randint


# force Use of methods by using a metaclass
class Account(metaclass=ABCMeta):

    @abstractmethod
    def createAccount(self):
        return 0

    @abstractmethod
    def authenticate(self):
        return 0

    @abstractmethod
    def withdraw(self):
        return 0

    @abstractmethod
    def deposit(self):
        return 0

    @abstractmethod
    def displayBalance(self):
        return 0


"""Class SavingsAccount that contains attr and methods of Account"""


class SavingsAccount(Account):
    def __init__(self):
        # Accounts saved in dictionary
        self.savingsAccounts = {}

    def createAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000, 99999)
        # random number as key in dict, name and deposit as value
        self.savingsAccounts[self.accountNumber] = [name, initialDeposit]
        print("Account creation succesful. Your account number is", self.accountNumber)

    """Check whether user entered valid log in data"""
    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingsAccounts.keys():
            if self.savingsAccounts[accountNumber][0] == name:
                print("Authentication successful!")
                self.accountNumber = accountNumber
                return True
            else:
                print("Authentication failed")
                return False
        else:
            print("Authentication failed")
            return False

    def withdraw(self, withdrawalAmount):
        if withdrawalAmount > self.savingsAccounts[self.accountNumber][1]:
            print("Insufficient balance!")
        else:
            self.savingsAccounts[self.accountNumber][1] -= withdrawalAmount
            print("Withdrawal was successful!")
            self.displayBalance()

    def deposit(self, depositAmount):
        self.savingsAccounts[self.accountNumber][1] += depositAmount
        print("Deposit was successful!")
        self.displayBalance()

    def displayBalance(self):
        deposit = self.savingsAccounts[self.accountNumber][1]
        print(deposit)


savingsAccount = SavingsAccount()


while True:
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing programm")
    print("Enter 3 to exit ")

    userChoice = int(input())

    if userChoice == 1:
        print("Enter your name: ")
        name = input()
        print("Enter the initial deposit")
        deposit = int(input())
        savingsAccount.createAccount(name, deposit)
    elif userChoice == 2:
        print("Enter your name: ")
        name = input()
        print("Enter your account number: ")
        accountNumber = int(input())
        authenticationStatus = savingsAccount.authenticate(name, accountNumber)
        if authenticationStatus is True:
            while True:
                print("Enter 1 to withdraw, 2 to deposit")
                print("3 for available balance, 4 for previous menu")
                userChoice = int(input())
                if userChoice is 1:
                    print("Enter a withdrawal amount")
                    withdrawal = int(input())
                    savingsAccount.withdraw(withdrawal)
                    savingsAccount.displayBalance()
                elif userChoice is 2:
                    print("Enter a deposit amount")
                    deposit = int(input())
                    savingsAccount.deposit(deposit)
                    savingsAccount.displayBalance()
                elif userChoice is 3:
                    savingsAccount.displayBalance()
                elif userChoice is 4:
                    break

    elif userChoice is 3:
        quit()