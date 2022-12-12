import requests

class Stock_Overview:
    '''
    This class sets up the API to get an overview of the ticker symbol the user inputs
    '''
    def __init__(self, ticker_symbol):
        '''
        This function takes ticker_symbol as an argument which is defined in main. This function defines the 
        api url as an instance variable. 
        '''
        self.url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker_symbol}&apikey=22GO7UY1UVGB2S85"

    def get(self):
        '''
        This function gets the information from the api url and returns it.
        '''
        response = requests.get(self.url).json()
        return response
        
