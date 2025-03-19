import pytest
from DataIngestion import DataIngestion
from DataProcessor import DataProcessor
import pandas as pd
import os

@pytest.fixture
def data_processor():
    ingest_data = DataIngestion()
    ingest_data.load_csv("datasets/dataset2.csv")
    ingest_data.load_json("datasets/dataset1.json")
    ingest_data.load_pptx("datasets/dataset4.pptx")
    ingest_data.load_pdf("datasets/dataset3.pdf")
    return DataProcessor(ingest_data.datasets)

def test_merge_data(data_processor):
    data_processor.merge_data()
    df = pd.read_csv("unified_data.csv")
    assert os.path.exists("unified_data.csv")
    assert not df.empty