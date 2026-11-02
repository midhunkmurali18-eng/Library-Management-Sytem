import json
from datetime import datetime,timedelta

filename2="userdetails.json"

with open(filename2,"r") as f:
    users_details=json.load(f)
    user_list=users_details["users"]
    
    
def log_in():
    user_mail=input("Enter your Mail: ")
    with open("userdetails.json","r") as f:
        user_data=json.load(f)
        
    user_details=user_data["users"]
    
    for user in user_details:
        if user["mail"]==user_mail:
            user_password=input("Enter your Password: ")
            
            if user["mail"]==user_mail and user["password"]==user_password:
                print("\nWelcome",user["name"])
                print("Loging in.....")
                log_in_user_mail=user["mail"]
                return log_in_user_mail
            
            elif user["mail"]==user_mail and user["password"]!=user_password:
                print("Wrong Password")
                print("Try Again")
                return log_in()
        
    else:  
        print("Mail Id not found....")
        return log_in()