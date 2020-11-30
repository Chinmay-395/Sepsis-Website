#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/Chinmay-395/Sepsis-Website.git'

PROJECT_BASE_PATH='/usr/local/apps/Sepsis-Website'

echo "Installing dependencies..."
apt-get update
apt-get install -y python3-dev python3-venv sqlite python-pip supervisor nginx git

# Create project directory
mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH

# Create virtual environment
mkdir -p $PROJECT_BASE_PATH/env
python3 -m venv $PROJECT_BASE_PATH/env

# Install python packages
$PROJECT_BASE_PATH/env/bin/pip install -r $PROJECT_BASE_PATH/requirements.txt
$PROJECT_BASE_PATH/env/bin/pip install uwsgi==2.0.18

# Run migrations and collectstatic
cd $PROJECT_BASE_PATH
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
$PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput

# Configure supervisor
cp $PROJECT_BASE_PATH/deploy/supervisor_sepsis_diagnostic_system.conf /etc/supervisor/conf.d/sepsis_diagnostic_system.conf
supervisorctl reread
supervisorctl update
supervisorctl restart sepsis_diagnostic_system

# Configure nginx
cp $PROJECT_BASE_PATH/deploy/nginx_sepsis_diagnostic_system.conf /etc/nginx/sites-available/sepsis_diagnostic_system.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/sepsis_diagnostic_system.conf /etc/nginx/sites-enabled/sepsis_diagnostic_system.conf
systemctl restart nginx.service

echo "DONE! :)"
