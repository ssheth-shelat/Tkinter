import yfinance as yf
import pandas as pd
import time

# # Load the CSV file into a DataFrame
# df = pd.read_csv(r"C:\Users\suri.shethshelat\Downloads\Yahoo Tickers - nyse_stocks.csv")
#
# # Display the first 5 rows
# # print(df.head())
#
# #Fetch data for the third ticker in the DataFrame
# ticker = df["Symbol"].iloc[2]  # Adjust column name as needed
# stock = yf.Ticker(ticker)

# # Get stock info
# # fast_info = stock.fast_info
# # print(fast_info)
# # for key, value in fast_info.items():
# #     print(f"{key}: {value}")
# # info = stock.info
# # print(info)


# Choose a stock (e.g., Apple Inc.)
ticker = "AAPL"

# Fetch stock data
stock = yf.Ticker(ticker)

# Print basic details
# print("Stock Name:", stock.info["longName"])
print("Current Price:", stock.info["currentPrice"])
# print("Market Cap:", stock.info["marketCap"])
# print("52-Week High:", stock.info["fiftyTwoWeekHigh"])
# print("52-Week Low:", stock.info["fiftyTwoWeekLow"])

# Delay to prevent hitting rate limits
time.sleep(5)  # Wait 5 seconds before making another request


