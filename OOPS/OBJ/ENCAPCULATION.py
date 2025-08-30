'''
Abstraction of details 

'''


class BankAccount:
    def __init__(self, Name, Account_Number, IFSC_Code, Balance):
        self.Name = Name
        self.Account_Number = Account_Number
        self.IFSC_Code = IFSC_Code
        self.__Balance = Balance  # private attribute

    def deposit(self, amount):
        self.__Balance += amount
        print(f"The amount has been deposited in account \n{self.Account_Number} \nholder name {self.Name}\nnew balance is {self.__Balance}")

    def get_balance(self):
        return self.__Balance

# Creating an object
account = BankAccount("Kartik Pant", "123456", "ICFCE34262", 500)

account.deposit(5000)
print(account.get_balance())
