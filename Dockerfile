# Dockerfile
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python manage.py migrate
RUN python create_dummy_employee.py

# Collect static files
RUN python manage.py collectstatic --noinput

RUN chmod -R 755 /app/static
RUN ls -l /app
EXPOSE 8000

CMD ["gunicorn", "initium.wsgi:application", "--bind", "0.0.0.0:8000"]
