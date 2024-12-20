from typing import Any, Dict

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def encode_features(dataset: pd.DataFrame) -> pd.DataFrame:
    """
    Encode features of data file.
    """
    features = dataset.drop(["user_id", "user_session"], axis=1).copy()
    # alternative
    variables_to_encode = ["category", "sub_category", "brand"]
    features[variables_to_encode] = features[variables_to_encode].astype(str)
    features[variables_to_encode] = features[variables_to_encode].replace(
        ["nan", np.NaN], "unknown"
    )
    print("hellooooo")

    encoders = []
    for label in variables_to_encode:
        # features[label] = features[label].astype(str)
        # features.loc[features[label] == "nan", label] = "unknown"
        # TODO: transform fit and transform in 2 steps and save encoder
        encoder = LabelEncoder()
        encoder.fit(features.loc[:, label].copy())
        features.loc[:, label] = encoder.transform(features.loc[:, label].copy())
        # features.loc[:, label] = encoder.fit_transform(features.loc[:, label].copy())
        features[label] = features[label].astype(int)
        encoders.append((label, encoder))

    features["weekday"] = features["weekday"].astype(int)

    return dict(features=features, transform_pipeline=encoders)


def split_dataset(dataset: pd.DataFrame, test_ratio: float) -> Dict[str, Any]:
    """
    Splits dataset into a training set and a test set.
    """
    X = dataset.drop("purchased", axis=1)
    y = dataset["purchased"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_ratio, random_state=40
    )

    return dict(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test)
