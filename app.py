from flask import Flask, request, render_template, jsonify
import pandas as pd
import json
app = Flask(__name__)

unified_data = pd.read_csv("unified_data.csv")
#GET /api/data: Returns the full unified dataset in JSON format.
#GET /api/data/{file_type}: Returns data specific to a file type (e.g., "csv", "excel").

@app.route('/')
def index():
    render_template("index.html")

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(unified_data.to_dict(orient="records"))

#api endpoint to retrieve data from ingested data files
@app.route('/api/data/<file_type>', methods=['GET'])
def get_data_by_file_type(file_type):
    if file_type == "csv":
        data = pd.read_csv("datasets/dataset2.csv").to_dict(orient="records")
    elif file_type == "json":
        with open("datasets/dataset1.json", "r") as file:
            data = json.load(file)
    else:
        return jsonify({"error": "Invalid file type. Supported types: 'csv', 'json'"}), 400
    return jsonify(data)

if __name__ == "__main__":
    app.run()