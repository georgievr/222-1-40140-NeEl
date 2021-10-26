from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def message():
    return jsonify('Message from Flask server 05/10/2021')

if __name__ == '__main__':
    app.run(debug=True)