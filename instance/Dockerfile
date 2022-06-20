FROM python:3.8-slim-buster

WORKDIR /app  

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY instance.py .


EXPOSE 2003

CMD ["python", "instance.py"]