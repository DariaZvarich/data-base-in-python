from lib.post_repository import PostRepository
from lib.post import Post

def test_all(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    result = repository.all()
    assert result == [
        Post("My Title 1", "My Content 1", 0, 1),
        Post("My Title 2", "My Content 2", 0, 2)
    ]

def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    result = repository.find(2)
    assert result == Post(2, "My Title 2", "My Content 2", 0, 2)


def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    post = Post(None, "My Title 3", "My Content 3", 1, 1)
    assert repository.create(post) is None 
    assert repository.all() == [
        Post("My Title 1", "My Content 1", 0, 1),
        Post("My Title 2", "My Content 2", 0, 2),
        Post(None, "My Title 3", "My Content 3", 1, 1)
    ] 

def test_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    user = User(None, "e", "efe.net")
    assert repository.delete(1) is None
    assert repository.all() == [
        Post("My Title 2", "My Content 2", 0, 2),
    ] 

def test_update(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    post = repository.find(1)
    post.title = "Fancy New Title"
    assert repository.update(post) is None
    assert repository.all() == [
        Post("Fancy New Title", "My Content 1", 0, 1),
        Post("My Title 2", "My Content 2", 0, 2),
    ] 