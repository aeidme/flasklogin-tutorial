#!/usr/bin/env bash
export GOOGLE_APPLICATION_CREDENTIALS='key.json'
export FLASK_APP=wsgi.py
export FLASK_ENV=development
export FLASK_DEBUG=1
export APP_CONFIG_FILE=config.py
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
chmod +x cloud_sql_proxy
./cloud_sql_proxy -instances="fourth-flag-270813:us-central1:attendance-database"=tcp:3306 &
P1=$!
cd /Photos-Docker-Flask
flask run
P2=$!
wait $P1 $P2

