import pytest
from api_testing.api_login import *


@pytest.mark.backend
def test_backend_login():
    login_request()