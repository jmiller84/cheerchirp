from lib.post import Post
from datetime import datetime

"""
Post constructs with an id, title, content, and tags
"""
def test_post_constructs():
    post = Post(1, "Test Title", "Test Content", user_id= 1)
    assert post.id == 1
    assert post.title == "Test Title"
    assert post.content == "Test Content"
    assert post.user_id == 1




"""
We can format posts to strings nicely
"""
def test_posts_format_nicely():
    post = Post(1, "Test Title", "Test Content", user_id= 1)
    assert str(post) == "Post(1, Test Title, Test Content, 1)"

"""
We can compare two identical posts
And have them be equal
"""
def test_posts_are_equal():
    post1 = Post(1, "Test Title", "Test Content", user_id= 1)
    post1.created = datetime(2023,1,1)
    post2 = Post(1, "Test Title", "Test Content", user_id= 1)
    post2.created = datetime(2023,1,1)
    assert post1 == post2

"""
Test post validity
"""
def test_post_validity():
    post = Post(1, "Test Title", "Test Content", user_id= 1)
    assert post.is_valid() == True
    post = Post(1, title="", content="Test Content", user_id= 1)
    assert post.is_valid() == False
    post = Post(1, title = "Test Title", content="", user_id= 1)
    assert post.is_valid() == False
    post = Post(1, title=None, content="Test Content", user_id= 1)
    assert post.is_valid() == False
    post = Post(1, title = "Test Title", content=None, user_id= 1)
    assert post.is_valid() == False

"""
Test post generates errors
"""
def test_posts_generate_errors():
    post = Post(1, title="", content="Test Content", user_id= 1)
    assert post.generate_errors() == "Title can't be blank"
    post = Post(1, title="Test Title", content="", user_id= 1)
    assert post.generate_errors() == "Content can't be blank"
    post = Post(1, title=None, content="Test Content", user_id= 1)
    assert post.generate_errors() == "Title can't be blank"
    post = Post(1, title="Test Title", content=None, user_id= 1)
    assert post.generate_errors() == "Content can't be blank"

