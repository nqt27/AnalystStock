import requests
import pandas as pd

# Thay thế 'YOUR_API_KEY' bằng API key bạn đã nhận được từ Alpha Vantage
api_key = 'HYX1N144T3UI7JUP'
symbol = 'IBM'  # Mã cổ phiếu IBM, bạn có thể thay đổi thành mã khác
interval = 'weekly'  # Khoảng thời gian (daily, weekly, monthly) - thay đổi theo nhu cầu
time_period = 10  # Số ngày được sử dụng để tính RSI - thay đổi theo nhu cầu
series_type = 'open'  # Loại dữ liệu sử dụng cho RSI (open, high, low, close) - thay đổi theo nhu cầu

# URL để lấy dữ liệu RSI
url = f'https://www.alphavantage.co/query?function=RSI&symbol={symbol}&interval={interval}&time_period={time_period}&series_type={series_type}&apikey={api_key}'

# Gửi yêu cầu GET đến Alpha Vantage API
response = requests.get(url)

# Kiểm tra xem yêu cầu có thành công không
if response.status_code == 200:
    data = response.json()

    # Chuyển đổi dữ liệu thành DataFrame
    df = pd.DataFrame(data[f'Technical Analysis: RSI']).T

    # Thêm cột mã cổ phiếu
    df.insert(0, "Stock", symbol)

    # Chuyển đổi định dạng cột ngày thành datetime
    df.index = pd.to_datetime(df.index)

    # Lưu dữ liệu vào tệp CSV
    df.to_csv(f"data/raw_data/rsi_{symbol.lower()}.csv")
    print(f"Dữ liệu RSI đã được lưu vào rsi_{symbol.lower()}.csv")

else:
    print(f'Error {response.status_code}: {response.text}')
