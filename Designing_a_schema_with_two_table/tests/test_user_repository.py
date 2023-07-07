from lib.user_repository import UserRepository
from lib.user import User

def test_all(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    result = repository.all()
    assert result == [
        User(1, "kay", "kay@kaylack.net"),
        User(2, "leo", "leo@leohetsch.net")
    ]

def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    result = repository.find(2)
    assert result == User(2, "leo", "leo@leohetsch.net")


def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    repository.delete(1)
    assert repository.all() == [
        User(1, "kay", "kay@kaylack.net"),
        User(2, "leo", "leo@leohetsch.net"),
        User(3, "e", "efe.net")
    ] 

def test_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    user = User(None, "e", "efe.net")
    assert repository.delete(1) is None
    assert repository.all() == [
        User(1, "kay", "kay@kaylack.net"),
        User(2, "leo", "leo@leohetsch.net"),
        User(3, "e", "efe.net")
    ] 

def test_update(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    user = repository.find(1)
    user.email = "kay@kaylack.com"
    assert repository.update(user) is None
    assert repository.all() == [
        User(1, "kay", "kay@kaylack.net"),
        User(2, "leo", "leo@leohetsch.net"),
    ] 