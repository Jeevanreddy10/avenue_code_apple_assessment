# Apple Stock Analysis

This project analyzes Apple stock data, including data cleaning, computing statistics, filtering, aggregation, and visualization.

## Requirements

- Python 3.x
- pandas
- matplotlib
- mplfinance
- pytest

## Directory Structure

```
avenuecode_apple_python-exercise_jeevanreddy-kommula/
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── data_loader.py
│       ├── data_cleaning.py
│       ├── data_analysis.py
│       └── visualization.py
├── data/
│   ├── finance_charts_apple.csv
│   └── filtered_apple_stock_data.csv
├── tests/
│   ├── test_data_analysis.py
│   ├── test_data_cleaning.py
│   └── test_visualization.py
├── venv/
│   ├── bin/
│   ├── include/
│   ├── lib/
│   ├── share/
│   └── pyvenv.cfg
├── analyze_apple_stock.py
├── setup.py
├── README.md
└── requirements.txt
```

## Functionality

- **Data Loading and Initial Inspection**: Loads the data from the provided CSV file using pandas.
- **Compute Information about the Dataset**: Calculates max, min, and average values of the 'Close' price. Cleans the time series data by removing duplicates and ensuring proper ordering.
- **Add Day of the Week**: Adds a new column 'DayOfWeek' indicating the day of the week corresponding to each entry's date.
- **Filtering Below Average Volume**: Computes the average volume for the entire dataset. Filters out rows where the volume is below the average and saves the filtered data to a new CSV file.
- **Aggregate Data to Weekly Level**: Aggregates the data to a weekly level, computing open, high, low, close, and volume for each week. Saves the aggregated data to a new CSV file.

## Visualization

- **Plots the closing prices over time** using matplotlib.
- **Plots the weekly stock prices as a candlestick chart** using mplfinance.

## Installation

To set up the project environment, follow these steps:


1. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Analysis

To perform the analysis, run the `analyze_apple_stock.py` script:

```bash
python analyze_apple_stock.py
```

This script will execute the entire data analysis pipeline, from loading and cleaning the data to performing analysis and generating visualizations.

## Contact

For any inquiries or feedback, please contact:

- Jeevan Reddy Kommula
- Email: jeevanreddykommula99@gmail.com

---

For more detailed information on the implementation, please refer to the in-line comments within the code and additional documentation files.


