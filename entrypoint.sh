#!/usr/bin/env bash
#!/bin/sh

#set -e

# Start Cron task scheduler
service cron start
# save environment varibles to file in order to be loaded in cron jobs
env > /etc/environment


cd /code

## Add x to variable and  compare whit to make sure it's what we want, and if it not set, it still working
## 'x$VAR_NAME' = 'xCOMPARE_WHIT'
if [ "x$PIP_INSTALL_REQUIREMENTS" = 'xon' ]; then

 echo -e "\n\n* ****************************************************************************** *"
 echo -e "* \t\t\t\t\t\t\t\t\t\t *"
 echo -e "* \t\t\t\tINSTALLING REQUIREMENTS\t\t\t\t *"
 echo -e "* \t\t\t\t\t\t\t\t\t\t *"
 echo -e "* ****************************************************************************** *"

 pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir -r requirements.txt
fi

if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then

 echo -e "\n\n* ****************************************************************************** *"
 echo -e "* \t\t\t\t\t\t\t\t\t\t *"
 echo -e "* \t\t\t\tRUNNING MIGRATIONS\t\t\t\t *"
 echo -e "* \t\t\t\t\t\t\t\t\t\t *"
 echo -e "* ****************************************************************************** *"

 python3 manage.py migrate --noinput
fi

if [ "x$DJANGO_MANAGEPY_COMPILEMESSAGES" = 'xon' ]; then
 echo -e "\n\n* ****************************************************************************** *"
 echo -e "* \t\t\t\t\t\t\t\t\t\t *"
 echo -e "* \t\t\t\tCOMPILING MESSAGES\t\t\t\t *"
 echo -e "* \t\t\t\t\t\t\t\t\t\t *"
 echo -e "* ****************************************************************************** *"

 python3 manage.py compilemessages
fi


if [ "x$DJANGO_MANAGEPY_COLLECTSTATIC" = 'xon' ]; then
 echo -e "\n\n* ****************************************************************************** *"
 echo -e "* \t\t\t\t\t\t\t\t\t\t *"
 echo -e "* \t\t\t\tCOLLECTING STATICS\t\t\t\t *"
 echo -e "* \t\t\t\t\t\t\t\t\t\t *"
 echo -e "* ****************************************************************************** *"

 #python3 manage.py collectstatic <<<yes
 python3 manage.py collectstatic --noinput
fi

echo -e "\n\n* ****************************************************************************** *"
echo -e "* \t\t\t\t\t\t\t\t\t\t *"
echo -e "* \t\t\t\t\tuWSGI Config\t\t\t\t *"
echo -e "* \t\t\t\t\t\t\t\t\t\t *"
echo -e "* ****************************************************************************** *\n"
printenv | grep UWSGI_

echo -e "\n\n* ****************************************************************************** *"
echo -e "* \t\t\t\t\t\t\t\t\t\t *"
echo -e "* \t\t\t\t\tRUNNING SERVER\t\t\t\t *"
echo -e "* \t\t\t\t\t\t\t\t\t\t *"
echo -e "* ****************************************************************************** *"
## run this config file
#uwsgi --ini /code/uwsgi.ini

## look for config files in this directory, auto start, auto restart on configfile changes
## make sure you linked config file into this directory on Dockerfile
#uwsgi --emperor /etc/uwsgi/vassals

## configured using environment variables
uwsgi --http-auto-chunked --http-keepalive=3000
