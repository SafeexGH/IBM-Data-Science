import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# Project Title
# ------------------------------
print("Project Title: Tesla and GameStop Stock and Revenue Analysis")

# ------------------------------
# Question 1: Extract Tesla Stock Data
# ------------------------------
tesla_data = yf.download('TSLA', start='2010-01-01', end='2025-01-01')
tesla_data.reset_index(inplace=True)
print(tesla_data.head())

# ------------------------------
# Question 2: Tesla Revenue Data from CSV
# ------------------------------
tesla_revenue = pd.read_csv(r"C:\Users\Samuel\Downloads\tesla_revenue.csv")
print(tesla_revenue.tail())

# ------------------------------
# Question 3: Extract GME Stock Data
# ------------------------------
gme_data = yf.download('GME', start='2010-01-01', end='2025-01-01')
gme_data.reset_index(inplace=True)
print(gme_data.head())

# ------------------------------
# Question 4: GME Revenue Data from CSV
# ------------------------------
gme_revenue = pd.read_csv(r"C:\Users\Samuel\Downloads\gme_revenue.csv")
print(gme_revenue.tail())

# ------------------------------
# Helper function to plot stock and revenue
# ------------------------------
def make_graph(stock_data, revenue_data, stock_name):
    fig, ax1 = plt.subplots(figsize=(14,6))
    ax1.plot(stock_data['Date'], stock_data['Close'], color='blue')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Stock Price', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    
    ax2 = ax1.twinx()
    ax2.bar(revenue_data['Date'], revenue_data['Revenue'], alpha=0.3, color='orange')
    ax2.set_ylabel('Revenue', color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')
    
    plt.title(f'{stock_name} Stock Price and Revenue Over Time')
    fig.tight_layout()
    plt.show()

# ------------------------------
# Question 5: Tesla Stock and Revenue Dashboard
# ------------------------------
make_graph(tesla_data, tesla_revenue, 'Tesla')

# ------------------------------
# Question 6: GameStop Stock and Revenue Dashboard
# ------------------------------
make_graph(gme_data, gme_revenue, 'GameStop')

# ------------------------------
# Question 7: Sharing your Assignment Notebook
# ------------------------------
print("GitHub/Watson Studio URL: https://example.com")
