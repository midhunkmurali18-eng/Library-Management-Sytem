import json
from datetime import datetime,timedelta

filename="bookdetails.json"
with open(filename,"r") as f:
    books=json.load(f)
    books_list=books["books"]
    
filename2="userdetails.json"
with open(filename2,"r") as f:
    users=json.load(f)
    user_list=users["users"]
    

def issue_book(log_in_email):
    
    book_taken=input("Enter The Book Name for Issue: ")
    
    for name in books_list:
        
        if name["title"]==book_taken:
             
            if name["available_copies"]>0:
                
                print("Book Available in Library") 
                
                for user in user_list:
                                        
                    if user["mail"]==log_in_email:
                        
                        for copy in user["issued_books"]:
                            if copy["title"]==book_taken:
                                print("Book Already Issued to the current user,Choose another Book !")
                                return
                            
                        issue_date=input("Enter the issue date: ")
                        no_days=int(input("Enter the number of days the book is issued: "))
                        issue_date=datetime.strptime(issue_date,"%d-%m-%Y").date()
                        return_date=issue_date+timedelta(days=no_days)
                        
                        issued_book_details={"title":book_taken,
                                                "issue_date":issue_date.strftime("%d-%m-%Y"),
                                                "return_date":return_date.strftime("%d-%m-%Y")} 
                           
                        user["issued_books"].append(issued_book_details)
                        name["available_copies"]-=1
                        
                        print(user)
                        
                        with open(filename2,"w") as f:
                            json.dump(users,f,indent=4)
                        
                        with open(filename,"w") as f:
                            json.dump(books,f,indent=4)
                
                        print(f"The Book named \"{name["title"]}\" is issued for {no_days} days and should be returned on {return_date}")
                
            else:
                print("Book is currently out of stock.")
                
            break
    else:
        print("Book not Available in Library")