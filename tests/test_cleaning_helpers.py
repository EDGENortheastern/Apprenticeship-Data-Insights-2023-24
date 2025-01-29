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

def test_filter_local_authority_districts_helper():
    df = pd.DataFrame({
        "geographic_level": ["National", "Local authority district", "Regional"],
        "lad_code": ["", "E07000123", ""]
    })
    filtered_df = filter_only_lads(df)
    assert filtered_df.shape[0] == 1  # Only 1 LAD row should remain
    assert "geographic_level" not in filtered_df.columns