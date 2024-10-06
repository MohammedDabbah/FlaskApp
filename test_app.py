import pytest
from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_ask_endpoint(client):
    response = client.post('/ask', json={'question': 'What is the capital of France?'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'answer' in json_data
