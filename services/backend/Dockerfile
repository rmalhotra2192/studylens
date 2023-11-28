FROM python:3.8-slim-buster

# environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install netcat
RUN apt-get update \
    && apt-get install -y netcat dos2unix \
    && apt-get clean

COPY . .

# port expose
EXPOSE 8000

RUN dos2unix /app/entrypoint.sh && chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]