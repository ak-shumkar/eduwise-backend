python manage.py migrate
python manage.py collectstatic
sudo systemctl stop gunicorn
sudo systemctl daemon-reload
sudo systemctl start gunicorn