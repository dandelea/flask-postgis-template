# Fresh installation test
#
# To run this: sudo docker build .

FROM ubuntu
MAINTAINER Daniel de los Reyes

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y                             && \
    apt-get install software-properties-common -y

# Add PostgreSQL's repository.
# Add PostGIS' repository from Ubuntugis.
RUN apt-get update -y                             && \
	echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
	add-apt-repository ppa:ubuntugis/ubuntugis-unstable

RUN apt-get update -y

ADD ./ /code/

RUN cat /code/packages.txt | xargs apt-get -y --force-yes install

# Create a PostgreSQL role named ``docker`` with ``docker`` as the password and
# then create a database `madrid` owned by the ``docker`` role.
# Note: here we use ``&&\`` to run commands one after the other - the ``\``
#       allows the RUN command to span multiple lines.
RUN    /etc/init.d/postgresql start &&\
    psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" &&\
    createdb -O docker madrid

# Adjust PostgreSQL configuration so that remote connections to the
# database are possible.
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.conf

# And add ``listen_addresses`` to ``/etc/postgresql/9.3/main/postgresql.conf``
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf

# Expose the PostgreSQL port
EXPOSE 5432

# Add VOLUMEs to allow backup of config, logs and databases
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

RUN sudo -u postgres psql -c "CREATE EXTENSION postgis; CREATE EXTENSION postgis_topology;" madrid

RUN cd /code/ && make setup

RUN cd /code/ && make run