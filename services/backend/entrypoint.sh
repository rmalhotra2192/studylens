#!/bin/sh

# Wait for the database to be available
echo "Waiting for database..."
while ! python -c "import socket; socket.create_connection(('db', 5432))" 2>/dev/null; do
  sleep 1
done

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Wait for Elasticsearch to be up and running
echo "Waiting for Elasticsearch..."
while ! nc -z elasticsearch 9200; do
  sleep 1
done
echo "Elasticsearch is up and running"

# Create the Elasticsearch indices or rebuild them
echo "Creating Elasticsearch indices..."
# python manage.py search_index --create
echo "y" | python manage.py search_index --rebuild

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start Gunicorn
echo "Starting Gunicorn..."
gunicorn backend.wsgi:application --bind 0.0.0.0:8000


