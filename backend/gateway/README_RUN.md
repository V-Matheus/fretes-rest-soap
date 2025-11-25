Run the Django gateway (development):

1. Create a virtualenv and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install django
```

2. Start the Django dev server:

```bash
python manage.py runserver 8000
```

3. Example requests (assuming provider services run on ports 8001 and 8002):

```
GET http://localhost:8000/api/fretes?cep=01001000
```

Environment variables:
- FLASHLOG_URL - URL for FlashLog REST API (default: http://localhost:8001)
- ENTREGAGOV_URL - URL for EntregaGov SOAP endpoint (default: http://localhost:8002)
