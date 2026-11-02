import json
from datetime import datetime,timedelta

filename="bookdetails.json"

with open(filename,"r") as f:
    books=json.load(f)
    books_list=books["books"]

    
def search_book():
    book_name=input("Enter the Book Name: ")
    with open("bookdetails.json","r") as f:
        book_details=json.load(f)
        
    books=book_details["books"]
    for name in books:
        if book_name==name["title"]:
            print("\nBooks Exits in library")
            print("\n---BOOK DETAILS---")
            print("Book Title:",name["title"])
            print("Book Author:",name["author"])
            print("Book Genre:",name["category"])
            print("Book Published By:",name["publisher"])
            print("Book Price: Rs",name["price"])
            print("Availabe Copies:",name["available_copies"])
            break
    else:
        print("Book Not Found in the library")