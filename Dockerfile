# Usa una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt si tienes o lo creamos aquí
COPY requirements.txt requirements.txt

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el contenido del proyecto al contenedor
COPY . .

# Exponer el puerto que Flask usará
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
