# yeongdo-Link Cooperation

## 1. Method of installation
1. git clone URL
2. pip install -r requirements.txt (make venv)
3. python manage.py makemigrations
4. python manage.py migrate

## 2. Push data of survey at database
1. python manage.py shell
2. from analysis.utils import insert_surveys
3. insert_surveys(path) --> path is excel file with survey data