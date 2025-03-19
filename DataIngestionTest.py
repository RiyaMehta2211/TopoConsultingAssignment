import pytest
from DataIngestion import DataIngestion

@pytest.fixture
def data_ingestion():
    return DataIngestion()
def test_load_csv(data_ingestion):
    data_ingestion.load_csv("datasets/dataset2.csv")
    csv_data = data_ingestion.get_data("csv")
    assert csv_data is not None
    assert not csv_data.empty

def test_load_json(data_ingestion):
    data_ingestion.load_json("datasets/dataset1.json")
    json_data = data_ingestion.get_data("json")
    assert json_data is not None
    assert not json_data.empty

def test_load_pptx(data_ingestion):
    data_ingestion.load_pptx("datasets/dataset4.pptx")
    pptx_data = data_ingestion.get_data("pptx")
    assert pptx_data is not None
    assert "Report" in pptx_data

def test_load_pdf(data_ingestion):
    data_ingestion.load_pdf("datasets/dataset3.pdf")
    pdf_data = data_ingestion.get_data("pdf")
    assert pdf_data is not None
    assert not pdf_data.empty