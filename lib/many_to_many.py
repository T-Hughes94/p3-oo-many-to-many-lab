class Author:
    all_authors = []

    def __init__(self, name):
        self._name = None
        self.name = name
        self.contracts_list = []  # Initialize a list to store contracts
        Author.all_authors.append(self)

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("Not a valid name")

    name = property(get_name, set_name)

    def contracts(self):
        return self.contracts_list

    def books(self):
        return [contract.book for contract in self.contracts_list]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book) or not isinstance(date, str) or not isinstance(royalties, int):
            raise ValueError("Invalid contract parameters")
        contract = Contract(self, book, date, royalties)
        self.contracts_list.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts_list)


class Book:
    all_books = []

    def __init__(self, title):
        self._title = None
        self.title = title
        self.contracts_list = []  # Initialize a list to store contracts
        Book.all_books.append(self)

    def get_title(self):
        return self._title

    def set_title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise ValueError('Title must be a string')

    title = property(get_title, set_title)

    def contracts(self):
        return self.contracts_list

    def authors(self):
        return [contract.author for contract in self.contracts_list]


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    def get_author(self):
        return self._author

    def set_author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise ValueError("Not a valid author")

    def get_book(self):
        return self._book

    def set_book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise ValueError("Not a valid book")

    def get_date(self):
        return self._date

    def set_date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise ValueError("Not a valid date")

    def get_royalties(self):
        return self._royalties

    def set_royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise ValueError("Not a valid input")

    royalties = property(get_royalties, set_royalties)
    author = property(get_author, set_author)
    book = property(get_book, set_book)
    date = property(get_date, set_date)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]



