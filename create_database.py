import yfinance as yf
import pandas as pd
import sqlite3
import time
import os


def create_stock_database(csv_path, db_file="stock_sectors.db"):
    """
    Create an SQLite database of tickers and their sectors from a CSV file.
    Resumes from where it left off if interrupted.
    """
    # Load all tickers from CSV
    print("Loading tickers from CSV...")
    tickers_df = pd.read_csv(csv_path, usecols=["Symbol"])
    tickers = tickers_df["Symbol"].tolist()
    print(f"Found {len(tickers)} tickers.")

    # Connect to SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create table if it doesn’t exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stocks (
            ticker TEXT PRIMARY KEY,
            sector TEXT NOT NULL
        )
    """)

    # Get already processed tickers
    cursor.execute("SELECT ticker FROM stocks")
    processed_tickers = set(row[0] for row in cursor.fetchall())
    remaining_tickers = [t for t in tickers if t not in processed_tickers]
    print(f"Already processed: {len(processed_tickers)} tickers. Remaining: {len(remaining_tickers)}")

    # Fetch and store sector data for remaining tickers
    if remaining_tickers:
        print("Fetching sector data from Yahoo Finance for remaining tickers...")
        for i, ticker in enumerate(remaining_tickers):
            try:
                stock = yf.Ticker(ticker)
                info = stock.info
                sector = info.get("sector", "Unknown")

                # Insert into database
                cursor.execute("INSERT OR REPLACE INTO stocks (ticker, sector) VALUES (?, ?)", (ticker, sector))

                if (i + 1) % 100 == 0:  # Commit every 100 entries
                    conn.commit()
                    print(f"Processed {i + 1}/{len(remaining_tickers)} remaining tickers...")

                time.sleep(1)  # Respect API rate limits
            except Exception as e:
                print(f"Error fetching {ticker}: {e}")
                cursor.execute("INSERT OR REPLACE INTO stocks (ticker, sector) VALUES (?, ?)", (ticker, "Unknown"))
                continue

        # Final commit
        conn.commit()
        print(f"Finished processing. Total tickers in database: {len(tickers)}")
    else:
        print("All tickers already processed.")

    # Cleanup
    conn.close()
    print(f"Database updated at {db_file}")


if __name__ == "__main__":
    csv_path = r"C:\Users\suri.shethshelat\Downloads\Yahoo Tickers - nyse_stocks.csv"
    create_stock_database(csv_path)