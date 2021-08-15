FROM python:3.9

WORKDIR /

COPY . /

RUN apt-get update && apt-get install -y cmake && python -m pip install -r requirements.txt

CMD ["python", "run.py"]
