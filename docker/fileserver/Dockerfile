FROM python:3.9

WORKDIR /home/fastapi

COPY /docker/fileserver/requirements.txt /home/fastapi/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /home/fastapi/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
