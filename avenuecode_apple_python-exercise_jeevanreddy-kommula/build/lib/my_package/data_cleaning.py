import pandas as pd

def clean_data(data):
    data.drop_duplicates(inplace=True)
    data.sort_values('Date', inplace=True)
    return data

def filter_below_average_volume(data):
    avg_volume = data['AAPL.Volume'].mean()
    filtered_data = data[data['AAPL.Volume'] >= avg_volume]
    filtered_data.to_csv('data/filtered_apple_stock_data.csv', index=False)
    return filtered_data

def add_day_of_week(data):
    data['DayOfWeek'] = pd.to_datetime(data['Date']).dt.day_name()
    return data
