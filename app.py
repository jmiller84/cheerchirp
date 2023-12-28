import os
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.post import Post
from lib.post_repository import PostRepository
from lib.user import User
from lib.user_repository import UserRepository
from config import secret_key


app = Flask(__name__)
app.secret_key = secret_key


@app.route('/index_new')
def new_index():
    return render_template('index_new.html')


#------------------LOG IN---------------------

# GET /login
@app.route('/login')
def login():
    return render_template('login.html')

# POST /login
@app.route('/login', methods=['POST'])
def login_post():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    username = request.form['username']
    password = request.form['password']


    if repository.check_password(username, password):

        user = repository.find_by_username(username)
        # Set the user ID in session
        session['user_id'] = user.id

        return redirect('/')
    else:
        errors = "Username and Password did not match please try again"
        return render_template('login.html', errors=errors)
        
#------------------SIGN UP---------------------

# GET /signup
@app.route('/signup')
def signup():
    return render_template('signup.html')

# POST /signup
@app.route('/signup', methods=['POST'])
def signup_post():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    first_name = request.form['first_name']
    surname = request.form['surname']

    if not repository.find_by_username(username):
        if repository.password_is_valid(password):
            new_user = User(None, username, password, email, first_name, surname)
            repository.create(new_user)
            auth_user = repository.find_by_username(username)
            session['user_id'] = auth_user.id

            return redirect('/')
        else:
            errors = "Password is not valid"
            return render_template('signup.html', errors = errors)
    else:
        errors = "Username has already been taken"
        return render_template('signup.html', errors = errors)



#------------------ HOME PAGE ---------------------

 # GET /
@app.route('/', methods=['GET'])
def get_posts():
    connection = get_flask_database_connection(app)
    repository = PostRepository(connection)

    if 'user_id' in session:
        auth = True
    else:
        auth = False

    posts = repository.all_with_user_info() 
    return render_template("/index.html", posts = posts, auth=auth)

# POST /
@app.route('/', methods = ['POST'])
def create_post():
    connection = get_flask_database_connection(app)
    repository = PostRepository(connection)

    if "logout_button" in request.form:
        session.pop('user_id')
        return redirect("/")
    else:
        title = request.form['title']
        content = request.form['content']
        user_id = session['user_id']

        if repository.content_is_positive(content) == "True" :
            new_post = Post(None, title, content, None, user_id)

            if not new_post.is_valid():
                errors = new_post.generate_errors()
                return redirect("/", errors= errors)

            repository.create(new_post) 
            return redirect("/")
        else:
            messages = "This is not a positive post, rephrase the content and try again"
            return redirect("/", messages)




if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
