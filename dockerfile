#docker file
FROM ubuntu

MAINTAINER geomongo version: 0.1
# Installation:
# Import MongoDB public GPG key AND create a MongoDB list file
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv 7F0CEB10
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee /etc/apt/sources.list.d/10gen.list
# Add the application resources URL
RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main universe" >> /etc/apt/sources.list
RUN	echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y \ 
		python \
		python-dev \ 
		python-distribute \
		python-pip \
		apache2 \
		libapache2-mod-wsgi \
		mongodb \
		curl \
		git \
		supervisor \
		x11vnc \
		xvfb \
		firefox \
                tidy \
		&& apt-get clean && rm -rf /var/lib/apt/lists/*

#Create the MongoDB data directory
RUN mkdir -p /data/db

#Apache config
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2

#Supervisor config
ENV SUPERVISOR_LOG_DIR /var/log/supervisor

RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR $SUPERVISOR_LOG_DIR

RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

EXPOSE 80
EXPOSE 27017

RUN mkdir /app

ADD scripts/req* /app/scripts/
ADD scripts/setup_pip* /app/scripts/

WORKDIR /app
RUN ["scripts/setup_pip_dependencies.sh"]

CMD ["scripts/docker_run.sh"]

