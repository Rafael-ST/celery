FROM python:3

RUN mkdir /www
WORKDIR /www

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /www/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# COPY . /usr/src/app/

# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]