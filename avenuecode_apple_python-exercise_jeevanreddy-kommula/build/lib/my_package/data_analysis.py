import pandas as pd

def compute_statistics(data):
    max_value = data['AAPL.Close'].max()
    min_value = data['AAPL.Close'].min()
    avg_value = data['AAPL.Close'].mean()
    return max_value, min_value, avg_value

def aggregate_weekly(data):
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    weekly_data = data.resample('W').agg({
        'AAPL.Open': 'first',
        'AAPL.High': 'max',
        'AAPL.Low': 'min',
        'AAPL.Close': 'last',
        'AAPL.Volume': 'sum'
    })
    weekly_data.to_csv('data/weekly_apple_stock_data.csv')
    return weekly_data
