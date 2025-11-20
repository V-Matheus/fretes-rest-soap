from django.http import JsonResponse
from django.views import View

from .services.rest_client import FlashLogClient
from .services.soap_client import EntregaGovClient
from .services.xml_to_json import soap_xml_to_dict, normalize_entregagov
from .services.aggregator import normalize_flashlog, merge_options


class FretesView(View):
    def get(self, request):
        cep = request.GET.get('cep')
        if not cep:
            return JsonResponse({'error': 'cep query param required'}, status=400)

        # For simplicity read service URLs from environment variables
        import os
        flash_url = os.environ.get('FLASHLOG_URL', 'http://localhost:8001')
        entregagov_url = os.environ.get('ENTREGAGOV_URL', 'http://localhost:8002')

        flash_client = FlashLogClient(flash_url)
        entrega_client = EntregaGovClient(entregagov_url)

        # Call FlashLog (REST)
        try:
            flash_json = flash_client.get_fretes(cep)
            flash_norm = normalize_flashlog(flash_json)
        except Exception as e:
            flash_norm = []

        # Call EntregaGov (SOAP)
        try:
            xml = entrega_client.get_fretes_xml(cep)
            parsed = soap_xml_to_dict(xml)
            entrega_norm = normalize_entregagov(parsed)
        except Exception as e:
            entrega_norm = []

        merged = merge_options(flash_norm, entrega_norm)
        return JsonResponse({'options': merged})
