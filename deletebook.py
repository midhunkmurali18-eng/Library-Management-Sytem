import json
from datetime import datetime,timedelta

filename="bookdetails.json"

with open(filename,"r") as f:
    books=json.load(f)
    books_list=books["books"]
    
    
def delete_book():
    book_isbn=input("Enter the 13 digit isbn of the book to be deleted from the library: ")
    
    for name in books_list:
        if book_isbn==name["isbn"]:
            print(f"\nBook name : {name["title"]}")
            books_list.remove(name)
            deleted_book_id=name["book_id"]
            
            for id in books_list:
                if id["book_id"]>deleted_book_id:
                    id["book_id"]-=1
                    
            print("Book Successfully Deleted from Library.")
            break 
    else:
        print("Book not found in Library Database")
        
    with open(filename,"w") as f:
        json.dump(books,f,indent=4)