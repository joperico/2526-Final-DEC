# Imagen base
FROM python:3.11-slim

# Evita que Python genere archivos .pyc y permite ver logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalamos dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código
COPY fuentes .

# Exponemos el puerto de FastAPI
EXPOSE 8000

# Comando para arrancar la aplicación
CMD ["uvicorn", "miapp:app", "--host", "0.0.0.0", "--port", "8000"]