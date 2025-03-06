import yfinance as yf
import pandas as pd
import json
import time


def run_stock_screener(json_file_path):
    """
    Run the stock screener based on user preferences and return the best stock ticker.
    Limited to the first column and first 300 rows of the CSV file.

    Args:
        json_file_path (str): Path to the JSON file containing user preferences.

    Returns:
        str or None: Recommended stock ticker or None if no match is found.
    """
    # Load user preferences
    try:
        with open(json_file_path, "r") as f:
            user_prefs = json.load(f)
    except FileNotFoundError:
        print("Error: user_preferences.json not found.")
        return None

    # Load stock tickers from CSV (first column, first 300 rows)
    try:
        tickers_df = pd.read_csv(
            r"C:\Users\suri.shethshelat\Downloads\Yahoo Tickers - nyse_stocks.csv",  # Raw string with 'r'
            usecols=["Symbol"],  # Read only the "Symbol" column
            nrows=50  # Limit to the first 300 rows
        )
        tickers = tickers_df["Symbol"].tolist()
    except FileNotFoundError:
        print("Error: NYSE tickers CSV file not found.")
        return None
    except KeyError:
        print("Error: 'Symbol' column not found in the CSV file.")
        return None

    # Filter logic based on user preferences
    selected_stock = None
    best_score = -1

    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info

            # Extract stock metrics
            sector = info.get("sector", "Unknown")
            beta = info.get("beta", 1)
            price = info.get("currentPrice", 0)
            dividend_yield = info.get("dividendYield", 0)

            # Match user preferences with scoring
            score = 0
            if user_prefs["sector"] in ["No Clue", sector]:
                score += 2
            if user_prefs["risk_tolerance"] == "Aggressive" and beta > 1:
                score += 1
            elif user_prefs["risk_tolerance"] == "Conservative" and beta < 1:
                score += 1
            if user_prefs["money_total"] >= price:
                score += 2
            if user_prefs["goal"] == "Diversification of Income" and dividend_yield > 0:
                score += 2

            # Select the best match
            if score > best_score:
                best_score = score
                selected_stock = ticker

            time.sleep(1)  # 1-second delay to respect API rate limits
        except Exception as e:
            print(f"Error processing ticker {ticker}: {e}")
            continue

    return selected_stock


# For standalone testing
if __name__ == "__main__":
    result = run_stock_screener("user_preferences.json")
    if result:
        print(f"Best stock recommendation: {result}")
    else:
        print("No suitable stock found.")



# import yfinance as yf
# import pandas as pd
# import time
#
# # Load the CSV file into a DataFrame
# df = pd.read_csv(r"C:\Users\suri.shethshelat\Downloads\Yahoo Tickers - nyse_stocks.csv")
#
# # Display the first 5 rows
# # print(df.head())
#
# #Fetch data for the third ticker in the DataFrame
# ticker = df["Symbol"].iloc[2]  # Adjust column name as needed
# stock = yf.Ticker(ticker)
#
# # Get stock info
# # fast_info = stock.fast_info
# # print(fast_info)
# # for key, value in fast_info.items():
# #     print(f"{key}: {value}")
# # info = stock.info
# # print(info)
#
# # Delay to prevent hitting rate limits
# time.sleep(5)  # Wait 5 seconds before making another request
#
#
# # Choose a stock (e.g., Apple Inc.)
# # ticker = "AAPL"
# #
# # # Fetch stock data
# # stock = yf.Ticker(ticker)
# #
# # # Print basic details
# # # print("Stock Name:", stock.info["longName"])
# # print("Current Price:", stock.info["currentPrice"])
# # # print("Market Cap:", stock.info["marketCap"])
# # # print("52-Week High:", stock.info["fiftyTwoWeekHigh"])
# # print("52-Week Low:", stock.info["fiftyTwoWeekLow"])
#
# # Delay to prevent hitting rate limits
# time.sleep(5)  # Wait 5 seconds before making another request
