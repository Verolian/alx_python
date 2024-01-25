from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import re
import sys

# Check for command-line arguments
if len(sys.argv) != 4:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)

db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

app = Flask(__name__)

############################# TO DO 1 ############################
# Add your code to connect to the database here
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_username}:{db_password}@{db_host}/{db_name}'
db = SQLAlchemy(app)
###############################################################

############################ TO DO 2 ##############################
# Define your USER Model class here
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
#################################################################

# Create the database tables
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()  # This calls the function to create tables


@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"

@app.route('/add_user' ,methods=['GET','POST'], strict_slashes=False)
def addUser():

    if request.method == 'POST':
        try:
            name = request.form.get('name')
            email = request.form.get('email')

            new_user = User(name=name)
            db.session.add(new_user)
            db.session.commit()

            flash('User added successfully!','success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}','error')
        return render_template('add_user.html')
@app.route('/users')
def users():
    all_users=User.query.all()
    return render_template('users.html',users=all_users)
#UPDATE USERS
# Routes
@app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    user = User.query.get(user_id)

    if user is None:
        flash("User not found", 'error')
        return redirect(url_for('index'))

    if request.method == 'POST':
        # Handle POST request
        updated_name = request.form.get('name')
        updated_email = request.form.get('email')

        if not updated_name or not updated_email:
            flash("Both name and email must be provided", 'error')
        else:
            # Validate and update user
            existing_user = User.query.filter(User.email == updated_email, User.id != user_id).first()
            if existing_user:
                flash("Email already taken. Choose a different email.", 'error')
            else:
                user.name = updated_name
                user.email = updated_email
                db.session.commit()
                flash("User updated successfully!", 'success')

    return render_template('update_user.html', user=user)
#  delete Routes
@app.route('/delete_user/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    user = User.query.get(user_id)

    if user is None:
        flash("User not found", 'error')
    else:
        db.session.delete(user)
        db.session.commit()
        flash("User deleted successfully!", 'success')

    return render_template('delete_user.html')

if __name__ == '__main__':
    db.create_all
    app.run(host='0.0.0.0', port=5000, debug=True)