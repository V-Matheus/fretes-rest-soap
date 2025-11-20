"""Aggregator utilities to merge and normalize provider responses."""
from typing import List, Dict


def normalize_flashlog(resp_json: Dict) -> List[Dict]:
    """Normalize FlashLog REST response into common shape.

    Expected FlashLog shape (example):
    {
        'options': [
            {'service': 'Express', 'price': 49.9, 'eta_days': 1},
            ...
        ]
    }
    """
    out = []
    options = resp_json.get('options') or resp_json.get('fretes') or []
    for o in options:
        service = o.get('service') or o.get('name') or 'Flash'
        price = o.get('price') or o.get('valor') or 0
        eta = o.get('eta_days') or o.get('prazo') or o.get('days') or 0
        try:
            price = float(price)
        except Exception:
            price = 0.0
        try:
            eta = int(eta)
        except Exception:
            eta = 0
        out.append({
            'provider': 'FlashLog',
            'service': service,
            'price': price,
            'eta_days': eta,
        })
    return out


def merge_options(*lists):
    """Merge multiple lists of normalized options and return sorted list.

    Sort by price ascending (cheaper first), but also prioritize lower ETA when prices equal.
    """
    merged = []
    for l in lists:
        merged.extend(l)
    merged.sort(key=lambda x: (x.get('price', float('inf')), x.get('eta_days', float('inf'))))
    return merged
