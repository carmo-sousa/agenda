FROM python:3.10

RUN useradd metatron

USER metatron:metatron
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
COPY . /app

CMD [ "tail", "-f", "/dev/null" ]
