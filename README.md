# Stock Analysis Tool

A conversational stock research assistant powered by Claude AI and Gradio. Ask questions about any stock in plain English — it fetches real-time prices, fundamentals, and news, then gives you a concise analysis.

## Features

- **Real-time stock prices** — historical data for any period (1 day to max) via Yahoo Finance
- **Fundamentals** — balance sheet, income statement, and key ratios
- **Latest news** — recent headlines with sentiment summary via NewsData.io
- **Indian & US stocks** — handles NSE/BSE (`.NS`/`.BO` suffixes) and US tickers automatically
- **Natural language** — type "Tata Motors" or "Reliance" without worrying about ticker formats
- **Streaming responses** — answers stream in real time through a Gradio chat UI

## How It Works

The Gradio chat interface passes your messages to Claude (claude-sonnet-4-6). Claude decides which tool to call (price, fundamentals, or news), the tool fetches live data, and Claude returns an interpreted summary — not just raw numbers.

```
User message → Claude → tool call → live data → Claude analysis → streamed response
```

## Setup

### Prerequisites

- Python 3.10+
- An [Anthropic API key](https://console.anthropic.com/)
- A [NewsData.io API key](https://newsdata.io/)

### Installation

```bash
pip install anthropic gradio yfinance python-dotenv requests
```

### Environment Variables

Create a `.env` file in the project root:

```
ANTHROPIC_API_KEY=your_anthropic_api_key
NEWS_API_KEY=your_newsdata_api_key
```

### Run

```bash
python main.py
```

Then open the local URL printed in the terminal (usually `http://127.0.0.1:7860`).

## Usage Examples

| You type | What happens |
|---|---|
| `"What's the price of Reliance?"` | Fetches current price for `RELIANCE.NS` |
| `"Show me Apple's fundamentals"` | Pulls balance sheet and key ratios for `AAPL` |
| `"Any news on Tata Motors?"` | Gets latest headlines and gives a sentiment read |
| `"How has TCS done over the last year?"` | Fetches 1y price history for `TCS.NS` |

## Project Structure

```
├── main.py                     # Gradio app entry point
├── chat.py                     # Chat loop with streaming + tool handling
├── system_message.py           # Claude system prompt
├── dictionaries_for_functions.py  # Tool definitions for Claude
├── tool_handling_function.py   # Dispatches tool calls to data functions
├── stock_data.py               # yfinance + NewsData.io data fetchers
└── .env                        # API keys (not committed)
```

## Tech Stack

- [Anthropic Claude](https://www.anthropic.com/) — AI reasoning and tool use
- [Gradio](https://gradio.app/) — chat UI
- [yfinance](https://github.com/ranaroussi/yfinance) — Yahoo Finance data
- [NewsData.io](https://newsdata.io/) — news headlines
