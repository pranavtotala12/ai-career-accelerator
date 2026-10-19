class Bank:                                                 #class create
    def __init__(self,balance):                             #Constructor create
        self.balance=balance

    def withdraw(self,Amount):                              #Function create
        if(Amount<0):
            raise Exception("Amount cant be in -ve")        #Raise Exception
        if(Amount>self.balance):
            raise Exception("Paise nahi hai re baba...")    #Raise Exception
        self.balance = self.balance-Amount


Obj = Bank(int(input("Enter Balance")))                     #Object created
try:
    Obj.withdraw(int(input("Enter Amount to withdraw")))    #Function Call
except Exception as e:
    print(e)
else:
    print(Obj.balance)
