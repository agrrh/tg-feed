FROM python:3-slim

ENV PYTHONDONTWRITEBYTECODE yes
ENV PYTHONUNBUFFERED yes

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./ ./
COPY ./entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/bin/bash"]
CMD ["/entrypoint.sh"]
