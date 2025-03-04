import yfinance as yf
import pandas as pd
import time

# Load the CSV file into a DataFrame
df = pd.read_csv(r"C:\Users\suri.shethshelat\Downloads\Yahoo Tickers - nyse_stocks.csv")

# Display the first 5 rows
# print(df.head())

#Fetch data for the third ticker in the DataFrame
ticker = df["Symbol"].iloc[2]  # Adjust column name as needed
stock = yf.Ticker(ticker)

# Get stock info
# fast_info = stock.fast_info
# print(fast_info)
# for key, value in fast_info.items():
#     print(f"{key}: {value}")
# info = stock.info
# print(info)

# Delay to prevent hitting rate limits
time.sleep(5)  # Wait 5 seconds before making another request


# Choose a stock (e.g., Apple Inc.)
# ticker = "AAPL"
#
# # Fetch stock data
# stock = yf.Ticker(ticker)
#
# # Print basic details
# # print("Stock Name:", stock.info["longName"])
# print("Current Price:", stock.info["currentPrice"])
# # print("Market Cap:", stock.info["marketCap"])
# # print("52-Week High:", stock.info["fiftyTwoWeekHigh"])
# print("52-Week Low:", stock.info["fiftyTwoWeekLow"])

# Delay to prevent hitting rate limits
time.sleep(5)  # Wait 5 seconds before making another request

'''
import yfinance as yf
import pandas as pd
import json
import time

# Load user preferences
with open("user_preferences.json", "r") as f:
    user_prefs = json.load(f)

# Load stock tickers from CSV
tickers_df = pd.read_csv("stocks.csv")  # Ensure the file exists
tickers = tickers_df["Symbol"].tolist()

# Filter logic based on user preferences
selected_stock = None
best_score = -1

for ticker in tickers[:50]:  # Limit API calls for testing
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        
        # Extract stock metrics
        sector = info.get("sector", "Unknown")
        beta = info.get("beta", 1)
        price = info.get("currentPrice", 0)
        dividend_yield = info.get("dividendYield", 0)

        # Match user preferences
        score = 0
        if user_prefs["preferred_sector"] in ["No Preference", sector]:
            score += 2
        
        if user_prefs["risk_tolerance"] == "Aggressive" and beta > 1:
            score += 1
        elif user_prefs["risk_tolerance"] == "Conservative" and beta < 1:
            score += 1
        
        if user_prefs["total_investment"] >= price:
            score += 2
        
        if user_prefs["goal"] == "Diversification" and dividend_yield > 0.02:
            score += 2
        
        # Select the best match
        if score > best_score:
            best_score = score
            selected_stock = ticker

        time.sleep(1)  # Avoid rate limit
    except Exception:
        continue

print(f"Best stock recommendation: {selected_stock}")

'''


