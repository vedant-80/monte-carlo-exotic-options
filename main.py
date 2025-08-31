import yfinance as yf
import numpy as np
import requests
import random

def main(ticker: str, call: bool, strike: float, T: int, N: int, option: str, accelerated: bool):
    data = yf.download(ticker, start='2020-01-01', end='2025-01-01')
    opens = data['Open'].to_numpy().ravel()
    percent_change_samples = np.empty((N, T))
    price_samples = np.empty((N, T + 1)) # +1 to account for strike price at time 0
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
    idxs = np.random.randint(1, len(opens), size=T)
    prev_idxs = idxs - 1
    samples = (opens[idxs] - opens[prev_idxs]) / opens[prev_idxs]
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
    prices = strike * np.cumprod(1 + samples)
    prices = np.insert(prices, 0, strike)
    return prices



if __name__ == "__main__":
    main("AAPL", True, 150, 30, 10, "asian", False)