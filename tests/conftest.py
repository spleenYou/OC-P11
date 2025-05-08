import pytest
import server


@pytest.fixture
def client():
    return server.app.test_client()


@pytest.fixture
def clubs():
    return server.clubs
