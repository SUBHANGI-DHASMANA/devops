from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json

import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
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

@app.route('/api', methods=['GET'])
def api():
    with open("data.json", "r") as file:
        data = json.load(file)
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)