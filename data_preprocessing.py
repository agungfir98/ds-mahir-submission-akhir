import joblib
from pandas import DataFrame

preproceessor = joblib.load("model/preprocessor.joblib")
feature_columns = joblib.load("model/feature_columns.joblib")


def preprocess(data: DataFrame):
    if list(data.columns) != feature_columns:
        raise ValueError(
            "Dataframe columns do not match the expected feature columns and order.")

    data = preproceessor.transform(data)

    return data
