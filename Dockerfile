FROM python:3.10

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

WORKDIR /
COPY . .

RUN pip install pipenv
RUN pipenv install

CMD ["pipenv", "run", "start"]

EXPOSE 5000
