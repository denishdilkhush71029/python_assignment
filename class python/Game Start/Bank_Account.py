class BankAccount:
    def __init__(self, acc_no, name, balance, pin):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.pin = pin

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount, entered_pin):
        if entered_pin == self.pin:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawn {amount}. Remaining Balance: {self.balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Incorrect PIN!")

# Usage
acc = BankAccount(12345, "Dilkhush", 5000, "0000")
acc.withdraw(1000, "0000")
