# A banking prototype class
class BankAccount:
    def __init__(self,account_number,balance,date_of_opening,customer_details) -> None:
        self.account_number=account_number
        self.balance=balance
        self.date_of_opening= date_of_opening
        self.customer_details=customer_details
    def deposit(self):
        depo=float(input("Enter the amount deposited:"))
        print("The deposit amount is: ",depo)
        self.balance= self.balance + depo
    def withdraw(self):
        Withdraw= float(input("Enter the amount to withdraw:"))
        if Withdraw > self.balance:
            print("Insufficient balance")
        else:
            print("The amount withdrawn is: ",Withdraw)
            self.balance=self.balance-Withdraw
    def check_balance(self):
        # self.balance=self.balance-self.withdraw
        print("The amount remaining is: ",self.balance)
    def show_customer_details(self):
        print("Customer details:")
        print("Account Number:", self.account_number)
        print("Date of Opening:", self.date_of_opening)
        print("Customer Name:", self.customer_details[2])
       
accNo= str(input("Enter your account number:"))
dates= str(input("Enter the day of opening of the account:"))
name= str(input("Enter your name: "))
customer_details=(accNo,dates,name)
bank= BankAccount(accNo,000,dates,customer_details)
bank.show_customer_details()
bank.deposit()
bank.withdraw()
bank.check_balance()

