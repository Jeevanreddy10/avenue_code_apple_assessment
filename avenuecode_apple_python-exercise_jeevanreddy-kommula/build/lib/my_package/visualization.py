import matplotlib.pyplot as plt
import mplfinance as mpf

def plot_closing_price(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['AAPL.Close'])
    plt.title('Apple Stock Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Closing Price (USD)')
    plt.grid(True)
    plt.show()

def plot_candlestick_chart(data):
    data = data.rename(columns={
        'AAPL.Open': 'Open',
        'AAPL.High': 'High',
        'AAPL.Low': 'Low',
        'AAPL.Close': 'Close',
        'AAPL.Volume': 'Volume'
    })
    mpf.plot(data, type='candle', style='charles', title='Weekly Apple Stock Prices', volume=True)
