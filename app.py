from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# MySQL configuration with URL-encoded password
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://vishnu:%23BJNVSreddy143@localhost:3306/reddy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define your model for the users table
class login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    number = db.Column(db.String(10))

# Route to test DB connection
@app.route('/check_db')
def check_db():
    try:
        db.engine.connect()
        return "✅ Database is connected!"
    except OperationalError as e:
        return f"❌ Database connection failed! Error: {e}"

# Routes
@app.route('/')
def first():
    return "hello vishnu"

@app.route('/vishnu')
def second():
    return 'this is second form'

@app.route('/form')
def form():
    return render_template('entry_form.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/report')
def reports():
    return 'hello this is report'

@app.route('/insert', methods=['POST'])
def inserts():
    name = request.form['name']
    age = request.form['age']
    phone = request.form['phone']

    if not name or not age or not phone:
        flash("⚠️ All fields are required!", "error")
        return redirect(url_for('form'))

    new_user = login(name=name, age=age, number=phone)
    db.session.add(new_user)
    db.session.commit()

    flash(f"✅ User {name} added successfully!", "success")
    return redirect(url_for('form'))


@app.route('/reports')
def report():
    users = login.query.filter(login.id == 10).all()
    return render_template('reports.html', users=users)





if __name__ == '__main__':
    app.run(debug=True)
