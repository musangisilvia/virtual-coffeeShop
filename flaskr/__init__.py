from flask import Flask, render_template, request, redirect, session, url_for
from flask_login import login_user, logout_user, current_user, login_required
from flaskr.models import db, Users, Posts
from flaskr.config import Config
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)

app.config.from_object(Config)
app.secret_key = app.config['SECRET_KEY']

# init db
db.init_app(app)

# for encryption
bcrypt = Bcrypt(app)


login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.route('/authenticate', methods=['POST'])
def authenticate():
    if request.method == 'POST':
        # Implement user authentication logic here and retrieve the user object
        user = Users.query.filter_by(username=request.form['username']).first()
        if user and user.check_password(request.form['password']):
            login_user(user)
            return redirect(url_for('timeline'))
        else:
            # Handle login failure, e.g., show an error message
            return render_template('login.html', error='Invalid credentials')

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('authenticate'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        existing_user = Users.query.filter(db.or_(Users.username == username, Users.email == email)).first()

        if existing_user:
            error = 'Username or email already exists. Please choose different ones.'
            return render_template('register.html', error=error)

        new_user = Users(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('authenticate'))

    return render_template('register.html')


@app.route('/timeline')
@login_required
def timeline():
    all_posts = Posts.get_all_posts()

    return render_template('timeline.html', all_posts=all_posts)

@app.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        content = request.form['content']
        new_post = Posts(user_id=current_user.id, content=content)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('timeline'))
    return render_template('create_post.html')

