FROM python:3.6-alpine
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY src/ /app
WORKDIR /app

ENV PYTHONUNBUFFERED 0
CMD ["python", "app.py"]
