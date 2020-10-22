from collections import namedtuple

BookRow = namedtuple("BookRow", ["title", "selling", "condition", "paperback", "edition", "int_ed", "isbn_10",
                                 "isbn_13", "isbn_other", "price"])


class Book():
    def __init__(self, book_info: BookRow):
        self.title = book_info.title
        self.selling = book_info.selling
        self.condition = book_info.condition
        self.paperback = book_info.paperback
        self.edition = book_info.edition
        self.int_ed = book_info.int_ed
        self.isbn_10 = book_info.isbn_10
        self.isbn_13 = book_info.isbn_13
        self.isbn_other = book_info.isbn_other
        self.price = []

    def __repr__(self):
        return self.title
