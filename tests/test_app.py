import pytest
import sys
import os

# Добавляем корневую директорию в путь
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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
    # Проверяем наличие ключевых слов (в декодированном виде)
    data = response.data.decode('utf-8')
    assert 'Backend' in data or 'DevOps' in data or 'Слонов' in data

def test_static_css(client):
    """Тест CSS файла"""
    response = client.get('/static/style.css')
    assert response.status_code == 200
    data = response.data.decode('utf-8')
    assert 'glass-card' in data or 'body' in data

def test_health_endpoint(client):
    """Тест health check"""
    response = client.get('/health')
    assert response.status_code == 200
    assert b'healthy' in response.data
