# zad1

class Student:
    name: str
    marks: int

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if self.marks > 50:
            return True
        else:
            return False

    def __str__(self):
        return f'Imie: {self.name}'


student_1 = Student("student_1", 60)

student_2 = Student("student_2", 30)

print(student_1.is_passed())
print(student_2.is_passed())

# zad2

# class_1 klasa opisujaca biblioteke
from datetime import date


class Library:
    city: str
    street: str
    zip_code: str
    open_hours: str
    phone: str

    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str) -> None:
        self.city = city
        self.zip_code = zip_code
        self.street = street
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Biblioteka w {self.city} na ulicy {self.street}. Jej numer to: {self.zip_code}. Godziny otwarcia: {self.open_hours}. Kontakt: {self.phone}'


# class_2 klasa opisująca pracownika biblioteki

class Employee:
    first_name: str
    last_name: str
    hire_date: date
    birth_date: date
    city: str
    street: str
    zip_code: str
    phone: str

    def __init__(self, first_name: str, last_name: str, hire_date: date, birthdate: date, city: str, street: str,
                 zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.zip_code = zip_code
        self.hire_date = hire_date
        self.birth_date = birthdate
        self.phone = phone
        self.street = street

    def __str__(self):
        return f'Dane pracownika: imie: {self.first_name}, nazwisko: {self.last_name}, data zatrudnienia: {self.hire_date}, data urodzenia: {self.birth_date}, miasto: {self.city}, ulica: {self.street}, kod: {self.zip_code}, telefon: {self.phone} '


# class_3 klasa opisujaca ksiązek

class Book:
    library: Library
    public_date: date
    author_name: str
    author_surname: str
    number_of_pages: int

    def __init__(self, library: Library, public_date: date, author_name: str, author_surname: str,
                 number_of_pages: int):
        self.library = library
        self.public_date = public_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Książka znajduje sie z bibliotece: {self.library}, data publikacji:{self.public_date}, autor: {self.author_name} {self.author_surname}, liczba stron: {self.number_of_pages}'


# class_4 klasa opisujaca zamówienie

class Order:
    employee: Employee
    student: Student
    books: Book
    order_date: date

    def __init__(self, employee: Employee, student: Student, books: Book, order_date: date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Zamówienie: pracownik wydajacy: {self.employee}, student: {self.student}, książka: {self.books}, data wypożyczenia: {self.order_date}.'


biblioteka_1 = Library("Zabrze", "Wolności", "1234", "8:00-16:00", "111-222-333")
biblioteka_2 = Library("Rybnik", "Porzeczkowa", "1235", "8:30-16:30", "123-456-789")

book_1 = Book(biblioteka_1, date(1997, 10, 10), "Adam", "Mickiewicz", 239)
book_2 = Book(biblioteka_1, date(1986, 10, 2), "Juliusz", "Słowacki", 596)
book_3 = Book(biblioteka_2, date(2010, 12, 27), "Nicholas", "Sparks", 432)
book_4 = Book(biblioteka_2, date(2001, 5, 30), "Regina", "Brett", 102)
book_5 = Book(biblioteka_2, date(1991, 4, 23), "Karol", "Miarka", 123)

employee_1 = Employee("Kamil", "Nowak", date(2021, 10, 27), date(1997, 5, 9), "Katowice", "Chorzowska", "1234",
                      "123-213-321")
employee_2 = Employee("Julia", "Kowalska", date(2012, 12, 12), date(1997, 9, 29), "Rybnik", "Rybnicka", "1237",
                      "657-342-841")
employee_3 = Employee("Pola", "Kwiatkowska", date(2012, 3, 5), date(1994, 8, 12), "Gliwice", "Główna", "1233",
                      "567-297-323")

student_1 = Student("Jan", 0)
student_2 = Student("Adam", 0)
student_3 = Student("Justyna", 0)

order_1 = Order(employee_1, student_1, book_4, date(2020, 9, 19))
order_2 = Order(employee_2, student_2, book_1, date(2021, 1, 31))

print(order_1)
print(order_2)


# zad3

class Property:
    area: str
    rooms: int
    price: float
    address: str

    def __init__(self, area: str, rooms: int, price: float, address: str) -> None:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f'Property: {self.area}, {self.rooms}, {self.price}, {self.address}'


class House(Property):
    plot: int

    def __init__(self, area: str, rooms: int, price: float, address: str, plot: int):
        Property.__init__(self, area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'Dom: {self.area}, liczba pokoi: {self.rooms}, cena: {self.price}, adres: {self.address}, plot: {self.plot} '


class Flat(Property):
    floor: int

    def __init__(self, area: str, rooms: int, price: float, address: str, floor: int):
        Property.__init__(self, area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Mieszkanie: {self.area}, {self.rooms}, {self.price}, {self.address}, {self.floor}'


dom = House('Bliźniak', 6, 237.40, 'Adres_1', 250)
mieszkanie = Flat('Kamienica', 2, 30.1, 'Adres_mieszkania', 40)
print(dom)
print(mieszkanie)
