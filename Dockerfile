FROM ubuntu

ADD requirements.txt requirements.txt
ADD . /repo

RUN apt-get update
RUN apt-get install -y python python-pip mongodb
RUN pip install --upgrade
RUN pip install -r requirements.txt

WORKDIR /repo

CMD service mongodb start && gunicorn server:app --log-file=- --reload --timeout=5 --enable-stdio-inheritance --config config/gunicorn.py

EXPOSE 8000
