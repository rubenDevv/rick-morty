
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from the Rick and Morty API!"

if __name__ == '__main__':
    app.run(debug=True)