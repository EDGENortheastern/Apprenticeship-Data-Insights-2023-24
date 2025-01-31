import pandas as pd

def remove_totals(df, columns):
    """
    Removes rows where any specified column contains the word 'Total'.
    
    Parameters:
        df (pd.DataFrame): The DataFrame to process.
        columns (list of str): The column names to check for 'Total'.
    
    Returns:
        pd.DataFrame: A new DataFrame with 'Total' rows removed.
    """
    mask = ~df[columns].apply(lambda col: col.str.contains("Total", na=False)).any(axis=1)
    return df[mask]
