FROM registry.gitlab.akhcheck.ru/tp2024/registry/python:3.12

WORKDIR /
COPY . /

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]
