from alpine:latest

RUN apk add --no-cache python3-dev
FROM python:3
WORKDIR C:\Users\Nick\Documents\PROJETOS GIT\distance-calculator-task-test
COPY requirements.txt ./

RUN pip install --upgrade pip && apt-get update && apt-get install -y cmake && python -m pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "run.py"]
