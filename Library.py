from signup import signup
from login import log_in
from viewbooks import view_books
from searchbook import search_book
from addbook import add_book
from deletebook import delete_book
from issue_book import issue_book
from return_book import return_book



print("---LIBRARY MANAGEMENT SYSTEM---")
print("1. Sign Up")
print("2. Log in")
print("3. Exit")


while True:
    
    choice=input("\nEnter Your Choice: ")
    
    match choice:
        
        case "1":
            signup()
            
            print("\n1. Sign Up")
            print("2. Log in")
            print("3. Exit")
            
        case "2":
            log_in_mail=log_in()
            
            while True:
                print("\n---LIBRARY MENU---")
                print("1. View Books")
                print("2. Search a Book")
                print("3. Add a Book")
                print("4. Delete a Book")
                print("5. Issue a Book")
                print("6. Return a Book")
                print("7. Exit")
                
                choice_2=input("\nEnter a choice: ")
                
                match choice_2:
                    case "1":
                        view_books()
                    case "2":
                        search_book()
                    case "3":
                        add_book()
                    case "4":
                        delete_book()
                    case "5":
                        issue_book(log_in_mail)
                    case "6":
                        return_book(log_in_mail)
                    case "7":
                        print("\nLogging You Out....")
                        break
                                
        case "3":
            print("Exiting.....")
            break
        case _:
            print("Invalid Input")
            exit