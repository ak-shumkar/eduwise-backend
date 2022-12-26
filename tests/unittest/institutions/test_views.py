import pytest


@pytest.mark.django_db
def test_search_by_name(client, usa_universities):
    response = client.get('/api/institutions/?search=Harvard')
    assert response.status_code == 200
    data = response.json()['results']
    print(data)
    assert len(data) == 1
    assert data[0]['name'] == 'Harvard University'


@pytest.mark.django_db
def test_filter_by_city(client, usa_universities, boston, boston_universities):
    response = client.get(f'/api/institutions/?city={boston.id}')
    data = response.json()['results']
    print(data)
    assert response.status_code == 200
    assert len(data) == len(boston_universities)
