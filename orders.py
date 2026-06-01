from bot.client import BinanceClient
from bot.logging_config import setup_logger

logger = setup_logger()

class OrderManager:
    def __init__(self, client: BinanceClient):
        self.client = client

    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float = None) -> dict:
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity,
        }

        if order_type.upper() == "LIMIT":
            if price is None:
                raise ValueError("Price is required for LIMIT orders")
            params["price"] = price
            params["timeInForce"] = "GTC"  # Good Till Cancel

        logger.info(f"Placing {order_type} {side} order | Symbol: {symbol} | Qty: {quantity}" + 
                   (f" | Price: {price}" if price else ""))

        response = self.client.post("/fapi/v1/order", params)

        logger.info(f"Order placed successfully | OrderId: {response.get('orderId')} | Status: {response.get('status')}")

        return response

    def print_order_summary(self, request_params: dict, response: dict):
        print("\n" + "="*50)
        print("ORDER REQUEST SUMMARY")
        print("="*50)
        print(f"  Symbol     : {request_params.get('symbol')}")
        print(f"  Side       : {request_params.get('side')}")
        print(f"  Type       : {request_params.get('type')}")
        print(f"  Quantity   : {request_params.get('quantity')}")
        if request_params.get('price'):
            print(f"  Price      : {request_params.get('price')}")

        print("\nORDER RESPONSE")
        print("="*50)
        print(f"  Order ID   : {response.get('orderId')}")
        print(f"  Status     : {response.get('status')}")
        print(f"  Executed   : {response.get('executedQty')}")
        print(f"  Avg Price  : {response.get('avgPrice', 'N/A')}")
        print("="*50)
        print(" Order placed successfully!")
        print("="*50 + "\n")