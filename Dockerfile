FROM python:3.8

COPY quiz.json .

ADD main.py .

CMD [ "python", "./main.py" ]