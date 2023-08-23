from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    message = {"message": "Hello, redStone, welcome"}
    return jsonify(message)


if __name__ == '__main__':
    app.run()
