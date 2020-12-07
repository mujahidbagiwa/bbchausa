import pytest
from starlette.testclient import TestClient

from ..main import app
from ..src.model import get_model
from .mock_model import MockModel


def get_mock_model():
    model = MockModel()
    return model


app.dependency_overrides[get_model] = get_mock_model


@pytest.fixture()
def test_client():
    return TestClient(app)


list.index()