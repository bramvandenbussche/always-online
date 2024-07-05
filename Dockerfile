FROM python:3

ENV SRC_DIR /app
COPY src/* ${SRC_DIR}/
WORKDIR ${SRC_DIR}

ENV PYTHONUNBUFFERED=1

EXPOSE 80

CMD ["python", "server.py"]
