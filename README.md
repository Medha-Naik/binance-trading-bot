# Binance Futures Trading Bot

A Python CLI application to place orders on Binance Futures Demo environment (USDT-M).

## Features
- Place MARKET and LIMIT orders
- BUY and SELL support
- Input validation
- Structured logging to file and console

## Setup

1. Clone the repository
   git clone https://github.com/Medha-Naik/binance-trading-bot.git
   cd binance-trading-bot

2. Create and activate virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Create a .env file in the root directory
   API_KEY=your_api_key_here
   API_SECRET=your_api_secret_here
   BASE_URL=https://demo-fapi.binance.com

## How to Run

Market Order:
   python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

Limit Order:
   python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 80000

## Arguments
- --symbol   Trading pair (e.g. BTCUSDT)
- --side     BUY or SELL
- --type     MARKET or LIMIT
- --quantity Order quantity
- --price    Price (required for LIMIT orders)

## Assumptions
- Uses Binance Futures Demo environment (demo-fapi.binance.com)
- API keys are stored in a .env file
- Logs are saved to logs/trading_bot.log