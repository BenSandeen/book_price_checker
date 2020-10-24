import urllib.request
import clean_isbn
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz

def search_for_item(title: str, isbn: str):
    url = f"https://www.ebay.com/sch/i.html?_nkw={isbn}"

    r = urllib.request.urlopen(url)
    if r.code != 200:
        raise ConnectionError(f"Couldn't retrieve webpage")

    br = BeautifulSoup(r.read(), "html.parser")

    # # titles = br.find_all("h3", "s-item__title")
    # titles = br.select(".s-item__title")
    #
    # # Just use the first title listing, because its parent will also be the parent
    # books = [book.parents for book in titles[0]]
    #
    # # Get list of titles
    # title_list = list(br.find_all('h3', 's-item__title'))
    #
    # # Make sure titles match title of the book we're trying to sell
    #
    #
    # book_list_common_ancestor = list(list(list(list(list(title_list[0].parents)[0].parents)[0].parents)[0].parents)[0].parents)
    #
    # prices = list(book_list_common_ancestor[0].find_all('span', 's-item__price'))

    book_listings = list(br.find_all('li', "s-item s-item--watch-at-corner"))

    # TODO: Do some sort of fuzzy title matching
    for book in book_listings:
        # if title not in book.find('h3', 's-item__title').contents[0]:
        if fuzz.ratio(title, book.find('h3', 's-item__title').contents[0]) < 0.7:
            book_listings.remove(book)
            print(f"Removing book {book.find('h3', 's-item__title').contents[0]} from results")

    return list(book.find('span', 's-item__price') for book in book_listings)


if __name__ == "__main__":
    print(*search_for_item("Astronomy: A Physical Perspective", clean_isbn.clean_isbn("978-0-521-52927-3")))
