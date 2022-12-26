import pytest

from eduwise.institutions.models import InstitutionType, Institution
from eduwise.locations.models import Country, Province, City


# --- Types ---
@pytest.mark.django_db
@pytest.fixture
def university():
    return InstitutionType.objects.create(name="University")


# --- Countries ---
@pytest.mark.django_db
@pytest.fixture
def usa():
    return Country.objects.create(name='United States')


@pytest.mark.django_db
@pytest.fixture
def uk():
    return Country.objects.create(name='United Kingdom')


# --- Provinces ---
@pytest.fixture
@pytest.mark.django_db
def massachusetts(usa):
    return Province.objects.create(name='Massachusetts', country=usa)


@pytest.fixture
@pytest.mark.django_db
def california(usa):
    return Province.objects.create(name='California', country=usa)


# --- cities ---
@pytest.fixture
@pytest.mark.django_db
def boston(massachusetts, usa):
    return City.objects.create(name='Boston', province=massachusetts, country=usa)


@pytest.fixture
@pytest.mark.django_db
def los_angeles(california, usa):
    return City.objects.create(name='Los Angeles', province=california, country=usa)


@pytest.fixture
@pytest.mark.django_db
def san_diego(california, usa):
    return City.objects.create(name='San Diego', province=california, country=usa)


# --- universities ---
@pytest.fixture
@pytest.mark.django_db
def boston_universities(boston, university):
    names = ['Massachusetts Institute of Technology', 'Harvard University', 'Boston College']
    objs = []
    for name in names:
        objs.append(Institution(name=name, institution_type=university, city=boston))

    return Institution.objects.bulk_create(objs)


@pytest.fixture
@pytest.mark.django_db
def usa_universities(boston_universities, san_diego, los_angeles, university):
    la_universities = ['University of California', 'Loyola Marymount University']
    san_diego_universities = ['University of San Diego', 'San Diego City College', 'San Diego State University']
    objs = []
    for name in la_universities:
        objs.append(Institution(name=name, institution_type=university, city=los_angeles))

    for name in san_diego_universities:
        objs.append(Institution(name=name, institution_type=university, city=san_diego))

    return Institution.objects.bulk_create(objs) + boston_universities
