Freight Aggregator Gateway (Django scaffold)

This project contains a lightweight Django scaffold for a gateway that aggregates freight options
from two services:

- FlashLog (REST): returns expensive & fast options
- EntregaGov (SOAP): returns cheap & slow options (legacy SOAP)

The gateway converts SOAP XML responses to JSON, normalizes both providers' outputs and
returns a unified list.

This workspace includes pure-Python service modules and unit tests so you can run tests
without installing Django.

Quick start (run unit tests):

1. Create a virtualenv and install test requirements:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Files of interest:
- `gateway/services/xml_to_json.py` - converts SOAP XML to JSON
- `gateway/services/aggregator.py` - normalizes and merges provider results
- `tests/test_xml_to_json.py` and `tests/test_aggregator.py` - unit tests
