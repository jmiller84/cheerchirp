from datetime import datetime

class User:
    def __init__(self, id, username, password, email, first_name, surname):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.surname = surname
        

    def form_is_valid(self):
        if self.username == None or self.username == "":
            return False
        if self.password == None or self.password == "":
            return False
        if self.email == None or self.email == "":
            return False
        if self.first_name == None or self.first_name == "":
            return False
        if self.surname == None or self.surname == "":
            return False
        return True
        

    def generate_errors(self):
        errors = []
        if self.username == None or self.username == "":
            errors.append("Username can't be blank")
        if self.password == None or self.password == "":
            errors.append("Password can't be blank")
        if self.email == None or self.email == "":
            errors.append("Email can't be blank")
        if self.first_name == None or self.first_name == "":
            errors.append("First Name can't be blank")
        if self.surname == None or self.surname == "":
            errors.append("Surname can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)
        

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.first_name}, {self.surname})"
