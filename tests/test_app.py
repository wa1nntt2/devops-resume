import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    """Тест главной страницы"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'DevOps' in response.data

def test_health_endpoint(client):
    """Тест health check"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {'status': 'healthy'}
