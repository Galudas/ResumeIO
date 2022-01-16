from flask import Flask
from processing import model

app = Flask(__name__)


@app.route("/")
def hello_world():
    model.encode_words(['foot', 'job', 'IT', 'ball'])
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
