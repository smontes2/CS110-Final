import requests

class Stockprice:
    '''
    This class sets up the API to get the current stock price of the ticker symbol the user inputs
    '''
    def __init__(self, ticker_symbol):
        '''
        This function takes ticker_symbol as an argument which is defined in main. This function defines the 
        api url as an instance variable. 
        '''
        self.url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey=43620a19078c459ea22098c6bddae06d"

    def get(self):
        '''
        This function gets the information from the api url and returns it.
        '''
        response = requests.get(self.url).json()
        return response
