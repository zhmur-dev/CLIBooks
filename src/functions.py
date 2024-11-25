from src.classes import Book
from src.const import STATUSES
from src.literals import (
    MISSING_PARAMETERS_MESSAGE, NOT_FOUND_MESSAGE, SUCCESS_MESSAGE
)


def json_file_to_list() -> list[dict]:
    """
    Auxiliary function that converts data from JSON file to dictionary entries
    and returns them as a list of dictionaries.
    """
    with open('data/books.json', 'r') as file:
        file_content = file.read()
        if file_content == '':
            return [{}]
        return eval(file_content.replace('\n', ''))


def get_last_book_id():
    """
    Auxiliary function that return the ID of last book in JSON file.
    """
    books = json_file_to_list()
    if books != [{}]:
        return books[-1]['id']
    return 0


def add_book_instance(
        title: str,
        author: str,
        year: int,
        id: int = None,
        status: int = 1
) -> Book:
    """
    Auxiliary function that creates a single instance of Book class
    based on received parameters.
    """
    if id is None:
        id = get_last_book_id() + 1
    return Book(id=id, title=title, author=author, year=year, status=status)


def bulk_add_book_instances(books: list[dict]) -> list[Book]:
    """
    Auxiliary function that creates multiple instances of Book class
    based on received list of dictionaries and returns them as a list.
    """
    if books == [{}]:
        return []
    added_books: list[Book] = []
    for book in books:
        added_books.append(
            add_book_instance(
                id=book['id'],
                title=book['title'],
                author=book['author'],
                year=book['year'],
                status=book['status'],
            )
        )
    return added_books


def collect_book(book: Book) -> dict:
    """
    Auxiliary function that converts values from a specific Book instance
    into a dictionary entry and returns such an entry.
    """
    return {
            'ID': book.id,
            'Title': book.title,
            'Author': book.author,
            'Year': book.year,
            'Status': STATUSES[book.status]
    }


def get_books_from_file() -> list[Book]:
    """
    Auxiliary function that creates multiple instances of Book class
    based on the parameters specified in JSON file
    and returns them as a list of instances.
    """
    return bulk_add_book_instances(json_file_to_list())


def save_books_to_file(books):
    """
    Auxiliary function that re-writes the content of a JSON file
    with the current values of Book instances.
    """
    file_content: list[str] = []
    for book in books:
        file_content.append('{\n'),
        file_content.append(f'   "id": {book.id},\n')
        file_content.append(f'   "title": "{book.title}",\n')
        file_content.append(f'   "author": "{book.author}",\n')
        file_content.append(f'   "year": {book.year},\n')
        file_content.append(f'   "status": {book.status}\n')
        file_content.append('},\n')
    with open('data/books.json', 'w') as file:
        file.writelines(file_content)


def user_add_book(args):
    """
    User-interface function that adds a new book
    and saves the updated JSON file.
    Title, Author and Year are mandatory parameters.
    """
    if not args.title or not args.author or not args.year:
        print(MISSING_PARAMETERS_MESSAGE)
        return
    books = get_books_from_file()
    books.append(add_book_instance(
        title=args.title, author=args.author, year=args.year
    ))
    save_books_to_file(books)
    print(SUCCESS_MESSAGE)


def user_delete_book(args):
    """
    User-interface function that deletes a book
    and saves the updated JSON file.
    Book ID is mandatory parameter.
    """
    if not args.id:
        print(MISSING_PARAMETERS_MESSAGE)
        return
    books = get_books_from_file()
    for book in books:
        if book.id == args.id:
            books.remove(book)
            save_books_to_file(books)
            print(SUCCESS_MESSAGE)
            return
    print(NOT_FOUND_MESSAGE)


def user_find_book(args):
    """
    User-interface function that searches for a book
    according to one or more provided parameters:
    Title, Author, Year (at least one parameter is required.)
    """
    if not args.title and not args.author and not args.year:
        print(MISSING_PARAMETERS_MESSAGE)
        return
    found_books = []
    for book in get_books_from_file():
        if (
            args.title is not None and book.title.find(args.title) == -1
            or args.author is not None and book.author.find(args.author) == -1
            or args.year is not None and book.year != args.year
        ):
            continue
        else:
            found_books.append(collect_book(book))
            print(found_books[-1])
    if len(found_books) == 0:
        print(NOT_FOUND_MESSAGE)
    return found_books


def user_get_books(args):
    """
    User-interface function that returns all books stored in JSON file.
    """
    books: list[dict] = []
    for book in get_books_from_file():
        books.append(collect_book(book))
        print(books[-1])
    return books


def user_change_book_status(args):
    """
    User-interface function that changes status of the book
    and saves the updated JSON file.
    Book ID and Status code (0 or 1) are mandatory parameters.
    """
    if args.id is None or args.status is None:
        print(MISSING_PARAMETERS_MESSAGE)
        return
    books = get_books_from_file()
    for book in books:
        if book.id == args.id:
            book.status = args.status
            save_books_to_file(books)
            print(SUCCESS_MESSAGE)
            return
    print(NOT_FOUND_MESSAGE)


MODE_TO_FUNCTION: dict[str:object] = {
    'add': user_add_book,
    'delete': user_delete_book,
    'find': user_find_book,
    'show-all': user_get_books,
    'change-status': user_change_book_status
}
