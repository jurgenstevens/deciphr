#/bin/bash
source /path/to/virtualenv/bin/activate

# Your other commands here

python manage.py makemigrations
python manage.py migrate
python manage.py runserver