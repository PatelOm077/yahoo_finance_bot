#So lets describe the functions thing
stock_price_function = {
    "name": "get_stock_price",
    "description":"Get the stock price for the user for the timeframe and the period he asks. Use this whenever the user"
                  "asks for the  stock price for any period",
    "input_schema":{
        "type": "object",
        "properties": {
            "ticker":{
                "type": "string",
                "description": "Stock name and if the Stock is of india add .NS for the Nse stock exchange and.BO for "
                               "bombay stock exchange"
                      },
            "period":{
                "type": "string",
                "description": "How far back to fetch price data. Valid values: '1d', '5d', '1mo', '3mo', '6mo', '1y', "
                               "'2y', '5y', '10y'"
                ", 'max'. Pick based on the user's question — '1d' for current price, '1mo' for recent trends, '1y' for "
                "yearly performance, '5y' or 'max' for long-term."
            }
        },
        "required":["ticker","period"]
    }

}
balance_sheet_function = {
    "name": "stock_balance_sheet",
    "description": "Get the balance sheet (assets, liabilities, equity) and key fundamentals for a company. Use this when the user asks about a company's financial health, fundamentals, debt, assets, or wants a deeper analysis beyond just the price.",
    "input_schema": {
        "type": "object",
        "properties": {
            "ticker": {
                "type": "string",
                "description": "Stock ticker symbol. For Indian NSE stocks append .NS (e.g. 'RELIANCE.NS', 'TCS.NS'). For Indian BSE stocks append .BO. For US stocks use the bare ticker (e.g. 'AAPL', 'GOOGL')."
            }
        },
        "required": ["ticker"]
    }
}


news_function = {
    "name": "get_stock_news",
    "description": "Get recent news headlines about a company or stock. Use this when the user asks about news, recent updates, sentiment, or what's happening with a company.",
    "input_schema": {
        "type": "object",
        "properties": {
            "stock_name": {
                "type": "string",
                "description": "Company or stock name to search news for (e.g. 'Reliance', 'Tata Motors', 'Apple'). Use the plain company name, not the ticker symbol — the news API works better with names than tickers."
            }
        },
        "required": ["stock_name"]
    }
}
tools = [
    stock_price_function,
    balance_sheet_function,
    news_function]

