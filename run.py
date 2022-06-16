import gspread
from google.oauth2.service_account import Credentials
import time

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

Here at Lite Library we only keep top rated books.
This is our automated system to keep track and log
what books we have, and other infomation.
We value your service and we wish you have a good
experience.

Please type the service you require.

1 = View books available.
2 = Borrow a book.
3 = Return a borrowed book.
4 = Quit the app.
"""

borrow_text = """
Hey and thanks for chooseing to borrow a book.
Please answer these questions in the format we show.
Each question must be seperated with a ',' 
Here is what you must write.

1,Enter your name: David 

2,Enter your age: 25

3,Enter your email:  david@gmail.com

4,Copys of the book are you taking: 1

5,Name of the author: JK Rowling

6,Title of the book: Harry Potter and the Goblet of Fire

7,Todays date:  14/5/2021

You should write your text like this.
David , 25 , david@gmail.com , 1 , JK Rowling , Harry potter and the Goblet of fire , 14/5/2021
"""

return_message = """
Wellcome to the return book page
Lets get started...
Please answer these questions in the format we show.
Each question must be seperated with a ',' 
Here is what you must write.

1,Enter your name: David 

2,Enter your age: 25

3,Enter your email:  david@gmail.com

4,Copys of the book are you returning: 1

5,Name of the author: JK Rowling

6,Title of the book: Harry Potter and the Goblet of Fire

7,Date of when you took the book:  14/5/2021

8,Todays date: 13/6/2021

You should write your text like this.
David , 25 , david@gmail.com , 1 , JK Rowling , Harry potter and the Goblet of fire , 14/5/2021 , 13/6/2021
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
            #time.sleep(0.5)
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
        print("Goodbye, See you next time! \n")
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

    for i in range(3):
        print("Updateing worksheet... \n")
        time.sleep(0.5)
    
    return_worksheet = SHEET.worksheet("returned-books")
    return_worksheet.append_row(returned_book)
    print("Updated sucsesfully...")
    print("placeholder for message to do with returns.")
    print("Now going back to main menu.")
    let_user_choose()

let_user_choose()