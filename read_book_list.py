# from . import book
# import book as book
from book import *
import csv
import pathlib


def read_book_list(file_name):
    if not pathlib.Path.is_file(pathlib.Path(file_name)):
        raise FileNotFoundError(f"{file_name} cannot be found!")

    books = []

    with open(file_name, 'r') as infile:
        reader = csv.reader(infile, delimiter=',')

        next(reader)  # skip header

        for row in reader:
            try:
                books.append(Book(BookRow(*row)))
            except:
                print(row)

    for book in books:
        print(book)


if __name__ == '__main__':
    read_book_list("College Book List.csv")
