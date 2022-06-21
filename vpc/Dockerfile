FROM python:3.8-slim-buster

WORKDIR /app  

COPY requirements.txt .
RUN apt-get update

RUN apt-get -y install awscli

RUN pip install -r requirements.txt

COPY vpc.py .


EXPOSE 2000

CMD ["python", "vpc.py"]