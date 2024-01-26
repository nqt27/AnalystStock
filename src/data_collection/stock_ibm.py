import requests
import pandas as pd

# Thay thế 'YOUR_API_KEY' bằng API key bạn đã nhận được từ Alpha Vantage
api_key = 'HYX1N144T3UI7JUP'
symbol = 'IBM'  # Mã cổ phiếu IBM, bạn có thể thay đổi thành mã khác

# URL để lấy giá cổ phiếu
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={api_key}'

# Gửi yêu cầu GET đến Alpha Vantage API
response = requests.get(url)

# Kiểm tra xem yêu cầu có thành công không
if response.status_code == 200:
    data = response.json()

    # Chuyển đổi dữ liệu thành DataFrame
    df = pd.DataFrame(data['Time Series (Daily)']).T

    # Thêm cột mã cổ phiếu
    df.insert(0, "Stock", symbol)

    # Chuyển đổi định dạng cột ngày thành datetime
    df.index = pd.to_datetime(df.index)

    # Lưu dữ liệu vào tệp CSV
    df.to_csv(f"data/raw_data/stock_{symbol.lower()}.csv")
    print(f"Dữ liệu đã được lưu vào stock_{symbol.lower()}.csv")

else:
    print(f'Error {response.status_code}: {response.text}')
