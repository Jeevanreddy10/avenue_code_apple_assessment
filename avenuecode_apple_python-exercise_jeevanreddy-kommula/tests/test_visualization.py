import pytest
from src.my_package.visualization import plot_closing_price, plot_candlestick_chart
import pandas as pd

# Sample test data (you can use real or synthetic data here)
test_data = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'AAPL.Close': [102, 104, 106, 102, 105],
    'AAPL.Volume': [1000000, 1100000, 1200000, 1050000, 1150000]
})

def test_plot_closing_price():
    # Your test cases for plot_closing_price function
    plot_closing_price(test_data)  # You can adjust this to your actual function usage
    # Add assertions if possible

# def test_plot_candlestick_chart():
#     # Your test cases for plot_candlestick_chart function
#     plot_candlestick_chart(test_data)  # You can adjust this to your actual function usage
#     # Add assertions if possible

if __name__ == "__main__":
    pytest.main()
