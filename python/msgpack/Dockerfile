FROM python:2.7.14-alpine3.6

WORKDIR /usr/src/app

COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["python","comparison.py"]
