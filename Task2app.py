from flask import Flask, render_template, jsonify
import pandas as pd
import json
import plotly.express as px
import re

app = Flask(__name__)

try:
    unified_data = pd.read_csv("unified_data.csv")
except FileNotFoundError:
    unified_data = pd.DataFrame()

target_cell = None
for col in unified_data.columns:
    for value in unified_data[col].dropna():
        if "Revenue Breakdown by Activity" in str(value):
            target_cell = value
            break
    if target_cell:
        break

#to extract the relevant percentages using regex
pattern = r"(\w+\s?\w*):\s?(\d+)%"
matches = re.findall(pattern, target_cell)

revenue_distribution_data = pd.DataFrame(matches, columns=["Activity", "Percentage"])
revenue_distribution_data["Percentage"] = revenue_distribution_data["Percentage"].astype(int)

#3 visualisations, hence I will use pie chart, bar graph and tabular data to convey the data representation

pie_fig = px.pie(
    revenue_distribution_data,
    names="Activity",
    values="Percentage",
    title="Revenue Breakdown by Activity for FitPro"
)
pie_chart = pie_fig.to_html()

#to remove duplicates in the dataset when plotting the bar graph
unique_companies = unified_data.drop_duplicates(subset=["company_name"], keep="first")

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

@app.route('/')
def index():
    return render_template("index.html", pie_chart=pie_chart, bar_chart=bar_graph, table_data=table_data)

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