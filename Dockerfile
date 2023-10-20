FROM python:3.10.2-slim-buster
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY pipelin.pkl /code/pipelin.pkl
RUN pip install --no-cache-dir -- upgrade -r /code/requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]

