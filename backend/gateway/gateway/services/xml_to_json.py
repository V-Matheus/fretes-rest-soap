"""Convert SOAP XML (EntregaGov) to normalized JSON format."""
import xmltodict


def soap_xml_to_dict(xml_str: str) -> dict:
    """Parse SOAP XML string to a Python dict using xmltodict.

    This expects a structure like:
    <Envelope>..</Envelope>
    and returns a normalized dict for the freight options.
    """
    parsed = xmltodict.parse(xml_str)
    return parsed


def normalize_entregagov(parsed_xml: dict) -> list:
    """Extract freight options from parsed SOAP XML into a list of normalized dicts.

    Normalized shape:
    {
        'provider': 'EntregaGov',
        'service': str,
        'price': float,
        'eta_days': int
    }
    """
    # Attempt to navigate common SOAP envelope/body shapes
    body = parsed_xml.get('Envelope') or parsed_xml.get('soap:Envelope') or parsed_xml
    # Drill down to response payload heuristically
    # Search recursively for 'Frete' or 'frete' entries

    def find_fretes(node):
        hits = []
        if isinstance(node, dict):
            for k, v in node.items():
                if k.lower().endswith('frete') or k.lower().endswith('fretes'):
                    # v may be a list of frete entries, or a dict that wraps the actual 'Frete' list
                    if isinstance(v, list):
                        hits.extend(v)
                    elif isinstance(v, dict):
                        # common SOAP shape: { 'Frete': [ ... ] }
                        inner = v.get('Frete') or v.get('frete')
                        if isinstance(inner, list):
                            hits.extend(inner)
                        elif inner:
                            hits.append(inner)
                        else:
                            hits.append(v)
                    else:
                        hits.append(v)
                else:
                    hits.extend(find_fretes(v))
        elif isinstance(node, list):
            for item in node:
                hits.extend(find_fretes(item))
        return hits

    fretes = find_fretes(body)

    normalized = []
    for f in fretes:
        # handle element names like 'service', 'price', 'eta' with various casings
        service = (
            f.get('service')
            or f.get('Servico')
            or f.get('servico')
            or f.get('nome')
            or f.get('tipo')
            or 'Entrega'
        )
        price = (
            f.get('price')
            or f.get('Price')
            or f.get('valor')
            or f.get('Valor')
            or f.get('preco')
            or f.get('Preco')
            or 0
        )
        eta = (
            f.get('eta')
            or f.get('Eta')
            or f.get('prazo')
            or f.get('Prazo')
            or f.get('dias')
            or f.get('Dias')
            or 0
        )
        try:
            price = float(price)
        except Exception:
            price = 0.0
        try:
            eta = int(eta)
        except Exception:
            eta = 0
        normalized.append({
            'provider': 'EntregaGov',
            'service': service,
            'price': price,
            'eta_days': eta,
        })
    return normalized
