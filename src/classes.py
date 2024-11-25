class Book:
    """
    The main and only class in CLIBooks.
    """
    def __init__(
            self,
            id: int,
            title: str,
            author: str,
            year: int,
            status: int
    ):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status
