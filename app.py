from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy  # Required for SQLAlchemy
from sqlalchemy.exc import OperationalError

app = Flask(__name__)

# MySQL configuration with URL-encoded password
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://vishnu:%23BJNVSreddy143@localhost:3306/reddy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Test Route to check database connection
@app.route('/check_db')
def check_db():
    try:
        # Attempting to connect to the database
        db.engine.connect()  # This is the correct way to check if the DB is reachable
        return "Database is connected!"
    except OperationalError as e:
        return f"Database connection failed! Error: {e}"

# Define your model for the users table
class login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    number = db.Column(db.String(10))



@app.route('/')
def first():
    return "hello vishnu"

@app.route('/vishnu')
def second():
    return 'this is second form'

@app.route('/form_entry')
def third():
    return render_template('entry_form.html')  # Make sure this HTML file exists in the 'templates' folder

@app.route('/fourth')
def home():
    return render_template('index.html')  # Make sure this HTML file exists in the 'templates' folder


@app.route('/insert', methods=['POST'])
def inserts():
    # Extract data from the form
    name = request.form['name']
    age = request.form['age']
    phone = request.form['phone']

    # Insert data into the database
    new_user = login(name=name, age=age, number=phone)
    db.session.add(new_user)
    db.session.commit()

    return f"{name} {age} {phone}"  # ✅ Now this happens after insertion

    # Return a success message
    return f"User {name} with age {age} and phone {phone} added successfully!"

if __name__ == '__main__':
    app.run(debug=True)
