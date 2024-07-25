FROM python:slim
LABEL Robertas Reiciunas
EXPOSE 8000
HEALTHCHECK --interval=5s --timeout=5s CMD ["curl", "-f", "http://localhost:8000", "||", "exit", "1"]

RUN apt-get update \
  && apt-get -y install curl \
  && apt-get clean \
  && apt-get -y purge

COPY requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app /app

USER 33
WORKDIR /app

ENTRYPOINT [ "python3", "app.py" ]
