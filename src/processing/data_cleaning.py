import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv('../../data/raw_data/stock_ibm.csv')
# sửa tên cột
df.columns = ["Date","Stock", "Open", "High", "Low", "Close", "Volume"]

df["Volatility"] = df["High"] - df["Low"]

print(df.head())


# Lưu trữ phiên bản đã xử lý của dữ liệu
df.to_csv('../../data/cleaned_data/stock_ibm.csv')
