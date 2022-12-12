import stock_priceAPI
import stock_overviewAPI

def main():
    '''
    This function adds both of the api's together in order to allow the user to 
    type in a ticker symbol and then in return receive information about that company.
    '''
    ticker = input("Enter a ticker symbol: ")

    stockprice = stock_priceAPI.Stockprice(ticker)
    stockoverview = stock_overviewAPI.Stock_Overview(ticker)
    overview = stockoverview.get()
    price = stockprice.get()

    current_price = price['price']
    sector = overview['Sector']
    name = overview['Name']
    description = overview['Description']
    exchange = overview['Exchange']
    market_cap = overview['MarketCapitalization']
    dividend_per_share = overview['DividendPerShare']
    fifty2_high = overview['52WeekHigh']
    fifty2_low = overview['52WeekLow']

    print(f"==\nName: {name}\n==\nCurrent Price: {current_price}\n==\nDescription: {description}\n==\nSector: {sector}\n==\nExchange: {exchange}\n==\nMarket Cap: {market_cap}\n==\nDividend Payout: {dividend_per_share}\n==\n52 Week High: {fifty2_high}\n==\n52 Week Low: {fifty2_low}\n==")

main()