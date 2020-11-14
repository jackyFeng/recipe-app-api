FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

# copy from local file system onto Docker image
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
# install the temp dependencies required while we run the requirements
# alias (called .tmp-build-deps) using --virtual so that all dependencies can be removed later easily
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
# remove the temp dependencies
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user