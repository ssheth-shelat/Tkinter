import yfinance as yf

# Choose a stock (e.g., Apple Inc.)
ticker = "AAPL"

# Fetch stock data
stock = yf.Ticker(ticker)

# Print basic details
print("Stock Name:", stock.info["longName"])
print("Current Price:", stock.info["currentPrice"])
print("Market Cap:", stock.info["marketCap"])
print("52-Week High:", stock.info["fiftyTwoWeekHigh"])
print("52-Week Low:", stock.info["fiftyTwoWeekLow"])
