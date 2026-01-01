import sqlite3

class Book():
    def __init__(self,name,writer,publisher,book_type,oppression):
        self.name=name
        self.writer=writer
        self.publisher=publisher
        self.book_type=book_type
        self.oppression=oppression

    def __str__(self):
        return ("Name: {}\n"
                "Writer: {}\n"
                "Publisher: {}\n"
                "book_type: {}\n"
                "oppression: {}").format(self.name, self.writer, self.publisher, self.book_type, self.oppression)

class Library():
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.connection = sqlite3.connect('library.db')

        self.cursor = self.connection.cursor()

        query = "CREATE TABLE IF NOT EXISTS books(name TEXT, writer TEXT, publisher TEXT, book_type TEXT, oppression INT)"

        self.cursor.execute(query) #sorguyu çalıştırdık

        self.connection.commit() #burada ise sorguyu db de etkili hale getirdik

    def close_connection(self):
        self.connection.close()

    def show_books(self):
        query = "SELECT * FROM books"
        self.cursor.execute(query)
        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("No books yet on library.")

        else:
            for i in books:
                book = Book(i[0],i[1],i[2],i[3],i[4])
                print(book)

    def inquire_book(self,name):
        query = "SELECT * FROM books WHERE name = ?"
        self.cursor.execute(query,(name,))
        books = self.cursor.fetchall()
        if (len(books) == 0):
            print("No book yet on library.")
        else:
            book = Book(books[0][0],books[0][1],books[0][2],books[0][3],books[0][4])
            print(book)

    def add_book(self, book):
        query = "INSERT INTO books VALUES(?,?,?,?,?)"
        self.cursor.execute(query, (
            book.name,
            book.writer,
            book.publisher,
            book.book_type,
            book.oppression
        ))
        self.connection.commit()

    def delete_book(self,name):
        query = "DELETE FROM books WHERE name = ?"
        self.cursor.execute(query,(name,))
        self.connection.commit()

    def upgrade_oppression(self,name):
        query = "Select * FROM books WHERE name = ?"
        self.cursor.execute(query,(name,))

        books = self.cursor.fetchall()
        if (len(books) == 0):
            print("No book yet on library.")
        else:
            oppression = books[0][4]
            oppression += 1

            query2 = "UPDATE books SET oppression = ? WHERE name = ?"
            self.cursor.execute(query2,(oppression,name))
            self.connection.commit()
