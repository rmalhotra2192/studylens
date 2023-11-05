FROM python:3.8-slim-buster

# environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

# port expose
EXPOSE 8001

# run application
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]