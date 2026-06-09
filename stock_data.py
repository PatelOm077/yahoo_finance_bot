import os
import requests
import yfinance as yf
from dotenv import load_dotenv

load_dotenv()
news_api_key = os.getenv('NEWS_API_KEY')


def get_stock_price(ticker, period):
    stock = yf.Ticker(ticker)
    try:
        data = stock.history(period)
    except Exception as e:
        return f"Error: {e}"
    if data.empty:
        return f"No data for {ticker}"
    return data["Close"]


def stock_balance_sheet(ticker):
    stock = yf.Ticker(ticker)
    try:
        balance_sheet = stock.balance_sheet
    except Exception as e:
        return f"Error: {e}"
    if balance_sheet.empty:
        return f"No data for {ticker}"
    return balance_sheet


def get_stock_news(stock_name):
    url = "https://newsdata.io/api/1/latest"
    params = {
        "q": stock_name,
        "country": "in",
        "apikey": news_api_key,
        "language": "en"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
    except requests.exceptions.RequestException as e:
        return f"Network error {e}"
    if data.get("status") != "success":
        return f"Api error: {data.get('message', 'unknown error')}"
    articles = data.get("results", [])
    if not articles:
        return f"No news articles found for {stock_name}"
    result = ""
    for article in articles:
        result += f"{article['title']}\n{article['link']}\n"
    return result
