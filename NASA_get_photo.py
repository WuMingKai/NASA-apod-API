import requests

#API密鑰
api_key = "YourAPIKey"
#API網址
url = "https://api.nasa.gov/planetary/apod"
#API參數
params = {
    "api_key": api_key
}

#發送API請求
response = requests.get(url, params=params)
#取得API的返回值
data = response.json()
print("Picture URL:", data["hdurl"])