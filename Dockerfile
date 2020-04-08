FROM python:3-slim

ENV PYTHONDONTWRITEBYTECODE yes
ENV PYTHONUNBUFFERED yes

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./ ./
RUN mv /app/entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/bin/bash"]
CMD ["/entrypoint.sh"]
