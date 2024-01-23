import pandas as pd

# Đọc dữ liệu từ file CSV
df_stock = pd.read_csv('../../data/raw_data/stock_ibm.csv')
# sửa tên cột
df_stock.columns = ["Date","Stock", "Open", "High", "Low", "Close", "Volume"]

df_stock["Volatility"] = df_stock["High"] - df_stock["Low"]

print(df_stock.head())


# Đọc dữ liệu từ file CSV
df_rsi = pd.read_csv('../../data/raw_data/rsi_ibm.csv')

print(df_rsi.head())
#thêm cột rsi vào df_stock
df_stock["RSI"] = df_rsi["RSI"]

#xử lý dữ liệu thiếu
df_stock["RSI"] = df_stock["RSI"].fillna(df_stock["RSI"].mean())
# Lưu trữ phiên bản đã xử lý của dữ liệu
df_stock.to_csv('../../data/cleaned_data/stock_ibm.csv')
