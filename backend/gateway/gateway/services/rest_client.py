"""Lightweight REST client for FlashLog (example)."""
import requests


class FlashLogClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')

    def get_fretes(self, cep: str) -> dict:
        """Call the FlashLog REST API and return parsed JSON.

        This is a simple wrapper used by the Django view. In tests we can call the normalizer directly.
        """
        url = f"{self.base_url}/fretes?cep={cep}"
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        return resp.json()
