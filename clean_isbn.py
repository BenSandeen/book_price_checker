import isbnlib

def clean_isbn(isbn: str) -> str:
    """Cleans ISBN and formats it as ISBN 13

    :param isbn: ISBN 10 or ISBN 13
    :return:     Cleaned ISBN, formatted to ISBN 13 and with hyphens stripped out
    """
    if isbnlib.notisbn(isbn):
        raise ValueError(f"{isbn} is not a valid ISBN")

    return isbnlib.to_isbn13(isbn)


if __name__ == "__main__":
    print(clean_isbn("978-0-521-52927-3"))
    try:
        clean_isbn("123-1234-1234")
    except Exception:
        pass  # We expect an exception here, so it's all good!  :D