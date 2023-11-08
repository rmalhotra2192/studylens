#!/bin/sh

# Wait for the database to be available
echo "Waiting for database..."
while ! python -c "import socket; socket.create_connection(('db', 5432))" 2>/dev/null; do
  sleep 1
done

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start Gunicorn
echo "Starting Gunicorn..."
gunicorn backend.wsgi:application --bind 0.0.0.0:8000