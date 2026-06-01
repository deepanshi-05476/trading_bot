import hmac
import hashlib
import time
import requests
from urllib.parse import urlencode
from bot.logging_config import setup_logger

logger = setup_logger()

class BinanceClient:
    def __init__(self, api_key: str, api_secret: str, base_url: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "X-MBX-APIKEY": self.api_key
        })

    def _sign(self, params: dict) -> dict:
        params["timestamp"] = int(time.time() * 1000)
        query_string = urlencode(params)
        signature = hmac.new(
            self.api_secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()
        params["signature"] = signature
        return params

    def post(self, endpoint: str, params: dict) -> dict:
        url = f"{self.base_url}{endpoint}"
        params["timestamp"] = int(time.time() * 1000)
        query_string = urlencode(params)
        signature = hmac.new(
            self.api_secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

        # Send signature as separate param, not in body
        query_string = query_string + f"&signature={signature}"

        full_url = f"{url}?{query_string}"
        logger.debug(f"POST {full_url}")

        try:
            response = self.session.post(full_url)
            data = response.json()
            logger.debug(f"RESPONSE: {data}")
            response.raise_for_status()
            return data
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP Error: {e} | Response: {response.text}")
            raise
        except requests.exceptions.ConnectionError:
            logger.error("Network error - could not connect to Binance API")
            raise
