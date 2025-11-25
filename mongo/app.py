# app.py
from flask import Flask, jsonify, request
from db import get_collection

app = Flask(__name__)

@app.route("/")
def home():
    print("SFILS Running")
    return jsonify({"message": "SFILS Mongo backend is running."}) # Asked ChatGPT, did not understand why this needed to return as JSON

# Access using http:{local_host}:{port}/records
@app.route("/records") # Shows the like seperate link
def get_records():
    collection = get_collection() # defined in db.py
    try:
        limit = int(request.args.get("limit", 10)) # This should show recent 10 records
    except ValueError:
        limit = 10

    docs = list(collection.find({}, {"_id": 0}).limit(limit))
    return jsonify(docs) # Things return as json through flask?

if __name__ == "__main__":
    app.run(debug=True)