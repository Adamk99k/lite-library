# Welcome to Lite Library.

## Hello there and welcome to my first project with Python.

## Wan't to check out my deployed Project? Here it is... [Lite Library](https://lite-library.herokuapp.com/)
<br>

The aim of my site was to act as a Automated Application for a library named 'Lite Library'<br> The app runs like this..<br>
The App starts and greets the user. The user then has a choice of options to pick from. Users can choose to view all books available in the Lite Library stock list, Once the user has seen the books available they then can decide if they would want to borrow a book or not.
Users that have borrowed a book also have an option to return the book via option '3' on the main menu, Both of these actions 1,Borrow a book 2, Return a book both do the same thing, they add the data given from the user to our external worksheet.
I wanted to make this application as simple as posible for the user to use to prevent users getiing overwelmed.<br>
The target audience is really anybody from all ages who would like to use Lite Library service.<br>
The main aim of this application was to make a simple way for a library to add books,users data and other information to a external worksheet automatically. In this case the external worksheet is google Spreadsheet.

# Flow chart.
![flowChart](/lite-library-flowchart.png)

# Features
* Main Menu. <br> The main function in this application acts as the main menu for the user.<br>This Main Menu is the core navigation tool used to get the user to and from the correct service offered. Here is how it is structured.<br>The main menu starts and greets the user.<br>Users then have an option too either...<br>1 = View books available.<br>
2 = Borrow a book.<br>
3 = Return a borrowed book.<br>
4 = Quit the app.<br> This structure makes it very simple and easy for users to select what they want to do and redirects them to the right place

* Option One: View all books. <br> This option simply accesses the google spreadsheet and prints out all books in that sheet for the user to see.

* Option Two: Borrow a book. <br> This option will print out the instructions and rules for the user to add a string of text in the correct way, Once this data has been received the program will then split the string up and store this data in a new variable. The program then calls to another function and adds the new variable as the argument to append the data to the external worksheet. Users are kept up-to-date with the process via print messages. Once users data has been added successfully to the spreadsheet the program restarts from the beginning.

* Option Three: Return a borrowed book. <br> This option acts the same way as option two. The only differences are that users will have to add slightly different information the from option Two. This data is processed the same way as option Two, Split string up, Store in new variable, Send that variable to append function. <br> That adds the data to a separate sheet on the external worksheet named 'returned-books'.

* Option Four: Quit app. <br> This option simple calls the quit() function built in and quits the app.

# Testing


# Deployment
This project was deployed using Code Institutes terminal for Heroku.<br>
<br>
Steps to deploy:
<br>
Fork or clone this repository.<br>
Create a new Heroku App.<br>
Set the buildbacks to Python and NodeJS in that order.<br>
Link the Heroku app to the repository via GitHub.<br>
Click on Deploy. <br>



# Features not implemented 


# Technologies used
## Languages.<br>
* Python programming language is the main language used for this system.<br>
## Frameworks and tools. <br>
* GitHub - Used to store my code in a remote repository.<br>
* GitPod - Used to edit my code and push to GitHub.<br>
* Lucid Chart - Used to create a mock up flow chart.<br>
* Google Sheets - Used to store data outside of this Application.<br>
* Google Cloud Platform - Used for authentications, Permissions to the google services, google auth and all sheets. <br>
* Heroku Platform - Used to deploy this project into a live environment.


# Credits