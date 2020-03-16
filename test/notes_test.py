import pytest
from notes import create_app

@pytest.fixture
def client(request):
    app = create_app('flask_test.cfg')
    test_client = app.test_client()

    def teardown():
        pass

    return test_client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

