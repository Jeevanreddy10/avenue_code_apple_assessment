import pytest
import pandas as pd
from src.my_package.data_cleaning import clean_data, filter_below_average_volume, add_day_of_week

def test_clean_data():
    # Create sample data
    data = pd.DataFrame({
        'Date': pd.date_range('2023-01-01', periods=5),
        'AAPL.Open': [100, 101, 102, 103, 104],
        'AAPL.High': [110, 111, 112, 113, 114],
        'AAPL.Low': [90, 91, 92, 93, 94],
        'AAPL.Close': [105, 106, 107, 108, 109],
        'AAPL.Volume': [1000000, 1100000, 1200000, 1300000, 1400000]
    })

    # Clean data
    cleaned_data = clean_data(data)
    
    # Check if lengths match
    assert len(cleaned_data) == len(data), "Lengths must match after cleaning."

def test_filter_below_average_volume():
    # Create sample data
    data = pd.DataFrame({
        'Date': pd.date_range('2023-01-01', periods=5),
        'AAPL.Open': [100, 101, 102, 103, 104],
        'AAPL.High': [110, 111, 112, 113, 114],
        'AAPL.Low': [90, 91, 92, 93, 94],
        'AAPL.Close': [105, 106, 107, 108, 109],
        'AAPL.Volume': [1000000, 900000, 800000, 1100000, 1200000]
    })

    # Filter below average volume
    filtered_data = filter_below_average_volume(data)
    
    # Check if lengths match
    assert len(filtered_data) == 3, "Expected 3 rows after filtering below average volume."

def test_add_day_of_week():
    # Create sample data
    data = pd.DataFrame({
        'Date': pd.date_range('2023-01-01', periods=4),
        'AAPL.Open': [100, 101, 102, 103],
        'AAPL.High': [110, 111, 112, 113],
        'AAPL.Low': [90, 91, 92, 93],
        'AAPL.Close': [105, 106, 107, 108],
        'AAPL.Volume': [1000000, 1100000, 1200000, 1300000]
    })

    # Add day of the week
    data_with_day = add_day_of_week(data)
    
    # Check day of the week values
    expected_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday']
    assert all(day in data_with_day['DayOfWeek'].unique() for day in expected_days), \
        f"DayOfWeek values do not match expected values: {expected_days}"

if __name__ == "__main__":
    pytest.main()
