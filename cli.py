from bot.orders import place_limit_order,place_market_order
from bot.logging_config import setup_logger
import argparse


logger=setup_logger("cli")

def main():
    parser=argparse.ArgumentParser(description="Binance Futures Trading Bot")
    parser.add_argument("--symbol",required=True,help="Trading pair e.g. BTCUSDT")
    parser.add_argument("--side", required=True,help="BUY or SELL")
    parser.add_argument("--type",required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity",required=True,type=float,help="Order quantity")
    parser.add_argument("--price",type=float,help="Price for LIMIT orders")

    args=parser.parse_args()

    logger.info(f"Order request | symbol: {args.symbol} | side: {args.side} | type: {args.type} | qty: {args.quantity} | price: {args.price}")

    try:
        if args.type=="MARKET":
           result= place_market_order(args.symbol,args.side,args.quantity)
        elif args.type =="LIMIT":
            result=place_limit_order(args.symbol,args.side,args.quantity,args.price)

        print("\n Order Placed succesfully!")
        print(f"Order ID: {result.get('orderId')}")
        print(f"Status: {result.get('status')}")
        print(f" Symbol : {result.get('symbol')}")
        print(f"Executed :{result.get('executedQty')}")
        print(f"Avg Price :{result.get('avgPrice')}\n")
        logger.info(f"Order success | orderId: {result.get('orderId')} | status:{result.get('status')}")
    
    except ValueError as e:
        print(f"\n Validation error:{e}\n")
        logger.error(f"Validation error: {e}")
    except Exception as e:
        print(f"\n Error:{e}\n")
        logger.error(f"Unexpected error:{e}")


if __name__=="__main__":
        main()