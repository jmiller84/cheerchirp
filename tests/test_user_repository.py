from lib.user_repository import UserRepository
from lib.user import User
import hashlib

"""
When we call UserRepository#all
We get a list of User objects reflecting the seed data.
"""
def test_get_all_users(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/cheerchirp.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new UserRepository

    users = repository.all() # Get all users

    # Assert on the results
    assert users == [
            User(1, 'jmiller84', 'password123!', 'jmiller@hotmail.com', 'Joe', 'Miller'),
            User(2, 'alexm_2023', 'London123', 'alexm@hotmail.com', 'Alex', 'Martin')
    ]

"""
When we call UserRepository#find_by_username
We get a single User object reflecting the seed data.
"""
def test_get_single_user(db_connection):
    db_connection.seed("seeds/cheerchirp.sql")
    repository = UserRepository(db_connection)

    user = repository.find_by_username('jmiller84')
    assert user == User(1, 'jmiller84', 'password123!', 'jmiller@hotmail.com', 'Joe', 'Miller')

"""
When we call UserRepository#create
We get a new record in the database.
"""
def test_create_user(db_connection):
    db_connection.seed("seeds/cheerchirp.sql")
    repository = UserRepository(db_connection)

    repository.create(User(None, "TestUser", "password123!", "test@hotmail.com", "tester", "testman"))
    new_user_password = "password123!".encode("utf-8")
    new_user_password = hashlib.sha256(new_user_password).hexdigest()

    result = repository.all()
    assert result == [
        User(1, 'jmiller84', 'password123!', 'jmiller@hotmail.com', 'Joe', 'Miller'),
        User(2, 'alexm_2023', 'London123', 'alexm@hotmail.com', 'Alex', 'Martin'),
        User(3, "TestUser", new_user_password, "test@hotmail.com", "tester", "testman")
    ]

"""
Test UserRepository #password_is_valid
"""
def test_password_is_valid(db_connection):
    db_connection.seed("seeds/cheerchirp.sql")
    repository = UserRepository(db_connection)

    assert repository.password_is_valid("1234567!") == True
    assert repository.password_is_valid("123456!") == False
    assert repository.password_is_valid("12345678") == False
