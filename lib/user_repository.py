from lib.user import User
import hashlib


class UserRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all users
    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["username"], row["password"], row['email'], row['first_name'], row['surname'])
            users.append(item)
        return users

    # Find a single user by its username
    def find_by_username(self, username):
        rows = self._connection.execute(
            'SELECT * from users WHERE username = %s', [username])
        if len(rows) > 0:
            row = rows[0]
            return User(row["id"], row["username"], row["password"], row['email'], row['first_name'], row['surname'])
        else:
            return None

    # Create a new user
    def create(self, user):
        # Hash the password
        binary_password = user.password.encode("utf-8")
        hashed_password = hashlib.sha256(binary_password).hexdigest()

        # Store the email and hashed password in the database
        rows = self._connection.execute('INSERT INTO users (username, password, email, first_name, surname) VALUES (%s, %s, %s, %s, %s) RETURNING id', [
                                    user.username, hashed_password, user.email, user.first_name, user.surname])
        row = rows[0]
        user.id = row["id"]
        return user
    
    def check_password(self, username, password_attempt):
        # Hash the password attempt
        binary_password_attempt = password_attempt.encode("utf-8")
        hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()

        # Check whether there is a user in the database with the given email
        # and a matching password hash, using a SELECT statement.
        rows = self._connection.execute(
            'SELECT * FROM users WHERE username = %s AND password = %s',
            [username, hashed_password_attempt])

        # Return True if SQL SELECT query finds any rows, the password is correct.
        return len(rows) > 0

    # Delete a user by its id
    def delete(self, user_id):
        self._connection.execute(
            'DELETE FROM users WHERE id = %s', [user_id])
        return None

    def password_is_valid(self, password):     
        special_chars = ["!", "@", "$", "%", "&"]
        result = [char for char in password if char in special_chars]

        if len(password) > 7 and len(result) >0 :
            return True
        else: 
            return False
            

    
    