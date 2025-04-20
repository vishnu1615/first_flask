from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def first():
    return "hello vishnu"
@app.route('/vishnu')
def second():
    return 'this is second form'

@app.route('/form_entry')
def third():
    return render_template('entry_form.html')
@app.route('/fourth')
def home():
    return render_template('index.html')  # This will look for templates/index.html

if __name__ == '__main__':
    app.run(debug = True)