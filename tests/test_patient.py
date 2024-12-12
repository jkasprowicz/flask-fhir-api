import pytest

from app import create_app, db


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        
        yield client

def test_create_patient(client):
    response = client.post('/Patient', json= {
        "id": "123",
        "resourceType": "Patient",
        "name": [{"family": "Doe", "given": ["John"]}],
        "gender": "male",
        "birthDate": "1980-01-01"
    })
    assert response.status_code == 201


    