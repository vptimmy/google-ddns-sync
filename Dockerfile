FROM registry.vptimmy.ddns.net/dockerhub-proxy/library/python:3 AS build
COPY ./app/requirements.txt /requirements.txt
RUN apt update
RUN pip3 install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir requests
RUN pip3 install --no-cache-dir -r /requirements.txt

RUN echo "user:x:1000:1000:Unprivileged User::/bin/false" >> /etc/passwd
USER 1000

COPY --chown=1000 ./app /app
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["main.py"]