import pytest

from eduwise.programs.models import Term

from eduwise.locations.models import Country


@pytest.mark.django_db
@pytest.fixture
def countries():
    country_names = ['United States of America', 'Canada', 'United Kingdom', 'China', 'Korea', 'Singapore', 'Germany',
                     'Russia']
    iso_codes = ['USA', 'CAN', 'GBR', 'CHN', 'KOR', 'SGP', 'GER', 'RUS']
    countries = []
    for i in range(len(iso_codes)):
        countries.append(Country.objects.create(name=country_names[i], iso_code=iso_codes[i]))

    return countries


@pytest.mark.django_db
@pytest.fixture
def provinces(countries):
    provinces_names = [
        {'USA': ['California', 'Massachusetts', 'Pennsylvania', 'Texas', 'Illinois']},
        {'CAN': ['Ontario', 'Quebec', '']}
    ]
    return provinces_names


def cities(provinces):
    city_names = [
        {('USA', 'California'): ['Los Angeles', 'San Diego', 'San Jose', 'San Fransisco']}
    ]
    return city_names


@pytest.fixture
def terms():
    seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
    years = [2022, 2023, 2024, 2025]
    terms = []
    for season in seasons:
        for year in years:
            terms.append(Term.objects.create(season=season, year=year))

    return terms


@pytest.mark.django_db
@pytest.fixture
def programs():
    return None
