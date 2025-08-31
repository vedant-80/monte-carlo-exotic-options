import yfinance as yf
import numpy as np
import requests
import random

def main(ticker: str, call: bool, strike: float, T: int, N: int, option: str, accelerated: bool):
    data = yf.download(ticker, start='2020-01-01', end='2025-01-01')
    opens = data['Open'].to_numpy().ravel()
    percent_change_samples = np.empty((N, T))
    price_samples = np.empty((N, T))
    for i in range(N):
        percent_change_samples[i] = draw_samples(T, opens)
    for i in range(N):
        price_samples[i] = get_prices(strike, percent_change_samples[i])
    
    print (price_samples)


def draw_samples(T:int, opens:np.ndarray):
    """
    Purpose: to simulate drawing T daily percent changes based on historical data for a stock
    Inputs:
        T - number of days to simulate
        opens - numpy array of historical opening prices for a stock
    Outputs:
        samples - numpy array of T daily percent changes
    """
    samples = np.zeros(T)
    for i in range(T):
        idx = np.random.randint(1, len(opens)) # Will vectorize in future
        daily_return = (opens[idx] - opens[idx-1]) / opens[idx-1]
        samples[i] = daily_return
    return samples
    


def get_prices(strike: float, samples: np.array):
    """
    Purpose: to convert daily percent changes into daily prices
    Inputs:
        strike - the strike price of the option  (i.e, the starting price of the stock)
        samples - numpy array of daily percent changes
    Outputs:
        prices - numpy array of daily prices
    """
    prices = np.zeros(len(samples))
    prices[0] = strike
    previous_price = strike
    for idx in range(1, len(prices)): # Start from 1 since we set 0th price to strike
        new_price = previous_price * (1 + samples[idx])
        prices[idx] = new_price
        previous_price = new_price

    return prices



if __name__ == "__main__":
    main("AAPL", True, 150, 30, 10, "asian", False)