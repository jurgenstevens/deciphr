BASE_DIR=$(cd "$(dirname "$0")" && pwd)
#/bin/bash
source /path/to/virtualenv/bin/activate

# Your other commands here
python -m pip install --upgrade pip3
pip3 install -r requirements.txt
pip3 install gunicorn
pip3 install django
pip3 install python-dotenv
pip3 install psycopg2
pip3 install psycopg2-binary
pip3 install dj_database_url
pip3 install
python manage.py createsuperuser
python manage.py makemigrations deciphr
python manage.py migrate
python manage.py runserver

if [[ $CREATE_SUPERUSER ]];
then
  python manage.py createsuperuser --no-input
fi

export BASE_DIR