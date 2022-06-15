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


menu_message = """ 
Wellcome to Lite Library.
placeholder text

random text

Please select the service you require.
1 = View books available.
2 = Borrow a book.
3 = Return a borrowed book.
4 = Quit the app.
"""

borrow_text = """
Please enter these details they way we show you.
Each question must be seperated with a ',' 
Here is what you must write.

Enter your name: David 

Enter your age: 25

Enter your email:  david@gmail.com

Copys of the book are you taking: 1

name of the author: JK Rowling

Title of the book: Harry Potter and the Goblet of Fire

Todays date:  14/5/2021


You should type your text like this...

David , 25 , david@gmail.com , 1 , JK Rowling , Harry potter and the Goblet of fire , 14'5'2021
"""


def let_user_choose():
    """
    Gets user input for what option they want to pick. 
    either view all books available or borrow a book
    or return a borrowed book
    """

    print(menu_message)


    while True:
        try:
            global user_option
            user_option = int(input("Enter 1, 2, 3, or 4 now: \n"))
            if user_option >= 5:
                print("Number to high. Try again")
                continue
            elif user_option <= 0:
                print("Number to low. Try again.")
                continue
            print(f'Your choice was {user_option}')
            break
        except ValueError:
            print("Please only choose from 1 / 2 / 3 or 4.")
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
        get_data()
    elif user_option == 3:
        #fucntioon to store the return details
        pass
    elif user_option == 4:
        print("Goodbye, See you next time! \n")
        quit()


# func to grab borrowed books details
def get_data():
    global borrowed_book
    print(borrow_text)

    data_text = input("Please enter your text like the example above now: \n")
    borrowed_book = data_text.split(",")


def return_data():
    print("You have choose the option to return a book. \n")

#def update_worksheet with data user submited for borrowed
def update_borrowed_book_worksheet(borrowed_book):
    """
    Takes the taken data for borrowed book and adds to worksheet
    """
    print("Updateing worksheet... \n")
    borrowed_worksheet = SHEET.worksheet("borrowed-books")
    borrowed_worksheet.append_row(borrowed_book)
    print("Updated sucsesfully...")
    print("RULES FOR BORROWEING.")
    print("Now going back to main menu.")
    let_user_choose()



let_user_choose()
update_borrowed_book_worksheet(borrowed_book)
