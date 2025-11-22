from django.http import HttpResponse, JsonResponse
from django.views import View
import os
import json


class OpenApiJsonView(View):
    def get(self, request):
        base = os.path.dirname(__file__)
        path = os.path.join(base, 'openapi.json')
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return JsonResponse(data, safe=False)
        except FileNotFoundError:
            return JsonResponse({'error': 'openapi.json not found'}, status=500)


class DocsView(View):
    def get(self, request):
        # Simple Swagger UI HTML that loads the local openapi.json
        html = '''<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <title>API Docs</title>
  <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@4/swagger-ui.css" />
</head>
<body>
  <div id="swagger-ui"></div>
  <script src="https://unpkg.com/swagger-ui-dist@4/swagger-ui-bundle.js"></script>
  <script>
    window.onload = function() {
      SwaggerUIBundle({
        url: '/api/docs/openapi.json',
        dom_id: '#swagger-ui'
      })
    }
  </script>
</body>
</html>'''
        return HttpResponse(html)
