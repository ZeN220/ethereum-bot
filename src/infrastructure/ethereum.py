from typing import Optional

from aiohttp import ClientSession


class Etherscan:
    def __init__(self, api_key: str, session: Optional[ClientSession] = None):
        self.api_key = api_key
        self.session = session or ClientSession()

    async def _get_balance(self, address: str) -> int:
        url = "https://api.etherscan.io/api"
        params = {
            "module": "account",
            "action": "balance",
            "address": address,
            "tag": "latest",
            "apikey": self.api_key,
        }
        async with self.session.get(url, params=params) as response:
            data = await response.json()
            return int(data["result"])

    async def get_balance(self, address: str) -> int:
        balance_as_wei = await self._get_balance(address)
        return balance_as_wei / 10**18
