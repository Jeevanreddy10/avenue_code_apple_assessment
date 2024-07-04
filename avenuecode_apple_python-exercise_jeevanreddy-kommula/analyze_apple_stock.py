from src.my_package.data_loader import load_data
from src.my_package.data_cleaning import clean_data, filter_below_average_volume, add_day_of_week
from src.my_package.data_analysis import compute_statistics, aggregate_weekly
from src.my_package.visualization import plot_closing_price, plot_candlestick_chart

import pytest
import os
import sys

def run_tests():
    # # Change directory to the tests directory
    # tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
    # os.chdir(tests_dir)
    
    # # Insert the src directory at the beginning of sys.path
    # sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
    
    # Run pytest
    result = pytest.main()
    
    # Change back to the original directory
    os.chdir(os.path.dirname(__file__))
    
    return result

def main():
    # Run tests
    print("Running tests...")
    test_result = run_tests()
    if test_result != 0:
        print("Tests failed. Exiting script.")
        return
    
    print("Tests passed. Proceeding with data analysis.")
    
    # Load data
    filepath = 'data/finance_charts_apple.csv'
    data = load_data(filepath)
    
    if data is not None:
        # Clean data
        data = clean_data(data)
        
        # Add day of the week
        data = add_day_of_week(data)
        
        # Compute statistics
        max_value, min_value, avg_value = compute_statistics(data)
        print(f"Max Value: {max_value}, Min Value: {min_value}, Average Value: {avg_value}")
        
        # Filter below average volume
        filtered_data = filter_below_average_volume(data)
        
        # Aggregate weekly
        weekly_data = aggregate_weekly(filtered_data)
        
        # Plot closing price
        plot_closing_price(data)
        
        # Plot candlestick chart
        plot_candlestick_chart(weekly_data)
    else:
        print("Failed to load data.")

if __name__ == "__main__":
    main()
