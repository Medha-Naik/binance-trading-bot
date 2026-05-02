def validate_side(side:str)->str:
    if side not in["BUY", "SELL"]:
        raise ValueError(f"Invalid side '{side}'. Must be BUY or SELL.")
    
    return side.upper()

def validate_order_type(type:str)->str:
    if not type in ["MARKET","LIMIT","STOP_MARKET"]:
        raise ValueError(f"Invalid side '{type}'. Must be MARKET, LIMIT or STOP_MARKET")
    
    return type.upper()

def validate_quantity(quantity:float)->float:
    if not quantity>0:
        raise ValueError(f"Invalid quantity'{quantity}'")
    
    return quantity

def validate_price(price:float)->float:
    if not price>0:
        raise ValueError(f"Invalid price'{price}'")
    
    return price