import json
from datetime import datetime,timedelta

filename="bookdetails.json"

with open(filename,"r") as f:
    books=json.load(f)
    books_list=books["books"]

def add_book():
    book_name=input("\nEnter the book name to be added: ")
    
    with open(filename,"r") as f:
        book_details=json.load(f)
        
    books=book_details["books"]
    
    for name in books:
        if name["title"]==book_name:
            print("Books exists in the library......")
            no_of_books=int(input("Enter the number of copies to add: "))
            name["total_copies"]+=no_of_books
            name["available_copies"]+=no_of_books
            print(f"\n{no_of_books} copies of \"{book_name}\" has been added to the library.")
            print("Available Copies After Adding: ",name["available_copies"])
            print("Total Copies After Adding: ",name["total_copies"])
            with open(filename,"w") as f:
                json.dump(book_details,f,indent=4)
            break
    
    else:
        print("Book does not exists in the library. \nEnter the below details to add book in the library: ")
        
        book_author=input("Enter the Book Author: ")
        book_genre=input("Enter the Book Genre: ")
        book_isbn=input("Enter the 13 digit ISBN: ")
        book_year=int(input("Enter the Publication Year: "))
        book_publisher=input("Enter the Book Publisher: ")
        book_price=int(input("Enter the Book Price: "))
        book_count=int(input("Enter the number of copies to add: "))
        
        size=len(books)
        book_id=size+1     
        
        new_book={
        "book_id": book_id,
        "title": book_name,
        "author": book_author,
        "category": book_genre,
        "isbn": book_isbn,
        "publication_year": book_year,
        "publisher": book_publisher,
        "price": book_price,
        "available_copies": book_count,
        "total_copies": book_count
        }
        
        books.append(new_book)
        
        with open(filename,"w") as f:
            print("Book Has Been Added to the library")
            json.dump(book_details,f,indent=4)