FROM python:3.10-slim

EXPOSE 80

WORKDIR /code

COPY ./requirements.txt  /code/requirements.txt
RUN pip install -r requirements.txt

COPY ./src /code/src
# CMD ["uvicorn", "--host", "0.0.0.0", "src.main:app"]
CMD ["gunicorn", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker",\
 "--bind","0.0.0.0:80", "src.main:app"]