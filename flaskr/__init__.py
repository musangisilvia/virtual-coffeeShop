from flask import Flask, render_template, request, redirect, session, url_for
from flask_login import login_user, logout_user, current_user, login_required
from flaskr.models import db, Users
from flaskr.config import Config
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)

app.config.from_object(Config)

# init db
db.init_app(app)

# for encryption
bcrypt = Bcrypt(app)


login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    if request.method == 'POST':
        # Implement user authentication logic here and retrieve the user object
        user = Users.query.filter_by(username=request.form['username']).first()
        if user and Users.check_password(request.form['password']):
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
    return redirect(url_for('login'))


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

        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/timeline')
@login_required
def timeline():
    return render_template('timeline.html')

@app.route('/create_post')
@login_required
def create_post():
    if request.method == 'POST':
        username = request.form['username']
        

# @app.route('/test-db-connection')
# def test_db_connection():
#     try:
#         # Replace the values below with your actual database credentials
#         connection = mysql.connector.connect(
#             # :3306/VirtualCoffee
#             host="database-1.creqgg4niwd7.eu-north-1.rds.amazonaws.com",
#             user="admin",
#             password="8QE1Oh8j9mPoruRmGtsw",
#             database="VirtualCoffee"
#         )

#         cursor = connection.cursor()
#         cursor.execute("SELECT VERSION()")
#         result = cursor.fetchone()

#         connection.close()

#         return jsonify({"status": "success", "result": result[0]}), 200
#     except Exception as e:
#         return jsonify({"status": "error", "message": str(e)}), 500


