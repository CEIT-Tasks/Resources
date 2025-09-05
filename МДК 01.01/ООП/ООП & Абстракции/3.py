class Book:
    def __init__(self, name, author, year, pages):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages
        
    def changePageCount(self, pages):
        if pages > 0:
            self.pages = pages
        else:
            print("Количество страниц должно быть положительным числом")
            
    def printInfo(self):
        print(f"Title: {self.name}, Author: {self.author}, Year: {self.year}, Pages: {self.pages}")
        
class Library(Book):
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def searchBook(self, book_name):
        for book in self.books:
            if book.name == book_name:
                return book
        return None
        
    def addBook(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Можно добавлять только объекты класса Book")
            
    def printBooks(self):
        print(f"Библиотека: {self.name}")
        for book in self.books:
            print(f"Title: {book.name}, Author: {book.author}, Year: {book.year}, Pages: {book.pages}.")

book1 = Book("1984", "George Orwell", 1949, 328)
book1.printInfo()