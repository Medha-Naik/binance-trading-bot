import hmac
import hashlib
import time
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv
import os
from bot.logging_config import setup_logger

logger=setup_logger("client")

class BinanceClient:
    def __init__(self):
        load_dotenv()
        self.api_key=os.getenv("API_KEY")
        self.api_secret=os.getenv("API_SECRET")
        self.base_url=os.getenv("BASE_URL")
        self.session=requests.Session()
        self.session.headers.update({"X-MBX-APIKEY":self.api_key})
        

    def _sign(self,params:dict)->dict:
        params["recvWindow"]=60000
        params["timestamp"]=int(time.time()*1000)
        
        query_string=urlencode(params)
        signature=hmac.new(
            self.api_secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256
            ).hexdigest()
        params["signature"]=signature
        

        return params
        

    def post(self,endpoint:str,params:dict)->dict:
        url=f"{self.base_url}{endpoint}"
        signed_params=self._sign(params)
        logger.debug(f"POST {url} | params: {signed_params}")

        try:
            response=self.session.post(url,params=signed_params)
            data=response.json()
            if response.status_code!=200:
                logger.error(f"API error:{data}")
                raise Exception(f"API error:{data.get('msg','Unknown Error')}")
            else:
                logger.info(f"Response:{data}")
        
            return data
        
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error:{e}")
            raise