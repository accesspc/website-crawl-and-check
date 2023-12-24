FROM python:slim

COPY requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app /app

WORKDIR /app

ENTRYPOINT [ "python3", "-u", "main.py" ]
