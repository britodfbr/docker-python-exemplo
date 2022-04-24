FROM python:2.7-alpine
#RUN apk update && apk --no-cache --update add build-base
RUN apk update && apk add --virtual build-dependencies
ADD . /code
WORKDIR /code
RUN pip install flask redis toml pathlib2
CMD python main.py
#RUN pip install -U pip  \
#    && pip install poetry==1.1.10 \
#    && poetry install
#CMD ["poetry", "run", "python", "main.py"]
