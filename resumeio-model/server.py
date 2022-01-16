from flask import Flask
from flask import request
import model

app = Flask(__name__)


@app.route("/", methods=['POST'])
def hello_world():
    req_data = request.get_json(force=True)
    print("Got data " + req_data)
    return model.match(req_data['job_description'], req_data['candidate_description'])


if __name__ == "__main__":
    app.run(host='0.0.0.0')
