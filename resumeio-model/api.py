from flask import Flask, request

app = Flask(__name__)


@app.route("/analyse", methods=['POST'])
def analyse():
    data = request.json
    print(data)
    return data['description']


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
