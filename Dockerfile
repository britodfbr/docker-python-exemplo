FROM python:2.7
ADD . /code
WORKDIR /code
RUN pip install poetry && poetry install
CMD ["python", "main.py"]
