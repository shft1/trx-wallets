import pytest
from fastapi.testclient import TestClient

from app.core.db import get_async_session
from app.main import app
from tests.conftest import override_db


@pytest.fixture
def client():
    app.dependency_overrides = {}
    app.dependency_overrides[get_async_session] = override_db

    with TestClient(app) as client:
        yield client
