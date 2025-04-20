from flask import Flask

app = Flask(__name__)

@app.route('/')
def first():
    return "hello vishnu"

if __name__ == '__main__':
    app.run()