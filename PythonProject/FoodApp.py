from Models.User import User
from Models.UserManager import UserManager


class LoginSystem:
    def Login(self):
        mailid=input("Email Id:  ")
        password=input("Password:  ")
        user=UserManager.FindUser(mailid,password)
        if user is not None:
            pass
        else:
            print("Invalid username and Password..Please retry")
        
        
    def Register(self):
        name=input("Name:  ")
        mobile=int(input("Mobile No:  "))
        mailid=input("Email Id:  ")
        password=input("Password:  ")
        user=User(name,mobile,mailid,password)
        UserManager.AddUser(user)
    def GuestLogin(self):
        pass  
    def ValidateOption(self,option):
        if option==1:
            self.Login()
        elif option==2:
            self.Register()
        elif option==3:
            self.GuestLogin()
        elif option==4:
            print("Thank you for using our food App!!!")
            exit()
        else:
            print("Invalid Choice...Please retry")    
                          
    
    
class FoodApp:
    LoginOptions={1:"Login",2:"Register",3:"Guest",4:"Exit"}
    @staticmethod
    def Init():
        print("Welcome to Online Food Ordering System")
        loginSystem=LoginSystem()
        while True:
            for option in FoodApp.LoginOptions:
                print(f"{option}.{FoodApp.LoginOptions[option]}",end="  ")
            print() 
            try:   
                choice=int(input("Enter your Choice:")) 
                loginSystem.ValidateOption(choice)
            except ValueError:
                print("Invalid input.. please Enter the valid Choice")    
         