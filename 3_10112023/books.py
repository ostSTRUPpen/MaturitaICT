class Book():
    def __init__(self, name, author, year):
        self.__name = name
        self.__author = author
        self.__year = year
    def info(self):
        return f"Název knihy: {self.__name}\nAutor: {self.__author}\nYear: {self.__year}"

class Library():
    def __init__(self):
        self.__books = []
    def add_book(self, book):
        self.__books.append(book)
    def print_books(self):
        print("Knihy v systému:")
        for __book in self.__books:
            print(f"{__book.info()}\n---")

lib = Library()
lib.add_book(Book("T", "JK", 1591))

lib.print_books()

class Novel(Book):
    def __init__(self, name, author, year, info):
        super().__init__(name, author, year)
        self.__info = info
        self.__genre = "Novel"
    def info(self):
        return f"{super().info()}\nŽánr: {self.__genre}\nInfo: {self.__info}"
        
nov = Novel("G", "LU", "0045", "POG")
lib.add_book(nov)
lib.print_books()