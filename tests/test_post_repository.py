from lib.post_repository import PostRepository
from lib.post import Post

"""
When we call PostRepository#all
We get an empty list
"""
def test_get_all_posts(db_connection):
    db_connection.seed("seeds/cheerchirp.sql") 
    repository = PostRepository(db_connection)
    posts = repository.all()

    assert posts == [
        Post(1, 'Test Title', 'Test Content', 1),
        Post(2, 'Test Post', 'Test Post Content', 2),
    ]

"""
When we call PostRepository#create
We see the post reflected in #all
"""
def test_create_post(db_connection):
    db_connection.seed("seeds/cheerchirp.sql") 
    repository = PostRepository(db_connection)
    post = Post(3, "Test Title", "Test Content", 1)
    created_post = repository.create(post)
    assert created_post == Post(3, "Test Title", "Test Content", 1)

    result = repository.all()
    assert result == [
        Post(1, 'Test Title', 'Test Content', 1),
        Post(2, 'Test Post', 'Test Post Content', 2),
        Post(3, "Test Title", "Test Content", 1)
    ]

