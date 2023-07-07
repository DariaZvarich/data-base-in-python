from lib.user import User

"""
Constructs with a username and an email
"""

def test_constructs():
    user = User(1, "My Username", "My Email")
    assert user.id == 1
    assert user.username == "My Username"
    assert user.email == "My Email"
    
def test_equality():
    user_1 = User(1, "My Username", "My Email")
    user_2 = User(1, "My Username", "My Email")
    assert user_1 == user_2
    
def test_formats():
    user = User(1, "My Username", "My Email")
    assert str(user) == ""