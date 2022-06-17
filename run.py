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
    This function will act as the Main Menu for Lite Library.
    It will give users a selection of options to take them to
    the required service.
    For each option there is a correlated action for python to take.
    some of which are. 
    Calling upon other functions to take over.
    Others are more simple with a default quit() and print() message.

    By keeping all this in one function, it offers a clean way to take 
    Users back to the Main Menu if needed.
    """
    
    print(menu_message)
    # menu_message is defined on (text.py) file.

    while True:
    # This is a while loop that will keep running until user input is a number between (1-4).
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
        # This will print all books available on the external worksheet, with a delay.
        print("Viewing all books....\n")
        print("We currently have 34 books.\n")
        for i in all_books:
            print(i, '\n')
            time.sleep(0.5)
        print("Want to borrow a book?")
        print("You need to go back to the Main Menu and select that option")
        print("Please keep the details of the book you want to borrow")
        print("We recommend writing the book details down to use when prompted to.\n")
       
       
        while True:
        # User has the option to go back to main menu (restarts). 
        # Will keep prompting user until a valid response is met.
            try:
                repeat = str(input("Want to go back to the Main Menu? ( Y = Main Menu / N = Quit App ) \n")).lower()
                if repeat == "n":
                    print("Thank-you for viewing the books we have in stock.")
                    print("We hope next time you find the book your looking for.")
                    for i in range(3):
                        print("App quitting...")
                        time.sleep(1)
                    print("App quit successfuly.")
                    quit()
                elif repeat == "y":
                    print("Going back to Main Menu.\n")
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
            print("App quitting...")
            time.sleep(1)
        print("App quit successfully.")
        quit()


def update_borrowed_book_worksheet(borrowed_book):
    """
    This function will append the data passed to it to the (borrowed-books) worksheet
    and a delayed print message to keep the user updated on what's happening.

    This function takes one variable named (borrowed_book). This would have already been defined 
    as this function only gets run after (borrowed_book) is defined.
    """
    for i in range(3):
        print("Updating worksheet... \n")
        time.sleep(0.5)
    
    borrowed_worksheet = SHEET.worksheet("borrowed-books")
    borrowed_worksheet.append_row(borrowed_book)
    print("Updated successfully...")
    print("Going back to Main Menu.\n")
    let_user_choose()


def update_returned_book_worksheet(returned_book):
    """
    This function will append the data passed to it to the (returned-books) worksheet
    and a delayed print message to keep the user updated on what's happening.

    This function takes one variable named (returned_book). 
    The function only gets run after returned_book variable has been defined.
    """
    return_worksheet = SHEET.worksheet("returned-books")
    return_worksheet.append_row(returned_book)
    for e in range(3):
        print("Updating..")
        time.sleep(1)
    print("Update complete.\n")
    print("Going back to Main Menu. \n")
    let_user_choose()


def get_data():
    """
    When called, this function will grab the details needed for (borrowed-books) worksheet, Split them up
    and store them in a new variable. These details can be given to a function to append them onto the worksheet.
    """
    global borrowed_book
    print(borrow_text)
    data_text = input("Please enter your text like the example above now: \n")
    borrowed_book = data_text.split(",")
    # Calling the append() function and passing it the new variable made.
    update_borrowed_book_worksheet(borrowed_book)


def return_data():
    """
    When called, this function will grab the return details needed, Split them up and store in a new variable.
    """
    global returned_book
    print(return_message)
    return_text = input("Please enter your text like the example above now: \n")
    returned_book = return_text.split(",")

    # Calling append() fucntion to add detials to returned worksheet.
    update_returned_book_worksheet(returned_book)

# Pythons first action starts here. 
# Because this is at the bottom, Python has read all code above.
let_user_choose()