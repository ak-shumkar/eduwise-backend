import requests
from django.db.utils import IntegrityError

from eduwise.locations.models import Country
from eduwise.utils.logging.logger import logger


def generate_countries():
    try:
        response = requests.get('https://restcountries.com/v3.1/all')
    except Exception as e:
        logger.exception(e)
        logger.exception('Cannot connect to countries API')
        return

    countries = response.json()
    for country in countries:
        try:
            name = country['name']['common']
        except KeyError:
            logger.exception('Cannot extract name')
            continue

        try:
            iso_code = country['cca3']
        except KeyError:
            logger.exception('Cannot extract iso code')
            continue

        try:
            Country.objects.create(name=name, iso_code=iso_code)
        except IntegrityError:
            logger.error(f'Country {name} already exists')
        except Exception as e:
            logger.exception(e)
        else:
            logger.log(1, f'Country {name} created')


logger.info('GENERATING COUNTRIES...')
generate_countries()
