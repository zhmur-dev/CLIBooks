# CLIBooks

---

### Description
A sample command-line utility for books management developed in pure Python without third-party imports except for `argparse` module from standard Python library. Works with a locally stored JSON file in 5 different modes (add, delete, find, show all, change status) followed by mandatory and optional parameters (id, title, author, year, status).  Just clone it from repository and refer to a sample session below to understand how it works. Since no third-party imports are used, you do not require to create a virtual environment for this utility.

#### Cloning CLIBooks
```
git clone https://github.com/zhmur-dev/CLIBooks.git
cd CLIBooks
```

#### Getting help
```
python3 clibooks.py -h
```

---

### Sample session

#### Showing all books
```
python3 clibooks.py show-all

{'ID': 1, 'Title': 'Learning Python (Forth Edition)', 'Author': 'Mark Lutz', 'Year': 2011, 'Status': 'В наличии'}
{'ID': 2, 'Title': '40 Algorithms Every Programmer Should Know', 'Author': 'Imran Ahmad', 'Year': 2023, 'Status': 'В наличии'}
{'ID': 3, 'Title': 'PostgreSQL 16 изнутри', 'Author': 'Егор Рогов', 'Year': 2024, 'Status': 'В наличии'}
```

#### Adding a new book
> `--title`, `--author` and `--year` are mandatory parameters
```
python3 clibooks.py add --title "My New Book" --author "Alexander Zhmurkov" --year 2024

Operation completed successfully
```

#### Deleting a book
> `--id` is a mandatory parameter.
```
python3 clibooks.py delete --id 2

Operation completed successfully
```

#### Changing a book status
> `--id` and `--status` are mandatory parameters
```
python3 clibooks.py change-status --id 3 --status 0

Operation completed successfully
```

#### Finding books with 1 parameter
> At least one of these parameters is required: `--title`, `--author`, `--year`
```
python3 clibooks.py find --year 2024

{'ID': 3, 'Title': 'PostgreSQL 16 изнутри', 'Author': 'Егор Рогов', 'Year': 2024, 'Status': 'Выдана'}
{'ID': 4, 'Title': 'My New Book', 'Author': 'Alexander Zhmurkov', 'Year': 2024, 'Status': 'В наличии'}
```

#### Finding a book with > 1 parameters and only by part of its title
> At least one of these parameters is specified: `--title`, `--author`, `--year`
```
python3 clibooks.py find --year 2024 --title "SQL"

{'ID': 3, 'Title': 'PostgreSQL 16 изнутри', 'Author': 'Егор Рогов', 'Year': 2024, 'Status': 'Выдана'}
```

#### Showing all books again after made changes
```
python3 clibooks.py show-all

{'ID': 1, 'Title': 'Learning Python (Forth Edition)', 'Author': 'Mark Lutz', 'Year': 2011, 'Status': 'В наличии'}
{'ID': 3, 'Title': 'PostgreSQL 16 изнутри', 'Author': 'Егор Рогов', 'Year': 2024, 'Status': 'Выдана'}
{'ID': 4, 'Title': 'My New Book', 'Author': 'Alexander Zhmurkov', 'Year': 2024, 'Status': 'В наличии'}
```

---

Developed with Python 3.12 by Alexander [zhmur-dev](https://github.com/zhmur-dev) Zhmurkov in 2024