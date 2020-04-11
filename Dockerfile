# TODO alpine
FROM python:3-slim

ENV PYTHONDONTWRITEBYTECODE yes
ENV PYTHONUNBUFFERED yes

ENV BUILD_DEPS g++ gcc librocksdb-dev libsnappy-dev libbz2-dev liblz4-dev zlib1g-dev

WORKDIR /app

RUN apt-get update \
  && apt-get install -y ${BUILD_DEPS}

COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN apt-get purge -y ${BUILD_DEPS}

COPY ./ ./

ENTRYPOINT ["/usr/local/bin/python"]
CMD ["main.py", "--daemon"]
