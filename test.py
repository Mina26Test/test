import pandas as pd


def clean_Data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows with missing 'value'."""
    return df.dropna(subset=["value"])

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Add a new column that doubles 'value'."""
    df = df.copy()
    df["double"] = df["value"] * 2
    return df

def run_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = clean_data(df)
    transformed = transform_data(cleaned)
    return transformed


def test_clean_data():
    df = pd.DataFrame({"value": [1, None, 3]})
    cleaned = clean_data(f)
    assert len(cleaned) == 2
    assert cleaned["value"].tolist() == [1, 3]

def test_transform_data():
    df = pd.DataFrame({"value": [2]})
    transformed = transform_data(df)
    assert "double" in transformed.columns
    assert transformed.loc[0,"double"] == 4

def test_run_pipeline_end_to_end():
    df = pd.DataFrame({"value": [1, None, 2]})
    result = run_pipeline(df)
    assert result["double"].tolist() == [2, 4]

    test_clean_data()
    test_transform_data()
    test_run_pipeline_end_to_end()