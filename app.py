from flask import Flask, jsonify
from apis.rick_and_morty import rick_and_morty_bp  # Correct import
from flask_cors import CORS


app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

app.register_blueprint(rick_and_morty_bp, url_prefix='/api')

@app.route("/")
def hello_world():
    print('route')
    return"<p>Hello</p>"

if __name__ == "__main__":
    app.run(debug=True)
