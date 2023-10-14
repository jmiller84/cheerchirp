from lib.user import User

"""
User constructs with an id, title, content, and tags
"""
def test_user_constructs():
    user = User(1, 'jmiller84', 'password123!', 'jmiller@hotmail.com', 'Joe', 'Miller')
    assert user.id == 1
    assert user.username == "jmiller84"
    assert user.password == "password123!"
    assert user.email == "jmiller@hotmail.com"
    assert user.first_name == "Joe"
    assert user.surname == "Miller"


"""
We can format users to strings nicely
"""
def test_users_format_nicely():
    user = User(1, 'jmiller84', 'password123!', 'jmiller@hotmail.com', 'Joe', 'Miller')
    assert str(user) == "User(1, jmiller84, Joe, Miller)"

"""
We can compare two identical users
And have them be equal
"""
def test_users_are_equal():
    user1 = User(1, 'jmiller84', 'password123!', 'jmiller@hotmail.com', 'Joe', 'Miller')
    user2 = User(1, 'jmiller84', 'password123!', 'jmiller@hotmail.com', 'Joe', 'Miller')
    assert user1 == user2

"""
Test user validity
"""
def test_user_validity():
    user = User(1, 'jmiller84', 'password123!', 'jmiller@hotmail.com', 'Joe', 'Miller')
    assert user.form_is_valid() == True
    user = User(1, username="", password="password123!", email="jmiller@hotmail.com", first_name="Joe", surname="Miller")
    assert user.form_is_valid() == False
    user = User(1, username="jmiller84", password="", email="jmiller@hotmail.com", first_name="Joe", surname="Miller")
    assert user.form_is_valid() == False
    user = User(1, username="jmiller84", password="password123!", email="", first_name="Joe", surname="Miller")
    assert user.form_is_valid() == False
    user = User(1, username="jmiller84", password="password123!", email="jmiller@hotmail.com", first_name="", surname="Miller")
    assert user.form_is_valid() == False
    user = User(1, username="jmiller84", password="password123!", email="jmiller@hotmail.com", first_name="Joe", surname="")
    assert user.form_is_valid() == False
    user = User(1, username=None, password="password123!", email="jmiller@hotmail.com", first_name="Joe", surname="Miller")
    assert user.form_is_valid() == False
    user = User(1, username="jmiller84", password=None, email="jmiller@hotmail.com", first_name="Joe", surname="Miller")
    assert user.form_is_valid() == False
    user = User(1, username="jmiller84", password="password123!", email=None, first_name="Joe", surname="Miller")
    assert user.form_is_valid() == False
    user = User(1, username="jmiller84", password="password123!", email="jmiller@hotmail.com", first_name=None, surname="Miller")
    assert user.form_is_valid() == False
    user = User(1, username="jmiller84", password="password123!", email="jmiller@hotmail.com", first_name="Joe", surname=None)
    assert user.form_is_valid() == False

"""
Test user generates errors
"""
def test_users_generate_errors():
    user = User(1, username="", password="password123!", email="jmiller@hotmail.com", first_name="Joe", surname="Miller")
    assert user.generate_errors() == "Username can't be blank"
    user = User(1, username="jmiller84", password="", email="jmiller@hotmail.com", first_name="Joe", surname="Miller")
    assert user.generate_errors() == "Password can't be blank"
    user = User(1, username="jmiller84", password="password123!", email="", first_name="Joe", surname="Miller")
    assert user.generate_errors() == "Email can't be blank"
    user = User(1, username="jmiller84", password="password123!", email="jmiller@hotmail.com", first_name="", surname="Miller")
    assert user.generate_errors() == "First Name can't be blank"
    user = User(1, username="jmiller84", password="password123!", email="jmiller@hotmail.com", first_name="Joe", surname="")
    assert user.generate_errors() == "Surname can't be blank"
    user = User(1, username=None, password="password123!", email="jmiller@hotmail.com", first_name="Joe", surname="Miller")
    assert user.generate_errors() == "Username can't be blank"
    user = User(1, username="jmiller84", password=None, email="jmiller@hotmail.com", first_name="Joe", surname="Miller")
    assert user.generate_errors() == "Password can't be blank"
    user = User(1, username="jmiller84", password="password123!", email=None, first_name="Joe", surname="Miller")
    assert user.generate_errors() == "Email can't be blank"
    user = User(1, username="jmiller84", password="password123!", email="jmiller@hotmail.com", first_name=None, surname="Miller")
    assert user.generate_errors() == "First Name can't be blank"
    user = User(1, username="jmiller84", password="password123!", email="jmiller@hotmail.com", first_name="Joe", surname=None)
    assert user.generate_errors() == "Surname can't be blank"


