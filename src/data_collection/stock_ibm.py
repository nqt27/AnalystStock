import requests
import pandas as pd

# Thay thế 'YOUR_API_KEY' bằng API key bạn đã nhận được từ Alpha Vantage
api_key = 'HYX1N144T3UI7JUP'
symbol = 'IBM'  # Mã cổ phiếu Apple, bạn có thể thay đổi thành mã khác

# URL để lấy giá cổ phiếu
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={api_key}'

# Gửi yêu cầu GET đến Alpha Vantage API
response = requests.get(url)

# Kiểm tra xem yêu cầu có thành công không
if response.status_code == 200:
    data = response.json()

    df = pd.DataFrame(data['Time Series (Daily)']).T
    df.insert(0, "Stock", symbol)
    df.to_csv("../../data/raw_data/stock_ibm.csv")

else:
    print(f'Error {response.status_code}: {response.text}')