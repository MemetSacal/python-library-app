from Sınıfların_Tasarlanması import *
import time

print("**************************\n"
      "Welcome to Library App\n"
      "Transactions\n"
      "1.Show Books\n"
      "2.Inquire Books\n"
      "3.Add Books\n"
      "4.Delete Books\n"
      "5.Upgrade Oppression\n"
      "Press 'q' to exit\n"
      "**************************")

library = Library()

while True:
    query = input("Enter the action you wish to perform: ")

    if query == "q":
        print("Goodbye")
        break

    elif query == "1":
        library.show_books()

    elif query == "2":
        name = input("The book you want to query: ")
        print("The book is being researched please wait...")
        time.sleep(1)
        book = library.inquire_book(name)

    elif query == "3":
        name = input("Book Name: ")
        writer = input("Book Writer: ")
        publisher = input("Publisher: ")
        book_type = input("Type of book: ")
        oppression = int(input("Oppression: "))

        new_book = Book(name,writer, publisher, book_type, oppression)

        print("The book is being added to the library please wait...")
        time.sleep(1)

        library.add_book(new_book)

    elif query == "4":
        name = input("Which book do you want to delete: ")
        answer = input("Are you sure? Y/N: ")
        if answer == "Y":
            print("The book is being deleted please wait...")
            time.sleep(1)
            library.delete_book(name)
            print("The book is deleted")

    elif query == "5":
        name = input("Book Name: ")
        print("Oppressions upgrade please wait...")
        time.sleep(1)
        library.upgrade_oppression(name)
        print("Oppressions upgraded")
    else:
        print("You entered an invalid transaction.")
        print("Please enter a valid transaction.")