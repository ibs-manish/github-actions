FROM python:3.8-slim-buster
WORKDIR /github-actions
COPY . .
RUN pip install awscli
RUN chmod +x script.sh
CMD cd /github-actions && ./script.sh
