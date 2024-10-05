# Usa una imagen base de Python con Alpine
FROM python:3.12-alpine

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt y lo instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación
COPY . .

# Comando por defecto para ejecutar la aplicación
CMD ["python", "main.py"]