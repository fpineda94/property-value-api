FROM python:3.11-slim
#Crea carpeta principal dentro del contenedor
WORKDIR /app
#Copia dependencias de requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#Copia todo el codigo en el contenedor 
COPY . .
EXPOSE 8000
CMD [ "uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000" ]
