sudo systemctl stop gunicorn
pip install --upgrade pip
pip install pipenv
pipenv install --deploy --system
python manage.py migrate
python manage.py collectstatic --no-input
sudo systemctl daemon-reload
sudo systemctl start gunicorn --error-logfile /var/log/gunicorn/error.log --access-logfile /var/log/gunicorn/access.log
