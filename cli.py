import argparse
import os
from dotenv import load_dotenv
from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import validate_inputs
from bot.logging_config import setup_logger

load_dotenv()
logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(
        description="🤖 Binance Futures Testnet Trading Bot",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("--symbol",     required=True,  help="Trading pair e.g. BTCUSDT")
    parser.add_argument("--side",       required=True,  help="BUY or SELL")
    parser.add_argument("--type",       required=True,  dest="order_type", help="MARKET or LIMIT")
    parser.add_argument("--quantity",   required=True,  help="Order quantity e.g. 0.01")
    parser.add_argument("--price",      required=False, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    try:
        # Validate all inputs
        symbol, side, order_type, quantity, price = validate_inputs(
            args.symbol,
            args.side,
            args.order_type,
            args.quantity,
            args.price
        )

        # Load credentials
        api_key    = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")
        base_url   = os.getenv("BASE_URL", "https://testnet.binancefuture.com")

        if not api_key or not api_secret:
            raise ValueError("API_KEY and API_SECRET must be set in .env file")

        # Initialize client and order manager
        client  = BinanceClient(api_key, api_secret, base_url)
        manager = OrderManager(client)

        # Place order
        request_params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "price": price
        }

        response = manager.place_order(symbol, side, order_type, quantity, price)
        manager.print_order_summary(request_params, response)

    except ValueError as e:
        logger.error(f"Validation error: {e}")
        print(f"\n Error: {e}\n")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"\n Unexpected error: {e}\n")

if __name__ == "__main__":
    main()