FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y gettext libjpeg-dev libpng-dev zlib1g-dev build-essential cron \
    && pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir -U pip \
    && pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir uwsgi \
 && apt-get clean

RUN mkdir /code
WORKDIR /code

ADD entrypoint.sh /entrypoint.sh

# Do this stuff on the build phaze of the image that use this as base-image
## Install requirements
ADD requirements.txt /code/requirements.txt
RUN pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir -r requirements.txt
## Add code to container
ADD . /code
RUN pip3 install uwsgi
RUN chown www-data:www-data ./
CMD [ "uwsgi", "uwsgi-conf.ini"]
ENV UWSGI_UID=www-data UWSGI_GID=www-data

# for uWSGI emperor mode
#RUN mkdir -p /etc/uwsgi/vassals
#RUN sudo ln -s /code/Deployment/uwsgi.ini /etc/uwsgi/vassals/

EXPOSE 3000

ENTRYPOINT ["bash","/entrypoint.sh"]
