import pytest
import random

from starlette.testclient import TestClient
from starlette.status import HTTP_200_OK


@pytest.mark.parametrize('n_instances', range(1, 10))
def test_predict(n_instances: int, test_client: TestClient):
    for n in range(n_instances):
        response = test_client.get('/predict/')
        print(response)
        assert response.status_code == HTTP_200_OK
