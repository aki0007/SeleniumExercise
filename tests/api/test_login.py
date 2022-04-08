import pytest

from tests.api.login_helper import login_request


@pytest.mark.api
def test_backend_login():
    login_request()
