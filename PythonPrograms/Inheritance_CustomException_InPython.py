
# Custom Exception Class created so that can get full control over Exception to Handle

class SecurityError(Exception):                            #Inherite from Exception Class
    def __init__(self,meassage):                           #Contructor Cretaed
        print(meassage)

    def logout(self):                                      #Logout Function Created
        print("Bhai logout kar diya tuze")

class Google:
    def __init__(self,name,email,password,device):
        self.name = name
        self.email = email
        self.password = password
        self.device = device

    def login(self,email,password,device):
        if device != self.device:
            raise SecurityError("Bhai tere account kisi dusre device se login ho raha hai")
                                                          #Inherite Class Object Created and 
                                                          #send as exception to the except block
        if email == self.email and password == self.password :
            print("Welcome to Bank")
        else:
            print("Login Error")

obj = Google("Pranav","pranavtotala@gmail.com","1234","Mobile")

try:
    #obj.login("pranavtotala@gmail.com","1234","Mobile")
    obj.login("pranavtotala@gmail.com","1234","Laptop")
except SecurityError as e:                                 #Catch object of Inherite class
    e.logout()                                             #Call Inherite Class function
else:
    print(obj.name)
finally:
    print("all connection closed")


