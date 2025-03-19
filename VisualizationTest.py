import pytest
from DataIngestion import DataIngestion
from DataProcessor import DataProcessor
from Visualization import Visualization
import pandas as pd

@pytest.fixture
def data_visualization():
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
    return Visualization(unified_data)

def test_create_pie_chart(data_visualization):
    pie_chart = data_visualization.create_pie_chart()
    assert pie_chart is not None

def test_create_bar_chart(data_visualization):
    bar_chart = data_visualization.create_bar_chart()
    assert bar_chart is not None

def test_create_bar_chart(data_visualization):
    bar_chart = data_visualization.create_bar_chart()
    assert bar_chart is not None

def test_create_table(data_visualization):
    table = data_visualization.create_table()
    assert table is not None