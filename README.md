# Python 101

A small collection of standalone Python practice scripts. The examples cover basic output and types, drawing a character grid from coordinates, reading an HTML table, and connecting to MySQL.

## Files

- [`hello.py`](hello.py) prints a basic greeting (`hellow world!`). It is a minimal example of running a Python script and using `print()`.
- [`variables.py`](variables.py) assigns values to variables, converts values with `str()`, `int()`, and `float()`, prints them, and displays their types with `type()`.
- [`code.py`](code.py) stores characters with `(x, y, character)` coordinates, builds a two-dimensional grid, and prints the resulting character-art pattern. It is a small example of lists, tuples, comprehensions, loops, and indexing.
- [`code1.py`](code1.py) uses a larger set of `(x, y, character)` coordinates to build and print a wider character-art pattern. It follows the same grid-building approach as `code.py`.
- [`read-page.py`](read-page.py) downloads a published Google Docs page, parses its first HTML table with BeautifulSoup, and prints the rows as formatted JSON. It requires network access and the `requests` and `beautifulsoup4` packages. The `table_class` variable is currently not used; the script selects the first table on the page.
- [`mysql_connection.py`](mysql_connection.py) connects to a MySQL server on `localhost`, prints the connection, runs `SHOW DATABASES`, and prints the results. It requires a running local MySQL server, the `mysql-connector-python` package, and connection settings that match your server.

## Running the examples

Run a script from the repository directory with Python:

```powershell
py hello.py
```

Replace `hello.py` with the script you want to run. For example, `py code.py` prints its grid and `py variables.py` prints the values and their types.

Install the scraper dependencies when using `read-page.py`:

```powershell
py -m pip install requests beautifulsoup4
```

Install the MySQL connector when using `mysql_connection.py`:

```powershell
py -m pip install mysql-connector-python
```

Before running the MySQL example, make sure MySQL is running and update the host, username, and password in the script for your local configuration. Avoid committing real credentials to the repository.
