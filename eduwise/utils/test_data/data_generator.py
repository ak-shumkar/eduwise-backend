import requests
from django.db import IntegrityError

from eduwise.locations.models import Country, Province, City


def generate_countries():
    try:
        response = requests.get('https://restcountries.com/v3.1/all')
    except Exception as e:
        print(e)
        print('Cannot connect to countries API')
        return

    countries = response.json()
    for country in countries:
        try:
            name = country['name']['common']
        except KeyError:
            print('Cannot extract name')
            continue

        try:
            iso_code = country['cca3']
        except KeyError:
            print('Cannot extract iso code')
            continue

        try:
            Country.objects.create(name=name, iso_code=iso_code)
        except Exception as e:
            print(e)


def generate_provinces():
    try:
        countries = Country.objects.all()
    except Exception as e:
        print(e)
        print('Cannot connect to database')
        return

    for country in countries:
        try:
            response = requests.post('https://countriesnow.space/api/v0.1/countries/states',
                                     data={"country": country.name})
        except Exception as e:
            print(e)
            print(f'Cannot get states of country {country.name}')
            continue

        try:
            data = response.json()
        except Exception as e:
            print(e)
            continue

        try:
            states = data['data']['states']
        except KeyError:
            print(f'Cannot extract states for {country.name}')
            continue

        for state in states:
            try:
                state_name = state['name']
            except KeyError:
                print('Cannot extract state name')
                continue

            try:
                Province.objects.create(name=state_name, country=country)
            except Exception as e:
                print(e)


def generate_cities():
    try:
        provinces = Province.objects.all()
    except Exception as e:
        print(e)
        print('Cannot connect to database')
        return

    for province in provinces:
        try:
            response = requests.post('https://countriesnow.space/api/v0.1/countries/state/cities',
                                     data={'country': province.country.name, 'state': province.name})
        except Exception as e:
            print(e)
            print(f'Cannot get cities in province {province.name}')
            continue

        try:
            data = response.json()
        except Exception as e:
            print(e)
            continue

        try:
            cities = data['data']
        except KeyError:
            print(f'Cannot extract cities for {province.name}')
            continue

        for city in cities:

            try:
                City.objects.create(name=city, country=province.country, province=province)
            except IntegrityError:
                print(f'City {city, province.name, province.country.name} already exists')


# print('GENERATING COUNTRIES...')
# generate_countries()
# print('GENERATING PROVINCES...')
# generate_provinces()
print('GENERATING CITIES...')
generate_cities()
