FROM python:3.6.8

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

# pip install requirements
RUN pip install -r requirements.txt

CMD ["uwsgi", "config.ini"]