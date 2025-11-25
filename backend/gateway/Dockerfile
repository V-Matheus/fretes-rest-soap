FROM python:3.11-slim
WORKDIR /app

# Install only production requirements
COPY requirements.prod.txt ./
RUN pip install --no-cache-dir -r requirements.prod.txt

# Copy only the Django app
COPY freight_gateway ./freight_gateway
COPY gateway ./gateway
COPY manage.py ./manage.py

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
