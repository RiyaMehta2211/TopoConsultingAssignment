from flask import Flask, request, render_template, jsonify
import pandas as pd
import json

app = Flask(__name__)

try:
    unified_data = pd.read_csv("unified_data.csv")
except FileNotFoundError:
    unified_data = pd.DataFrame()

@app.route('/')
def index():
    return render_template("index.html")

# GET /api/data: Returns the full unified dataset
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(unified_data.to_dict(orient="records"))

# GET /api/data/{file_type}: Returns data specific to a file type
@app.route('/api/data/<file_type>', methods=['GET'])
def get_data_by_file_type(file_type):
    file_type = file_type.lower()
    try:
        if file_type == "csv":
            data = pd.read_csv("datasets/dataset2.csv").to_dict(orient="records")
        elif file_type == "json":
            with open("datasets/dataset1.json", "r") as file:
                data = json.load(file)
        else:
            return jsonify({"error": "Invalid file type. Supported types: 'csv', 'json'"}), 400
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": f"File for {file_type} not found."}), 404

if __name__ == "__main__":
    app.run(debug=True)