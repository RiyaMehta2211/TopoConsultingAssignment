from flask import Flask, render_template, jsonify
import pandas as pd
import json
class APIHandler:
    def __init__(self, app, data):
        self.app = app
        self.data = data
    def set_routes(self):
        # GET /api/data: Returns the full unified dataset
        @self.app.route('/api/data', methods=['GET'])
        def get_data():
            return jsonify(self.data.to_dict(orient="records"))

        # GET /api/data/{file_type}: Returns data specific to a file type
        @self.app.route('/api/data/<file_type>', methods=['GET'])
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