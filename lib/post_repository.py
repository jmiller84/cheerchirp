from lib.post import Post
from datetime import datetime
from config import open_ai_api_key
import os
import openai

class PostRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all posts
    def all_with_user_info(self):
        sql_query = """
            SELECT
                posts.id AS post_id,
                posts.title,
                posts.content,
                posts.datetime,
                users.id AS user_id,
                users.username,
                users.email,
                users.first_name,
                users.surname
            FROM
                posts
            JOIN
                users ON posts.user_id = users.id;
        """
    
        rows = self._connection.execute(sql_query)
        posts = []
        
        for row in rows:
            post_data = {
                "id": row["post_id"],
                "title": row["title"],
                "content": row["content"],
                "datetime": row["datetime"],
                "user_id": row["user_id"]
            }
            user_data = {
                "id": row["user_id"],
                "username": row["username"],
                "email": row["email"],
                "first_name": row["first_name"],
                "surname": row["surname"]
            }
            
            # Create a Post instance with user information
            post = Post(post_data["id"], post_data["title"], post_data["content"], post_data["datetime"], user_data)
            posts.append(post)
        
        return posts


    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Post(row["id"], row["title"], row["content"], row["datetime"], row['user_id'])
            posts.append(item)
        return posts

    # Find a single post by its id
    def find(self, post_id):
        rows = self._connection.execute(
            'SELECT * from posts WHERE id = %s', [post_id])
        row = rows[0]
        return Post(row["id"], row["title"], row["content"], row["datetime"], row['user_id'])

    # Create a new post
    def create(self, post):
        dt_now = datetime.now()
        rows = self._connection.execute('INSERT INTO posts (title, content, datetime, user_id) VALUES (%s, %s, %s, %s) RETURNING id', [
                                    post.title, post.content, dt_now, post.user_id])
        row = rows[0]
        post.id = row["id"]
        return post

    # Delete a post by its id
    def delete(self, post_id):
        self._connection.execute(
            'DELETE FROM posts WHERE id = %s', [post_id])
        return None
    
    
    def content_is_positive(self, content):

        openai.api_key = open_ai_api_key
        # openai.api_key = os.getenv(open_ai_api_key)

        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "user",
            "content": f"Return True or False to the following: '{content}' is a positive statement"
            }
        ],
        temperature=1,
        max_tokens=1,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

        print("api: ", response['choices'][0]['message']['content'])
        print(type(response['choices'][0]['message']['content']))
        return str(response['choices'][0]['message']['content'])
