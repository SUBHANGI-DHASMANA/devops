from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

# MongoDB connection
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.test
collection = db['flask-tutorial']

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    # return jsonify({"error": "test error"}), 500
    try:
        form_data = request.json

        if not form_data:
            return jsonify({"error": "No data received"}), 400

        collection.insert_one(form_data)

        return jsonify({"message": "Data submitted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    try:
        data = request.json

        if not data:
            return jsonify({"error": "No data received"}), 400

        item_name = data.get("itemName")
        item_description = data.get("itemDescription")

        if not item_name or not item_description:
            return jsonify({
                "error": "itemName and itemDescription are required"
            }), 400

        todo_item = {
            "itemName": item_name,
            "itemDescription": item_description
        }

        collection.insert_one(todo_item)

        return jsonify({
            "message": "To-Do item submitted successfully"
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api', methods=['GET'])
def api():
    with open("data.json", "r") as file:
        data = json.load(file)
    return jsonify(data), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
