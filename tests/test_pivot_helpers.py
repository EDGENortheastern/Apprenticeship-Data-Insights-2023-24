import pandas as pd
import pytest
from src.helpers.pivot_helpers import remove_totals

@pytest.fixture
def sample_dataframe():
    """Create a sample DataFrame for testing."""
    return pd.DataFrame({
        "category": ["A", "B", "Total", "C", "Total", "D"],
        "value": [10, 20, 30, 40, 50, 60],
        "remarks": ["valid", "Total", "valid", "Total", "valid", "valid"]
    })

def test_remove_totals_single_column(sample_dataframe):
    """Test removal of rows where 'category' contains 'Total'."""
    result = remove_totals(sample_dataframe, ["category"])
    assert "Total" not in result["category"].values
    assert len(result) == 4  # Expecting only non-"Total" rows

