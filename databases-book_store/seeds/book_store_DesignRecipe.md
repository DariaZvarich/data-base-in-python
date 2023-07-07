# Function Design Recipe: to test-drive a Book class and a BookRepository class with an all method 


## 1. Describe the Problem

As a training programmer
So that I can use extant data as arguements/attributes in Python
I want to pull data from SQL Database into a repository
and code a connection for a class in Python code to access the data

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python 
# EXAMPLE

def test_constructs_fields(mixed_words):
    """Reflects the the instance of properties

    Parameters: (list all parameters and their types)
        mixed_words: string and integers that comprise of the
        category headings (e.g. Book('Nineteen Eighty-Four', 'George Orwell'); RepositoryBook('Nineteen Eighty-Four', 'George Orwell') )

    Returns: (state the return value and its type)
        to instantiate each attribute and show equivalency (e.g. Book('Nineteen Eighty-Four', 'George Orwell'); RepositoryBook('Nineteen Eighty-Four', 'George Orwell'))

    Side effects: (state any side effects)
        This function has the side effects of:
        -the data coming from the database do not have 'id' 
        included and there is a need for manually inputting consecutive numbers
        -identical category data in the repository and the python code but the 
        system does not recognise the instance as such 
    """
    pass # Test-driving means _not_ writing any code here yet.
    

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE 
"""
Given field of information from table 
And it returns instant
"""
constructs_field_of_info == (Book(1, "Nineteen Eighty-Four', 'George Orwell")) => (book.id == "Nineteen Eighty-Four', book.author_name == 'George Orwell')

"""
Given two books that similliar, but in different places(instances)
And output - we are make them equal 
"""
test_equality 

book_1 = (Book(1, "Nineteen Eighty-Four', 'George Orwell"))
book_2 = (Book(1, "Nineteen Eighty-Four', 'George Orwell"))
 => ("book_1") == ("book_2") 

"""
Given the instances of the class in integer format and string format
Return everything in string format
"""
test_format_to_string
book = Book(1, "Doolittle", 1989, 1)
assert str(book) == "Book(1, Doolittle, 1989, 1)"

"""
When i call @all in the Book repository i get all the books back in the list
"""
test_all_books
repository.all == [] => Book(1, "Nineteen Eighty-Four', 'George Orwell")

"""
Given a lowercase word and an uppercase word with an exclamation mark
It returns a list with the uppercase word, no exclamation mark
"""
extract_uppercase("hello WORLD!") => ["WORLD"]

"""
Given an empty string
It returns an empty list
"""
extract_uppercase("") => []

"""
Given a None value
It throws an error
"""
extract_uppercase(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->