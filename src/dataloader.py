import yfinance as yf
import numpy as np
from torch.utils.data import Dataset
from torchvision.transforms import Compose

from transforms import Standarize, MinMaxNorm

class StockPriceTimeSeries(Dataset):
    """
    Class that handles time series of stock prices
    """

    def __init__(
        self,
        company:str,
        period:str,
        transforms=None
        ) -> None:
        """
        Initialize new stock price time series

        Parameters:
        - company (string): Company tracker ID
        - period (string): Period of interest 
        """

        self.company = company
        self.period = period
        self.transforms = transforms
        self.historical_data = self.fetch_historical_data()
        self.mean = {col: np.mean(getattr(self.historical_data, col).values) for col in self.historical_data.columns}
        self.std = {col: np.std(getattr(self.historical_data, col).values) for col in self.historical_data.columns}
        self.min = {col: np.min(getattr(self.historical_data, col).values) for col in self.historical_data.columns}
        self.max = {col: np.max(getattr(self.historical_data, col).values) for col in self.historical_data.columns}
       
    def __len__(self):
        return len(self.historical_data)

    def __getitem__(self, index):
        
        sample = {'Date': self.historical_data.index[index], 
                  **{col: getattr(self.historical_data, col).values[index] for col in self.historical_data.columns},
                  **{'mean': self.mean, 'std': self.std, 'min': self.min, 'max': self.max}}
        
        if self.transforms:
            sample = self.transforms(sample)

        return sample


    def fetch_historical_data(self):
        """
        Fetch historical data of the stock price time series
        """

        stock_data = yf.Ticker(self.company)
        historical_data = stock_data.history(period=self.period)

        return historical_data

if __name__ == '__main__':

    stock_price_time_series = StockPriceTimeSeries(
        company='AAPL', 
        period='5d',
        transforms=Compose([Standarize(), MinMaxNorm()])
        )
    stock_price_time_series[4]
    pass
    
