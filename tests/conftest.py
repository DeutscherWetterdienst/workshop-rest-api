import pytest
from fastapi.testclient import TestClient

from my_rest_api import app


@pytest.fixture
def client():
    return TestClient(app)
