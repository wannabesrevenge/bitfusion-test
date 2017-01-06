FROM alpine:3.5

RUN apk add --update py2-pip curl
RUN pip install --upgrade pip
RUN pip install flask

ADD server.py ./

HEALTHCHECK --interval=5s \
   CMD curl --fail http://localhost:8888/hello || exit 1

CMD ["python", "server.py"]
