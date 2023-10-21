import os
from flask import Flask, request, Response
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017/task")
mongo = PyMongo(app)
collection = mongo.db['objects']


@app.route('/', methods=['GET', 'POST', 'PUT'])
def process_request():
    if request.method == 'POST':
        data = request.get_json()
        if "key" in data and "value" in data:
            if collection.find_one({"key": data["key"]}):
                return Response(status=409, response="The same key already exists."
                                                     " Did you mean the PUT method?")
            collection.insert_one(data)
            return Response(status=200, response="Success")
        else:
            return Response(status=400, response="Not all fields provided. ['key', 'value']")

    elif request.method == 'PUT':
        data = request.get_json()
        if "key" in data and "new_value" in data:
            key = data["key"]
            new_value = data["new_value"]
            if not collection.find_one({"key": key}):
                return Response(status=404, response="No such key-value pair")
            result = collection.update_one({"key": key}, {"$set": {"value": new_value}})
            if result.modified_count > 0:
                return Response(status=200, response="Success")
            else:
                return Response(status=404, response="Data already up to date!")
        else:
            return Response(status=400, response="Not all fields provided. ['key', 'value']")

    elif request.method == 'GET':
        key = request.args.get("key")
        if key:
            document = collection.find_one({"key": key})
            if document:
                document["_id"] = str(document["_id"])
                return document
            else:
                return Response(status=404, response="No such key")
        else:
            return Response(status=400, response="Not all fields provided. ['key']")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
