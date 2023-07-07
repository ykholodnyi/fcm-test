FROM python:3.10-slim

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt

WORKDIR /data

CMD ["bash"]
