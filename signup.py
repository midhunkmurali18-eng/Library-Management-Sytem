import json

filename2="userdetails.json"

with open(filename2,"r") as f:
    users_details=json.load(f)
    user_list=users_details["users"]

def signup():
    
    user_name=input("Enter Your name: ")
    user_mail=input("Enter Your Mail: ")
    user_password=input("Enter the password: ")
    
    for user in user_list:
        if user_mail==user["mail"]:
            print("Mail Id Already Exists.")
            return
        
    new_user_details={"name":user_name,
                      "mail":user_mail,
                      "password":user_password,
                      "issued_books":[]}
    
        
    user_list.append(new_user_details)
    print("\nSigning Up....")
        
    with open("userdetails.json","w") as f:
                    json.dump(users_details,f,indent=4)