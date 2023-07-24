from apistar import test

from app import app, cars

client = test.TestClient(app)


def test_list_cars():
    response = client.get('/')
    assert response.status_code == 200
    cars = response.json()
    assert len(cars) == 1000
    assert type(cars) == list
    car = cars[0]
    expected = {"id": 1, "manufacturer": "GMC", "model": "3500", "year": 1998, "vin": "KMHHT6KD2CU924395"}
    assert car == expected
    last_id = cars[-1]['id']
    assert last_id == 1000


def test_create_car():
    new_car = dict(manufacturer='Toyota',
                   model='ThisCrazy',
                   year=2008,
                   vin='19vh')
    response = client.post('/', data=new_car)
    assert response.status_code == 201
    assert len(cars) == 1001

    response = client.get('/1001/')
    assert response.status_code == 200
    expected = {"id": 1001, "manufacturer": "Toyota", "model": "ThisCrazy", "year": 2008, "vin": "19vh"}
    assert expected == response.json()
