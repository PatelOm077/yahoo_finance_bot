#Lets make the handle tool function
from stock_data import get_stock_price, stock_balance_sheet, get_stock_news


def handle_tool(message):
    tool_results = []

    for block in message.content:
        if block.type == "tool_use":
            if block.name == "get_stock_price":
                ticker = block.input.get("ticker")
                period = block.input.get("period")
                result=get_stock_price(ticker, period)
            elif block.name == "stock_balance_sheet":
                ticker = block.input.get("ticker")
                result=stock_balance_sheet(ticker)
            elif block.name == "get_stock_news":
                stock_name = block.input.get("stock_name")
                result=get_stock_news(stock_name)

            tool_results.append({
              "type": "tool_result",
              "tool_use_id":block.id,
             "content": str(result),
            })

    return {"role":"user","content":tool_results}


