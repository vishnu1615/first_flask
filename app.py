from flask import Flask

app = Flask(__name__)

@app.route('/')
def first():
    return "hello vishnu"
@app.route('/vishnu')
def second():
    return 'this is second form'

if __name__ == '__main__':
    app.run()