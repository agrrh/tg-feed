FROM python:3-slim

ENV PYTHONDONTWRITEBYTECODE yes
ENV PYTHONUNBUFFERED yes

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./ ./

ENTRYPOINT ["/usr/local/bin/python"]
CMD ["main.py"]
