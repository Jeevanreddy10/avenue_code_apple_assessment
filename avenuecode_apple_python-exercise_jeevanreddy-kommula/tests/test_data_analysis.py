import pytest
import pandas as pd
from src.my_package.data_analysis import compute_statistics, aggregate_weekly

def test_compute_statistics():
    # Create sample data
    data = pd.DataFrame({
        'Date': pd.date_range('2023-01-01', periods=10),
        'AAPL.Open': [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
        'AAPL.High': [110, 111, 112, 113, 114, 115, 116, 117, 118, 119],
        'AAPL.Low': [90, 91, 92, 93, 94, 95, 96, 97, 98, 99],
        'AAPL.Close': [105, 106, 107, 108, 109, 110, 111, 112, 113, 114],
        'AAPL.Volume': [1000000, 1100000, 1200000, 1300000, 1400000, 1500000, 1600000, 1700000, 1800000, 1900000]
    })

    # Compute statistics
    max_value, min_value, avg_value = compute_statistics(data)
    
    # Check computed statistics
    assert max_value == 114, f"Expected max_value to be 119, but got {max_value}"
    assert min_value == 105, f"Expected min_value to be 100, but got {min_value}"
    assert avg_value == 109.5, f"Expected avg_value to be 109.5, but got {avg_value}"

def test_aggregate_weekly():
    # Create sample data
    data = pd.DataFrame({
        'Date': pd.date_range('2023-01-01', periods=10),
        'AAPL.Open': [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
        'AAPL.High': [110, 111, 112, 113, 114, 115, 116, 117, 118, 119],
        'AAPL.Low': [90, 91, 92, 93, 94, 95, 96, 97, 98, 99],
        'AAPL.Close': [105, 106, 107, 108, 109, 110, 111, 112, 113, 114],
        'AAPL.Volume': [1000000, 1100000, 1200000, 1300000, 1400000, 1500000, 1600000, 1700000, 1800000, 1900000]
    })

    # Aggregate weekly
    weekly_data = aggregate_weekly(data)
    
    # Check if weekly_data is not empty
    assert not weekly_data.empty, "Weekly aggregated data is empty."


if __name__ == "__main__":
    pytest.main()
