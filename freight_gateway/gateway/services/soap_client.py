"""Lightweight SOAP client for EntregaGov (example).

This client will be kept simple and return raw XML string. For tests we'll call the xml->json parser directly.
"""
import requests


class EntregaGovClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')

    def get_fretes_xml(self, cep: str) -> str:
        """Call the EntregaGov SOAP endpoint and return raw XML as string."""
        headers = {'Content-Type': 'text/xml; charset=utf-8'}
        # Minimal SOAP envelope example
        envelope = f'''<?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
          <soap:Body>
            <GetFretesRequest xmlns="http://example.org/entregagov">
              <cep>{cep}</cep>
            </GetFretesRequest>
          </soap:Body>
        </soap:Envelope>'''
        resp = requests.post(self.base_url, data=envelope.encode('utf-8'), headers=headers, timeout=10)
        resp.raise_for_status()
        return resp.text
