import pymongo
from flask import Flask

import config

app = Flask(__name__)
if app.config["ENV"] == "production":
    app.config.from_object(config.ProductionConfig)
else:
    app.config.from_object(config.DevelopmentConfig)

client = pymongo.MongoClient(app.config["DATABASE_URI"])
db = client.get_database('resumeiomodel')

if "scores" not in db.list_collection_names():
    print("== create scores ==")
    db.create_collection("scores")


@app.route("/")
def hello_world():
    db.get_collection("scores").insert_one(
        {"id": 1, "name": "name"})
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
