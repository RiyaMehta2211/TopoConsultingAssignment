import pytest
from flask import Flask
from DataIngestion import DataIngestion
from DataProcessor import DataProcessor
from APIHandler import APIHandler
import pandas as pd

@pytest.fixture
def api_handler():
    app = Flask(__name__)
    ingest_data = DataIngestion()
    ingest_data.load_csv("datasets/dataset2.csv")
    ingest_data.load_json("datasets/dataset1.json")
    ingest_data.load_pptx("datasets/dataset4.pptx")
    ingest_data.load_pdf("datasets/dataset3.pdf")
    data_processor = DataProcessor(ingest_data.datasets)
    data_processor.merge_data()
    try:
        unified_data = pd.read_csv("unified_data.csv")
    except FileNotFoundError:
        unified_data = pd.DataFrame()
    api_handler = APIHandler(app, unified_data)
    api_handler.set_routes()
    return app.test_client()

def test_get_data(api_handler):
    response = api_handler.get('/api/data')
    assert response.status_code == 200

def test_get_data_csv(api_handler):
    response = api_handler.get('/api/data/csv')
    assert response.status_code == 200

def test_get_data_json(api_handler):
    response = api_handler.get('/api/data/json')
    assert response.status_code == 200