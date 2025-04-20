from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy  # Required for SQLAlchemy
from sqlalchemy.exc import OperationalError

app = Flask(__name__)

# MySQL configuration with URL-encoded password
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%23BJNVSreddy143@localhost:3306/vishnu'
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

if __name__ == '__main__':
    app.run(debug=True)
