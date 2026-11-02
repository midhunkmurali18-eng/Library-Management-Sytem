import json
from datetime import datetime,timedelta

filename="bookdetails.json"
filename2="userdetails.json"

with open(filename,"r") as f:
    books=json.load(f)
    books_list=books["books"]

with open(filename2,"r") as f:
    users_details=json.load(f)
    user_list=users_details["users"]
    
    
def return_book(log_in_mail):
    for user in user_list:
        if user["mail"]==log_in_mail:
            if not user["issued_books"]:
                print("\nYou do not have books to return")
            else:
                print("\nYou have books to return")

                return_book_name=input("\nEnter the name of the returning book: ")
                
                for book in user["issued_books"]:
                    if book["title"]==return_book_name:
                        
                        issue_date=book["issue_date"]
                        return_date=book["return_date"]
                        issue_date=datetime.strptime(issue_date,"%d-%m-%Y").date()
                        return_date=datetime.strptime(return_date,"%d-%m-%Y").date()
                        
                        book_return_date=input("Enter the date the book is returned: ")
                        book_return_date=datetime.strptime(book_return_date,"%d-%m-%Y").date()
                        
                        book_allowed_days=(return_date-issue_date).days
                        book_taken_days=(book_return_date-issue_date).days

                        days_difference=book_taken_days-book_allowed_days
                        fine_per_day=10
                        
                        if days_difference<=0:
                            
                            print("No Fine")
                            
                            user["issued_books"].remove(book)
                            with open(filename2,"w") as f:
                                json.dump(users_details,f,indent=4)
                            
                            for name in books_list:
                                
                                if name["title"]==return_book_name:                                  
                                    name["available_copies"]+=1                                   
                                    with open(filename,"w") as f:
                                        json.dump(books,f,indent=4)                                    
                                    break
                                
                            print("\nBook Successfully Returned")
                            break
                        
                        else:
                            print("\nFine Per Day : Rs 10")
                            print(f"The book was kept for {days_difference} extra days")
                            print(f"Payable Fine : Rs {days_difference*fine_per_day}")
                            print("Pay fine and return the book")