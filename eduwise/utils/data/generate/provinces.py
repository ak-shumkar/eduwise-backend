import requests

from concurrent import futures
from django.db.utils import IntegrityError

from eduwise.locations.models import Country, Province
from eduwise.utils.logging.logger import logger


def generate_country_provinces(country):
    try:
        response = requests.post('https://countriesnow.space/api/v0.1/countries/states', data={"country": country.name})
    except Exception as e:
        logger.exception(e)
        logger.exception(f'Cannot get states of country {country.name}')
        return
    try:
        data = response.json()
    except Exception as e:
        logger.exception(e)
        return
    try:
        states = data['data']['states']
    except KeyError:
        logger.exception(f'Cannot extract states for {country.name}')
        return

    for state in states:
        try:
            state_name = state['name']
        except KeyError:
            logger.exception('Cannot extract state name')
            continue

        try:
            Province.objects.create(name=state_name, country=country)
        except IntegrityError:
            logger.exception(f'Province {state_name}, {country} already exists')
        except Exception as e:
            logger.exception(e)
        else:
            logger.log(1, f'Province {state_name}, {country} created')


def generate_provinces():
    try:
        countries = Country.objects.all()
    except Exception as e:
        logger.exception(e)
        logger.exception('Cannot connect to database')
        return

    with futures.ThreadPoolExecutor(10) as executor:
        executor.map(generate_country_provinces, countries)


logger.info('GENERATING PROVINCES...')
generate_provinces()
