from Models.User import User
from Models.UserManager import UserManager
import re


class LoginSystem:
    def Login(self):
        mailid=input("Email Id:  ")
        password=input("Password:  ")
        user=UserManager.FindUser(mailid,password)
        if user is not None:
            print("Login Successfull!")
        else:
            print("Invalid username and Password..Please retry")
        
        
    def Register(self):
        while True:
            name = input("Name: ")
            if not name.isalpha():
                print("Name should only contain letters.")
                continue
            
            # Validate Mobile Number
            mobile = input("Mobile No: ").strip()
            if not (mobile.isdigit() and len(mobile) == 10):
                print("Mobile number should be exactly 10 digits.")
                continue
            
            # Validate Email ID
            mailid = input("Email Id: ").strip()
            if not (re.match(r"[^@]+@[^@]+\.[^@]+", mailid)):
                print("Invalid email address.")
                continue
            
            # Validate Password
            password = input("Password: ").strip()
            if len(password) < 6:
                print("Password should be at least 6 characters long.")
                continue

    def GuestLogin(self):
        pass
    def Exit():
        print("Thank you for using our food App!!!")
        exit()
        
          
    def ValidateOption(self,option):
        #it is a attribute which calls the option we are using() because it acts as a method
        getattr(self,option)()
                          
    
    
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
                loginSystem.ValidateOption(FoodApp.LoginOptions[choice])
            except (ValueError,KeyError):
                print("Invalid input.. please Enter the valid Choice")    
         