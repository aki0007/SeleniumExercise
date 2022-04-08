import pytest
from tests.api.api_login_helper import *


@pytest.mark.api
def test_backend_login():
    login_request()
