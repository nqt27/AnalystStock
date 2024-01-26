import sqlite3

import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv('data/raw_data/stock_ibm.csv')
# sửa tên cột
df.columns = ["Date","Stock", "Open", "High", "Low", "Close", "Volume"]

df["Volatility"] = round(df["High"] - df["Low"], 4)

print(df.head())


# Kết nối đến SQLite
conn = sqlite3.connect('database/StockAnalyst.db')

# Tạo bảng nếu chưa tồn tại
df.to_sql('stock_ibm', conn, if_exists='replace')

# Lưu các thay đổi và đóng kết nối
conn.commit()
conn.close()

# Lưu trữ phiên bản đã xử lý của dữ liệu
df.to_csv('data/cleaned_data/stock_ibm.csv')
