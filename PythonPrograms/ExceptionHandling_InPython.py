def divide_numbers(i):
    try:
        result = 10 / i
    except ZeroDivisionError:
        print("Zero se Division kon karta hai bhai.")
    except Exception as e:
        print(e)
    else:
        print("Result aa gaya bhai...")
        print(result)
    finally:
        print("Mujhe kuch farak nhi padta, Mai toh aaunga")

num = int(input("Enter a number"))
divide_numbers(num)

print("-------------------------")

class Bank:                                                 
    def __init__(self,balance):                             
        self.balance=balance

    def withdraw(self,Amount):                              
        if(Amount<0):
            raise Exception("Amount cant be in -ve")        #Raise Exception
        if(Amount>self.balance):
            raise Exception("Paise nahi hai re baba...")    #Raise Exception
        self.balance = self.balance-Amount


Obj = Bank(int(input("Enter Balance")))                     
try:
    Obj.withdraw(int(input("Enter Amount to withdraw")))    
except Exception as e:
    print(e)
else:
    print(Obj.balance)
