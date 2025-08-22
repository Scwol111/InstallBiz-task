FROM python

RUN apt -y update && apt -y upgrade

RUN mkdir /service

WORKDIR /service

COPY . .
RUN pip3 install poetry
RUN poetry install --no-root

EXPOSE 8000