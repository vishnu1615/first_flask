from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def first():
    return "hello vishnu"
@app.route('/vishnu')
def second():
    return 'this is second form'

app.route('/form_entry')
def third():
    return render_template('entry_form.html')

if __name__ == '__main__':
    app.run()