FROM python:3-slim

ENV PYTHONDONTWRITEBYTECODE yes
ENV PYTHONUNBUFFERED yes

WORKDIR /app

RUN apt-get update \
  && apt-get install -y \
    g++ \
    gcc \
    librocksdb-dev \
    libsnappy-dev \
    libbz2-dev \
    liblz4-dev \
    zlib1g-dev

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /entrypoint.sh

COPY ./ ./

ENTRYPOINT ["/bin/bash"]
CMD ["/entrypoint.sh"]
