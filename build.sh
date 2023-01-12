BASE_DIR=$(cd "$(dirname "$0")" && pwd)
#/bin/bash
set -o errexit
source /path/to/virtualenv/bin/activate

# Your other commands here
pip install gunicorn
pip install django
pip install python-dotenv
pip install psycopg2
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

export BASE_DIR