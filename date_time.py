from datetime import datetime,timedelta

# issue_date=input("Enter the Issue Date: ")
issue_date="5-6-2026"
# datetime used to represent and work with date and time 
# strptime convert input to a datetime object that is speified like %d-%m-%Y
# date extracts date from the object containing data along with time ( the object will be like 2026-08-12 00:00:00), we only need date from it
issue_date=datetime.strptime(issue_date,"%d-%m-%Y").date()
print("Issue Date:",issue_date)

allowed_days=int(input("Enter the number of days the book is issued: "))
# timedelta represents a duration and lets you add or subtract days,weeks,etc
due_date=issue_date+timedelta(days=allowed_days)
print("Due Date:",due_date)

# return_date=input("Enter the date the book is returned: ")
return_date="11-6-2026"
return_date=datetime.strptime(return_date,"%d-%m-%Y").date()
print("Return Date:",return_date)

days_kept=(return_date-issue_date).days
print("Days Kept:",days_kept)
print(type(days_kept))