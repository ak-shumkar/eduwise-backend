import requests

from concurrent import futures
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.db.utils import IntegrityError
from bs4 import BeautifulSoup
from eduwise.locations.models import City
from eduwise.institutions import Institution, InstitutionType
from eduwise.utils.logging.logger import logger


def create_university(given_country, name, website):
    try:
        response = requests.get(
            url=f'https://en.wikipedia.org/wiki/{name.replace(" ", "_")}',
        )
    except Exception as e:
        print(e)
        return
    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        info_box = soup.find("table", {"class": "infobox vcard"})
        location = info_box.find('td', {"class": "infobox-data adr"})
    except Exception as e:
        print(e)
        return

    try:
        city = location.find('div', {"class": "locality"}).find('a').text
    except:
        try:
            city = location.find('div', {"class": "locality"}).text
        except:
            city = None
    try:
        province = location.find('div', {"class": "state"}).find('a').text
    except:
        try:
            province = location.find('div', {"class": "state"}).text
        except:
            province = None
    try:
        country = location.find('div', {"class": "country-name"}).find('a').text
    except:
        try:
            country = location.find('div', {"class": "country-name"}).text
        except:
            country = None
    if not province:
        try:
            city, province = city.split(', ')
        except:
            pass

    try:
        assert given_country == country
    except AssertionError:
        print(given_country, "!=", country)
        return

    print(city,"|", province, "|", country)
    try:
        if City.objects.filter(country__name=country, province__name=province, name=city).exists():
            city_object = City.objects.get(country__name=country, province__name=province, name=city)
        else:
            logger.exception(f'City {name} does not exist')
            return
    except (MultipleObjectsReturned, ObjectDoesNotExist):
        logger.exception(f'Missing city {city}')
    else:
        try:
            tp = InstitutionType.objects.get(name='University')
            if Institution.objects.filter(name=name, city=city_object).exists():
                logger.exception(f'University {name} already exists')
            else:
                Institution.objects.create(name=name, city=city_object, address="", about="", website=website, institution_type=tp)
        except IntegrityError:
            logger.exception(f'University {name} already exists')
        except Exception as e:
            logger.exception(e.__cause__)
        else:
            logger.log(1, f'University {name} is created')


def parse_and_create(datum):
    try:
        country = datum['country']
        try:
            website = datum['web_pages'][0]
        except KeyError:
            website = ""
        name = datum['name']
    except KeyError:
        logger.exception('Cannot extract name or country name')
    else:
        logger.info(f'University: {name}')
        create_university(country, name, website)


def generate_universities():
    try:
        response = requests.get('http://universities.hipolabs.com/search?')
    except Exception as e:
        print(e)
        print('Cannot connect to http://universities.hipolabs.com')
        return

    try:
        assert response.ok
    except AssertionError:
        print('Response is not ok')

    try:
        data = response.json()
    except Exception as e:
        print(e)
        return

    with futures.ThreadPoolExecutor(100) as executor:
        executor.map(parse_and_create, data)


print('GENERATING UNIVERSITIES...')
generate_universities()
