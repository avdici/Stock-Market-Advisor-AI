import yfinance as yf

class StockPriceTimeSeries():
    """
    Class that handles time series of stock prices
    """

    def __init__(
        self,
        company:str,
        period:str
        ) -> None:
        """
        Initialize new stock price time series

        Parameters:
        - company (string): Company tracker ID
        - period (string): Period of interest 
        """

        self.company = company
        self.period = period
        self.historical_data = self.fetch_historical_data()

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
        period='5d'
        )
    print(stock_price_time_series.historical_data)

