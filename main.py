from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    message = {"message": "Hello, redStone, welcome"}
    return message


if __name__ == '__main__':
    app.run()
