from lib.database_connection import DatabaseConnection
from lib.book_store_repository import BookRepository

connection = DatabaseConnection()
connection.connect()

connection.seed("seeds/book_store.sql")

book_store_repository = BookRepository(connection)
books = book_store_repository.all()

for book in books:
    print(f"{book.id} - {book.title} - {book.author_name}")