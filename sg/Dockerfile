FROM python:3.8-slim-buster

WORKDIR /app  

COPY requirements.txt .
RUN apt-get update

RUN apt-get -y install awscli

RUN pip install -r requirements.txt

COPY sec.py .


EXPOSE 2002

CMD ["python", "sec.py"]