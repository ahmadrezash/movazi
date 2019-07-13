FROM python:3
# RUN apt-get update && apt-get install -y gettext libjpeg-dev libpng-dev zlib1g-dev build-essential cron \
#     && pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir -U pip \
#     && pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir uwsgi \
#  && apt-get clean

WORKDIR /usr/src/app

RUN git clone https://057425d2c264b6336b7bd6a43aec8976559a01b3@github.com/ahmadrezash/movazi.git
WORKDIR /usr/src/app/movazi
RUN git pull origin master


COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN echo "yes" | python manage.py collectstatic

CMD gunicorn movazi.wsgi:application --bind 0.0.0.0:8000 --keep-alive 2

EXPOSE 8000