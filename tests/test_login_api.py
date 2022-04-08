import pytest

from base.helpers.login_api import login_request


@pytest.mark.api
def test_backend_login():
    login_request()
