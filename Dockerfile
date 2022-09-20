FROM python:3.10
ARG $port 
ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

WORKDIR /
COPY . .

RUN pip install pipenv
RUN pipenv install
ENV $PORT=$port
EXPOSE $PORT

CMD ["pipenv", "run", "start"]


