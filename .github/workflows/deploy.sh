# gunicorn config resides in /etc/systemd/system/gunicorn.service
sudo systemctl stop gunicorn
pip install --upgrade pip
pip install pipenv
pipenv install --deploy --system
python manage.py migrate
python manage.py collectstatic --no-input
sudo systemctl daemon-reload
sudo systemctl start gunicorn

# Debug postgres on server
# See if pg clusters are up: pg_clusters
# Restart postgres: sudo systemctl start postgresql@9.5-main.service