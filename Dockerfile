FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./database /code/database
COPY ./models /code/models
COPY ./repositories /code/repositories
COPY ./main.py /code/
COPY ./routes /code/routes
COPY ./schemas /code/schemas
COPY ./services /code/services

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
