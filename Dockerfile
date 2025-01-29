FROM python:3.13.0-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN mkdir -p /app/staticfiles && chmod -R 755 /app/staticfiles
RUN mkdir -p /app/media && chmod -R 755 /app/media

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--timeout", "300", "hoteles_responsables.wsgi:application"]