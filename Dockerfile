FROM geographica/postgis

MAINTAINER Daniel de los Reyes "danirele10@gmail.com"

EXPOSE 5000

ADD . /code

WORKDIR /code

RUN apt-get update &&\
	cat /code/packages.txt | xargs apt-get -y --allow-unauthenticated install

RUN ls -a

RUN make

RUN ls -a

# Run server
CMD ["make", "run"]
