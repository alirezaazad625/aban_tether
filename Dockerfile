FROM python:3.9.6-alpine

RUN mkdir -p /app

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY src /app/src

ENTRYPOINT ["python", "-m" ,"src.app"]