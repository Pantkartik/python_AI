class Bankaccount:
    def __init__(self,Name,Account_Number,IFSC_Code,Balance):
        self.Name=Name
        self.Account_Number=Account_Number
        self.IFSC_Code=IFSC_Code
        self.__Balance=Balance
        
    def deposit(self,amount):
        self.__Balance +=amount
        print(f"The amount has been deposited in account{self.Account_Number} holder name{self.Name}, new balance is {self.__balance}")
        
    def get_balance(self):
        return self.__balance
    
account=Bankaccount("kartik pant","123456","ICFCE34262",500)

account.deposit(5000)
print(account.get_balance())
