FROM python:3.10
ARG $port 
ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

WORKDIR /
COPY . .

RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy


ENV PORT=$port

EXPOSE $PORT

CMD exec python main.py
