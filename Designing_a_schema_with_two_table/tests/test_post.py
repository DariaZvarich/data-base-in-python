from lib.post import Post


"""
Constructs with an id, title, content, views, and user_id
"""

def test_constructs():
    post = Post(1, "My Title", "My Content", 2, 1)
    assert post.id == 1
    assert post.title == "My Title"
    assert post.content == "My Content"
    assert post.views == 2
    assert post.user_id == 1
    
def test_equality():
    post_1 = Post(1, "My Title", "My Content", 2, 1)
    post_2 = Post(1, "My Title", "My Content", 2, 1)
    assert post_1 == post_2
    
def test_formats():
    user = Post(1, "My Username", "My Content", 2, 1)
    assert str(post) == "Post(1, My Title, My Content , 2, 1)"