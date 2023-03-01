FROM python:3.8-slim

RUN mkdir /app
WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]