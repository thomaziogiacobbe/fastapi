FROM python:3.12

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 8000

WORKDIR /app/src

CMD [ "uvicorn", "--host=0.0.0.0", "--port=8000", "--reload", "main:app"]