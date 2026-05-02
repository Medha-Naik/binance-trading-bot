from bot.client import BinanceClient
from bot.validators import validate_order_type,validate_price,validate_quantity,validate_side
from bot.logging_config import setup_logger

logger=setup_logger("orders")

def place_market_order(symbol:str, side:str, quantity:float)->dict:
    side=validate_side(side)
    quantity=validate_quantity(quantity)
    client=BinanceClient()
    params={
        "symbol":symbol,
        "side":side,
        "type":"MARKET",
        "quantity":quantity
    }
    logger.info(f"Placing MARKET {side} order | {symbol} |qty:{quantity}")
    return client.post("/fapi/v1/order",params)

def place_limit_order(symbol:str,side:str,quantity:float,price:float)->dict:
    side=validate_side(side)
    quantity=validate_quantity(quantity)
    price=validate_price(price)
    client=BinanceClient()
    params={
        "symbol":symbol,
        "side":side,
        "type":"LIMIT",
        "quantity":quantity,
        "price":price,
        "timeInForce":"GTC"
    }
    logger.info(f"Placing LIMIT {side} order | {symbol} | qty:{quantity} | price: {price}")
    return client.post("/fapi/v1/order",params)