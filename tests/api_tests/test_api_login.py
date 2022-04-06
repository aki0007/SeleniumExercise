import pytest
from tests.api_tests.api_login_helper import *


@pytest.mark.api
def test_backend_login():
    login_request()
