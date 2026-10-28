class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student {self.name}"


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Biblioteka w miescie {self.city} ({self.street})"


class Employee:
    def __init__(
        self,
        first_name,
        last_name,
        hire_date,
        birth_date,
        city,
        street,
        zip_code,
        phone,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Pracownik {self.first_name}"
            f"{self.last_name} zatrudniony od {self.hire_date}"
            )


class Book:
    def __init__(
        self,
        library,
        publication_date,
        author_name,
        author_surname,
        number_of_pages
    ):
        self.library =
        library
        self.publication_date =
        publication_date
        self.author_name =
        author_name
        self.author_surname =
        author_surname
        self.number_of_pages =
        number_of_pages

    def __str__(self):
        return (
            f"Ksiazka autorstwa {self.author_name} "
            f"{self.author_surname} z [{self.library}]"
            )


class Order:
    def __init__
    (
        self,
        employee,
        student,
        books,
        order_date
    ):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n  - ".
        join([str(b) for b in self.books])
        return (
            f"Zamowienie z dnia {self.order_date}\n"
            f"  Obslugujący: {self.employee}\n"
            f"  Zamawiający: {self.student}\n"
            f"  Ksiazki:\n  - {books_str}"
        )


lib1 = Library(
    "Warszawa",
    "Marszalkowska 10",
    "00-001",
    "8:00-18:00",
    "123456789"
    )
lib2 = Library(
    "Krakow",
    "Florianska 5",
    "30-001",
    "9:00-17:00",
    "987654321"
    )

emp1 = Employee(
    "Jan",
    "Kowalski",
    "2020-01-15",
    "1990-05-12",
    "Warszawa",
    "Prosta 1",
    "00-002",
    "111222333",
)
emp2 = Employee(
    "Anna",
    "Nowak",
    "2021-03-01",
    "1992-08-22",
    "Krakow",
    "Dluga 12",
    "30-002",
    "444555666",
)
emp3 = Employee(
    "Piotr",
    "Wisniewski",
    "2019-11-10",
    "1985-02-30",
    "Warszawa",
    "Miodowa 3",
    "00-003",
    "777888999",
)

std1 = Student("Michal Zielinski")
std2 = Student("Kasia Kaminska")
std3 = Student("Tomek Lewandowski")

book1 = Book(lib1, "1954", "J.R.R.", "Tolkien", 423)
book2 = Book(lib1, "1949", "George", "Orwell", 328)
book3 = Book(lib2, "1961", "Stanislaw", "Lem", 204)
book4 = Book(lib2, "1905", "Henryk", "Sienkiewicz", 560)
book5 = Book(lib1, "1997", "J.K.", "Rowling", 223)

order1 = Order(emp1, std1, [book1, book2], "2023-10-25")
order2 = Order(emp2, std2, [book3, book4, book5], "2023-10-26")

print(order1)
print("-" * 50)
print(order2)
