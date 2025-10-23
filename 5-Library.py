class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.__isbn = isbn
        self.available = True

    def display_info(self):
        print(f"{self.title} by {self.author} | ISBN: {self.__isbn} | Available: {self.available}")


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.__member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book.title)
            book.available = False
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is not available")

    def return_book(self, book):
        if book.title in self.borrowed_books:
            self.borrowed_books.remove(book.title)
            book.available = True
            print(f"{self.name} returned {book.title}")


class StaffMember(Member):
    def __init__(self, name, member_id, staff_id):
        super().__init__(name, member_id)
        self.staff_id = staff_id

    def add_book(self, library, title, author, isbn):
        new_book = Book(title, author, isbn)
        library.append(new_book)
        print(f"{self.name} added {title} to the library")


# ======= Test the system =======
library = []

# Add books
book1 = Book("Python", "John", "111")
book2 = Book("OOP", "Sara", "222")
library.extend([book1, book2])

# Create member and staff
m1 = Member("Ali", "M01")
s1 = StaffMember("Hossam", "M02", "S01")

# Display books
print("\nLibrary Books:")
for b in library:
    b.display_info()

# Borrow and return
m1.borrow_book(book1)
m1.return_book(book1)

# Add new book by staff
s1.add_book(library, "Data Science", "Ahmed", "333")

print("\nUpdated Library:")
for b in library:
    b.display_info()

