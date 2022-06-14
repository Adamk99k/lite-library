import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('lite-library')

books = SHEET.worksheet('books')

all_books = books.get_all_values()


def let_user_choose():
    """
    Gets user input for what option they want to pick. 
    either view all books available or borrow a book
    or return a borrowed book
    """
    print("\n")
    print("Wellcome to Lite Library. \n")
    print("Please select the service you require. \n")
    print("1 = View books available.")
    print("2 = Borrow a book.")
    print("3 = Return a borrowed book. \n")


    while True:
        try:
            global user_option
            user_option = int(input("Enter 1 , 2 or 3 now: \n"))
            if user_option > 3:
                print("No option for that number. Try again")
                continue
            elif user_option <= 0:
                print("Number to low. Try again.")
                continue
            print(f'Your choice was {user_option}')
            break
        except ValueError:
            print("Please only choose from 1 / 2 or 3.")
            continue


    if user_option == 1:
        print("Viewing all books....\n")
        for i in all_books:
            print(i, '\n')
        print("If you want to borrow a book ")
        print("please seclect option '2' from the main menu.")
        print("Make sure you remember the details of the book you want to borrow if thats what you decide to do... \n")
        repeat = str(input("Want to go to main menu? yes / no : \n")).lower()
        if repeat == "yes":
            print("Going to main menu..")
            let_user_choose()
        else:
            print("No problem, Please do come back if you want to use lite library..")
            quit()
    elif user_option == 2:
        print("You want to borrow a book. GREAT!! \n")
        print("Please follow our instructions to add your borrowed book to our list.")
        # grab users borrowed book details and add to google sheet 'Borrowed books' then return a message comfiming book has been added successfuly.
    elif user_option == 3:
        print("You choose to retunr a book your previously borrowed.")
        print("Thank you from us at Lite Library for retrning your book.")
        print("Please follow our prompts so we can update your account on our list to")




let_user_choose()