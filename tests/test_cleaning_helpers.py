import pandas as pd
from src.helpers.cleaning_helpers import remove_1val_cols, filter_only_lads


def test_remove_single_value_columns_helper():
    df = pd.DataFrame({
        "A": [1, 1, 1],
        "B": [2, 3, 4],
        "C": ["X", "X", "X"]
    })
    cleaned_df = remove_1val_cols(df)
    assert "A" not in cleaned_df.columns
    assert "C" not in cleaned_df.columns
    assert "B" in cleaned_df.columns

def test_filter_only_lads():
    df = pd.DataFrame({
        "geographic_level": ["National", "Local authority district", "Regional", "LOCAL AUTHORITY DISTRICT"],
        "lad_code": ["", "E07000123", "", "E07000456"]
    })
    filtered_df = filter_only_lads(df)
    assert filtered_df.shape[0] == 2
    expected_lad_codes = {"E07000123", "E07000456"}
    assert set(filtered_df["lad_code"]) == expected_lad_codes
    assert "geographic_level" in filtered_df.columns

