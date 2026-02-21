from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
import os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

# MongoDB connection
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.aws
collection = db['users_data']

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello world!"

@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = list(collection.find({}, {"_id": 0}))
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000, debug=True)
