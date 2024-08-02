FROM python:3.8-slim-buster

ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY

ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}

WORKDIR /github-actions
COPY . .

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir awscli

RUN pip install awscli
RUN chmod +x script.sh
CMD cd /github-actions && ./script.sh
