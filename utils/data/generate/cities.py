import requests

from concurrent import futures
from django.db.utils import IntegrityError

from locations.models import Province, City
from utils.logging.logger import logger


def create_cities(city, province):
    try:
        City.objects.create(name=city, country=province.country, province=province)
    except IntegrityError:
        logger.exception(f'City {city, province.name, province.country.name} already exists')
    except Exception as e:
        logger.exception(e)
    else:
        logger.log(1, f'City {city, province.name, province.country.name} created')


def generate_province_cities(province):
    try:
        response = requests.post('https://countriesnow.space/api/v0.1/countries/state/cities',
                                 data={'country': province.country.name, 'state': province.name})
    except Exception as e:
        logger.exception(e)
        logger.exception(f'Cannot get cities in province {province.name}')
        return

    try:
        data = response.json()
    except Exception as e:
        logger.exception(e)
        return

    try:
        cities = data['data']
    except KeyError:
        logger.exception(f'Cannot extract cities for {province.name}')
        return

    for city in cities:
        create_cities(city, province)


def generate_cities():
    try:
        provinces = Province.objects.all()
    except Exception as e:
        logger.exception(e)
        logger.exception('Cannot connect to database')
        return

    with futures.ThreadPoolExecutor(100) as executor:
        executor.map(generate_province_cities, provinces)


print('GENERATING CITIES...')
generate_cities()
