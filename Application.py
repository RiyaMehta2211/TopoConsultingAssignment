from flask import Flask, render_template, jsonify
import DataIngestion
import DataProcessor
import APIHandler
import Visualization
import pandas as pd
class Application:
    def _init_(self):
        self.app = Flask(__name__)
        self.data = None
    def run(self):
        ingest_data = DataIngestion()
        ingest_data.load_csv("datasets/dataset2.csv")
        ingest_data.load_json("datasets/dataset1.json")
        ingest_data.load_pptx("datasets/dataset4.pptx")
        ingest_data.load_pdf("datasets/dataset3.pdf")
        process_data = DataProcessor(ingest_data.datasets)
        process_data.merge_data()
        try:
            unified_data = pd.read_csv("unified_data.csv")
        except FileNotFoundError:
            unified_data = pd.DataFrame()
        self.data = unified_data
        api_handler = APIHandler(self.app, self.data)
        api_handler.set_routes()
        data_visualization = Visualization(self.data)
        pie_chart = data_visualization.create_pie_chart()
        bar_chart = data_visualization.create_bar_chart()
        table_data = data_visualization.create_table()
        @self.app.route('/')
        def index():
            return render_template("index.html", pie_chart=pie_chart, bar_chart=bar_chart, table_data=table_data)
        self.app.run(debug=True)


        
