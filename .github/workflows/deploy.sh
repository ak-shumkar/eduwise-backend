sudo systemctl stop gunicorn
pip install --upgrade pip
pip install pipenv
pipenv install --deploy --system
python manage.py migrate
python manage.py collectstatic
sudo systemctl daemon-reload
sudo systemctl start gunicorn