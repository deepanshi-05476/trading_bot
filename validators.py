VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]

def validate_symbol(symbol: str) -> str:
    if not symbol or len(symbol) < 3:
        raise ValueError(f"Invalid symbol: '{symbol}'. Example: BTCUSDT")
    return symbol.upper()

def validate_side(side: str) -> str:
    if side.upper() not in VALID_SIDES:
        raise ValueError(f"Invalid side: '{side}'. Must be one of {VALID_SIDES}")
    return side.upper()

def validate_order_type(order_type: str) -> str:
    if order_type.upper() not in VALID_ORDER_TYPES:
        raise ValueError(f"Invalid order type: '{order_type}'. Must be one of {VALID_ORDER_TYPES}")
    return order_type.upper()

def validate_quantity(quantity: str) -> float:
    try:
        qty = float(quantity)
        if qty <= 0:
            raise ValueError()
        return qty
    except ValueError:
        raise ValueError(f"Invalid quantity: '{quantity}'. Must be a positive number. Example: 0.01")

def validate_price(price: str) -> float:
    try:
        p = float(price)
        if p <= 0:
            raise ValueError()
        return p
    except ValueError:
        raise ValueError(f"Invalid price: '{price}'. Must be a positive number. Example: 30000.5")

def validate_inputs(symbol, side, order_type, quantity, price=None):
    symbol = validate_symbol(symbol)
    side = validate_side(side)
    order_type = validate_order_type(order_type)
    quantity = validate_quantity(quantity)

    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders. Use --price flag.")
        price = validate_price(price)

    return symbol, side, order_type, quantity, price