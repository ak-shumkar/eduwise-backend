import pytest

from rest_framework.test import APIClient

from ..models import Institution, InstitutionType
from eduwise.locations.models import City, Country, Province

client = APIClient()


@pytest.mark.django_db
@pytest.fixture
def country():
    return Country.objects.create(name='United States')


@pytest.fixture
@pytest.mark.django_db
def province(country):
    return Province.objects.create(name='Massachusetts', country=country)


@pytest.fixture
@pytest.mark.django_db
def city(province, country):
    return City.objects.create(name='Boston', province=province, country=country)


@pytest.fixture
@pytest.mark.django_db
def institutions(city):
    institution_type = InstitutionType.objects.create(name='university')
    names = ['Harvard', 'MIT', 'Princeton', 'Cambridge', 'ITMO', 'Tsinghua', 'Nanyang', 'UNIST',
             'Manas', 'METU', 'Waterloo', 'Stanford', 'Oxford', 'Toronto', 'Duke']
    for name in names:
        Institution.objects.create(name=name, city=city, institution_type=institution_type)


@pytest.mark.django_db
def test_search_institutions(institutions):
    response = client.get('/api/institutions/?search=Toronto')
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]['name'] == 'Toronto'
