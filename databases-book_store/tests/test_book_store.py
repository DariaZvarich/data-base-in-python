from lib.book_store import BookStore

"""
BookStore constructs with an id, title, and author_name
"""
def test_book_constructs(): 
    book = BookStore(1, "Nineteen Eighty-Four", "George Orwell")
    assert book.id == 1
    assert book.title == "Nineteen Eighty-Four"
    assert book.author_name == "George Orwell"

def test_book_format_nicely():
    book = BookStore(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert str(book) == "BookStore(1, Nineteen Eighty-Four, George Orwell)"


        