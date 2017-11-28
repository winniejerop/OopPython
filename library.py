2# Class => Library
# Layers of Abstraction => display available books, to lend a book, to add a book


# Class Customer
# Layers of abstraction => request for a book, return a book

class Library:

    def __init__(self, listofBooks):
        self.availableBooks = listofBooks


    def displayAvailableBook(self):
        print()
        print("Available books.")
        for book in self.availableBooks:
            print(book)


    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("You borrowed the book.")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, not here")

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("Thanks for returning!")


class Customer:
    def requestBook(self):
        print("Enter the name of the book")
        self.book = input()
        return self.book

    def returnBook(self):
        print ("Enter name of book you are returning")
        self.book = input()
        return self.book


library = Library(["Book1", "Book2", "Book3"])
customer = Customer()
while True:
    print("1 = available, 2 = request, 3 = return, 4 = exit")
    userChoice = int(input())

    if userChoice is 1:
        library.displayAvailableBook()
    elif userChoice is 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice is 3:
        returnBook = customer.returnBook()
        library.addBook(returnBook)
    elif userChoice is 4:
        quit()
