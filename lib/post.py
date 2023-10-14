from datetime import datetime

class Post:
    def __init__(self, id, title, content, user_id):
        self.id = id
        self.title = title
        self.content = content
        self.user_id = user_id


    def is_valid(self):
        if self.title == None or self.title == "":
            return False
        if self.content == None or self.content == "":
            return False
        return True

    def generate_errors(self):
        errors = []
        if self.title == None or self.title == "":
            errors.append("Title can't be blank")
        if self.content == None or self.content == "":
            errors.append("Content can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)
        

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Post({self.id}, {self.title}, {self.content}, {self.user_id})"
