import pandas as pd

def remove_1val_cols(df: pd.DataFrame) -> pd.DataFrame:
    """Removes columns that contain only a single unique value."""
    return df.drop(columns=[col for col in df.columns if df[col].nunique() == 1])

def filter_only_lads(df: pd.DataFrame) -> pd.DataFrame:
    """Filters DataFrame to include only Local Authority District (LAD) data."""
    return df[df["geographic_level"].str.casefold() == "local authority district"]
