BASE_DIR=$(cd "$(dirname "$0")" && pwd)
#/bin/bash
source /path/to/virtualenv/bin/activate

# Your other commands here

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

export BASE_DIR