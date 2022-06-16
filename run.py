import gspread
from google.oauth2.service_account import Credentials
import time
from text import *

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

    print(menu_message)


    while True:
        try:
            
            user_option = int(input("Enter option now: \n"))
            if user_option >= 5:
                print("Number to high. Try again")
                continue
            elif user_option <= 0:
                print("Number to low. Try again.")
                continue
            break
        except ValueError:
            print("Please only choose from 1 / 2 / 3 or 4.")
            continue
    if user_option == 1:
        print("Viewing all books....\n")
        print("We currently have 34 books.\n")
        for i in all_books:
            print(i, '\n')
            time.sleep(0.5)
        print("Want to borrow a book?")
        print("You need to go back to the Main Menu and select that option")
        print("Please keep the details of the book you want to borrow")
        print("We recommend writing the books details down to use in the borrow book section.\n")
       
       
        while True:
            try:
                repeat = str(input("Want to go back to the Main Menu? ( Y = Main Menu / N = Quit App ) \n")).lower()
                if repeat == "n":
                    print("Thankyou for viwing the books we have in stock.")
                    print("We hope next time you find the book your looking for")
                    for i in range(3):
                        print("App quiting...")
                        time.sleep(1)
                    print("App quit successfuly.")
                    quit()
                elif repeat == "y":
                    print("Going back to main menu.")
                    let_user_choose()
                else:
                    print("Try again.")
                    continue
            except ValueError:
                pass
            


    elif user_option == 2:
        get_data()
    elif user_option == 3:
        return_data()
    elif user_option == 4:
        for i in range(3):
            print("App quiting...")
            time.sleep(1)
        print("App quit successfuly.")
        quit()


# function to grab data
def get_data():
    global borrowed_book

    print(borrow_text)

    data_text = input("Please enter your text like the example above now: \n")
    borrowed_book = data_text.split(",")
    update_borrowed_book_worksheet(borrowed_book)

# function to grab details about the returned book to use in update function
def return_data():
    global returned_book

    print(return_message)

    return_text = input("Please enter your text like the example above now: \n")
    returned_book = return_text.split(",")
    update_returned_book_worksheet(returned_book)




#def update_worksheet with data user submited for borrowed
def update_borrowed_book_worksheet(borrowed_book):
    """
    Takes the taken data for borrowed book and adds to worksheet
    """
    for i in range(3):
        print("Updateing worksheet... \n")
        time.sleep(0.5)
    
    borrowed_worksheet = SHEET.worksheet("borrowed-books")
    borrowed_worksheet.append_row(borrowed_book)
    print("Updated sucsesfully...")
    print("Going back to main menu.")
    let_user_choose()

#function to update returned-books sheet useing the data from return_data function.
def update_returned_book_worksheet(returned_book):
    """
    #
    """
    return_worksheet = SHEET.worksheet("returned-books")
    return_worksheet.append_row(returned_book)
    for e in range(3):
        print("Updating..")
        time.sleep(1)
    print("Update complete.\n")
    print("Going back to main menu.")
    let_user_choose()

let_user_choose()