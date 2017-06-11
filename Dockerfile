FROM ubuntu
MAINTAINER Endika Iglesias

RUN apt-get update \
    && apt-get dist-upgrade -y \
    && apt-get install -y \
    golang-go

ADD . /home/weertik

EXPOSE 8004

CMD ["go", "run", "/home/weertik/run.go"]
