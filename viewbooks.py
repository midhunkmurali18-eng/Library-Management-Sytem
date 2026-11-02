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
    
def view_books():
    with open("bookdetails.json","r") as f:
        book_details=json.load(f)
        
    books=book_details["books"]
    print("\n---BOOKS IN THE LIBRARY---")
    for bookname in books:
        print(bookname["title"])