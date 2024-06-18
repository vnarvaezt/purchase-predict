import pytest
import pandas as pd
import os
from purchase_predict.pipelines.preprocessing.nodes import encode_features
from kedro.io import DataCatalog, MemoryDataset

@pytest.fixture(scope="module")
def dataset_not_encoded():
    print(os.getcwd())
    path = "data/03_primary/primary.csv"
    return pd.read_csv(path, sep=",")


@pytest.fixture(scope="module")
def test_ratio():
    return 0.3

@pytest.fixture(scope="module")
def dataset_encoded(dataset_not_encoded):
    return encode_features(dataset_not_encoded)["features"]

@pytest.fixture(scope="module")
# necessary to test the pipeline
def catalog_test(dataset_not_encoded, test_ratio):
    catalog = DataCatalog({
        "primary": MemoryDataset(dataset_not_encoded),
        "params:test_ratio": MemoryDataset(test_ratio)
    })
    return catalog 