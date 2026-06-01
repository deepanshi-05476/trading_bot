# Binance Futures Testnet Trading Bot

A lightweight Python CLI trading bot for placing orders on Binance Futures Testnet (USDT-M).


# Project Structure

 Setup Steps

 1. Clone the repository
```bash
git clone https://github.com/yourusername/trading_bot.git
cd trading_bot
```

 2. Install dependencies
```bash
pip install -r requirements.txt
```

 3. Register on Binance Futures Testnet
- Go to https://testnet.binancefuture.com
- Register and log in
- Scroll down to *API Key* section
- Click *Generate* and copy your API Key and Secret Key

 4. Configure environment
Create a `.env` file in the root folder:
```env
API_KEY=testnet_api_key
API_SECRET=testnet_api_secret
BASE_URL=https://testnet.binancefuture.com
```

---

# How to Run

# Place a MARKET order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Place a LIMIT order
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 50000
```

### More examples
```bash
# Buy ETH at market price
python cli.py --symbol ETHUSDT --side BUY --type MARKET --quantity 0.1

# Sell BTC at limit price
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 70000
```

---

#  Sample Output
1. Exmple : 

==================================================
ORDER REQUEST SUMMARY
==================================================
  Symbol     : BTCUSDT
  Side       : SELL
  Type       : LIMIT
  Quantity   : 0.01
  Price      : 72000.0
ORDER RESPONSE
==================================================
  Order ID   : 13672798826
  Status     : NEW
  Executed   : 0.0000
  Avg Price  : 0.00
==================================================
 Order placed successfully!
==================================================

2. Example 
2026-06-01 12:55:26 | INFO | Placing MARKET BUY order | Symbol: BTCUSDT | Qty: 0.01
2026-06-01 12:55:26 | INFO | Order placed successfully | OrderId: 13672669538 | Status: NEW
==================================================
ORDER REQUEST SUMMARY
==================================================
  Symbol     : BTCUSDT
  Side       : BUY
  Type       : MARKET
  Quantity   : 0.01
ORDER RESPONSE
==================================================
  Order ID   : 13672669538
  Status     : NEW
  Executed   : 0.0000
  Avg Price  : 0.00
==================================================
 Order placed successfully!
==================================================

