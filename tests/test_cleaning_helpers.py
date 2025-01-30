import pandas as pd
from src.helpers.cleaning_helpers import remove_1val_cols, filter_only_lads, remove_missing_lads

def test_remove_single_value_columns_helper():
    """Ensure remove_1val_cols removes columns with only one unique value."""
    df = pd.DataFrame({
        "A": [1, 1, 1],
        "B": [2, 3, 4],
        "C": ["X", "X", "X"]
    })
    cleaned_df = remove_1val_cols(df)
    
    assert "A" not in cleaned_df.columns, "Failed: Column 'A' should be removed"
    assert "C" not in cleaned_df.columns, "Failed: Column 'C' should be removed"
    assert "B" in cleaned_df.columns, "Failed: Column 'B' should be retained"

def test_filter_only_lads():
    """Ensure filter_only_lads retains only LAD-level data."""
    df = pd.DataFrame({
        "geographic_level": ["National", "Local authority district", "Regional", "LOCAL AUTHORITY DISTRICT"],
        "lad_code": ["", "E07000123", "", "E07000456"]
    })
    filtered_df = filter_only_lads(df)

    assert filtered_df.shape[0] == 2, "Failed: Incorrect number of LAD rows retained"
    assert set(filtered_df["lad_code"]) == {"E07000123", "E07000456"}, "Failed: LAD codes do not match expected values"
    assert "geographic_level" in filtered_df.columns, "Failed: 'geographic_level' column should remain"

def test_remove_missing_lads():
    """Ensure remove_missing_lads removes rows where lad_name or lad_code is missing."""
    
    df_full = pd.DataFrame({
        "lad_name": ["A", "B", "C"],
        "lad_code": ["LAD01", "LAD02", "LAD03"],
        "other_col": [1, 2, 3]
    })
    df_cleaned = remove_missing_lads(df_full)
    assert df_cleaned.equals(df_full), "Failed: Clean DataFrame was modified incorrectly"

    df_partial = pd.DataFrame({
        "lad_name": ["A", None, "C"],
        "lad_code": ["LAD01", "LAD02", None],
        "other_col": [1, 2, 3]
    })
    df_cleaned = remove_missing_lads(df_partial)
    assert df_cleaned.shape[0] == 1, "Failed: Not all rows with missing data were removed"
    assert set(df_cleaned["lad_name"]) == {"A"}, "Failed: Remaining rows do not match expected values"

    df_all_missing = pd.DataFrame({
        "lad_name": [None, None],
        "lad_code": [None, None],
        "other_col": [1, 2]
    })
    df_cleaned = remove_missing_lads(df_all_missing)
    assert df_cleaned.empty, "Failed: Expected an empty DataFrame"

    df_irrelevant_missing = pd.DataFrame({
        "lad_name": ["A", "B", "C"],
        "lad_code": ["LAD01", "LAD02", "LAD03"],
        "other_col": [1, None, 3]
    })
    df_cleaned = remove_missing_lads(df_irrelevant_missing)
    assert df_cleaned.equals(df_irrelevant_missing), "Failed: Unrelated missing values caused removal"

    df_already_clean = pd.DataFrame({
        "lad_name": ["X", "Y", "Z"],
        "lad_code": ["LAD10", "LAD11", "LAD12"],
        "other_col": [5, 6, 7]
    })
    df_cleaned = remove_missing_lads(df_already_clean)
    assert df_cleaned.equals(df_already_clean), "Failed: Clean data was altered incorrectly"
