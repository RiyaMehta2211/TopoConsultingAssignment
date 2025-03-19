from flask import Flask, request, render_template, jsonify
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go

app = Flask(__name__)

try:
    unified_data = pd.read_csv("unified_data.csv")
except FileNotFoundError:
    unified_data = pd.DataFrame()

#to remove duplicates in the dataset when plotting the bar graph
unique_companies = unified_data.drop_duplicates(subset=["company_name"], keep="first")

#at least 2 visualisations, hence I will use bar graph and tabular data to convey the point
bar_fig = px.bar(
    unified_data,
    x=unique_companies["company_name"],
    y=unique_companies["company_revenue"],
    title="Revenue Comparison by Company",
    labels={"company_revenue": "Revenue", "company_name": "Company"}
)
bar_fig.update_layout(
    xaxis_title="Company Name",
    yaxis_title="Total Revenue"
)

bar_graph = bar_fig.to_html()
table_data = unified_data.head(10).to_dict(orient="records")
#bar_fig.show()

@app.route('/')
def index():
    return render_template("index.html", bar_chart=bar_graph, table_data=table_data)

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