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
            user_option = int(input("Enter 1 , 2 or 3 now: "))
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



let_user_choose()