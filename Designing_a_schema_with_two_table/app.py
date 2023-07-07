from lib.database_connection import DatabaseConnection

from lib.user_repository import UserRepository
from lib.post_repository import PostRepository

connection = DatabaseConnection
connection.connect()
user_repository = UserRepository(connection)
post_repository = PostRepository(connection)

for user in user_repository.all():
    print(user)
    
for post in post_repository.all():
    print(post)
